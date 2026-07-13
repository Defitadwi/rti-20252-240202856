# Tahap 1 — Perancangan Arsitektur & Skema Database

**Status:** Selesai

---

## 1. Komponen Sistem

1. **API Gateway (Go, Echo)** — Berfungsi sebagai gerbang utama (entry point) yang menerima citra daun padi dari pengguna, melakukan pre-processing (seperti augmentasi pengurangan brightness 25%), dan meneruskannya ke model CNN untuk deteksi.
2. **Redis (L1 Cache, murni cache JWKS)** — Berfungsi sebagai cache efisien untuk menyimpan JSON Web Key Set (JWKS) guna mempercepat proses autentikasi pengguna saat mengakses API.
3. **PostgreSQL (L2 / Source of Truth + Rate Limit Counter Permanen)** — Berfungsi sebagai pusat penyimpanan data permanen yang mencakup data profil pengguna, log rate limit untuk mencegah penyalahgunaan sistem, serta catatan riwayat hasil klasifikasi penyakit.  

## 2. Alur Resolusi Kunci (Mitigasi)

```
Request (Gambar Daun + JWT) → Gateway parsing header JWT → ambil `kid`
  │
  ├─ Cek Redis positive cache (jwks:kid:<kid>)
  │     ├─ HIT  → verifikasi signature → lanjut
  │     └─ MISS ↓
  │
  ├─ Cek Redis negative cache (jwks:negative:<kid>)
  │     ├─ HIT  → tolak langsung (401), tanpa query DB
  │     └─ MISS ↓
  │
  ├─ UPSERT & cek rate_limit_counters di PostgreSQL (atomic, per client_ip + window)
  │     ├─ EXCEEDED → tolak (429) + set Redis negative cache
  │     └─ OK ↓
  │
  └─ Query PostgreSQL (signing_keys WHERE kid = ? AND is_active)
  |      ├─ FOUND     → isi Redis positive cache → verifikasi signature
  |     └─ NOT FOUND → set Redis negative cache → tolak (401)
  |
  |
  |
  └─ Load Model (InceptionV3) → Pre-processing (Resize + Brightness 25%) → Prediksi
        └─ Return Hasil (Nama Penyakit: Brownspot/Blas/HDB + Akurasi)

```

Penyesuaian Mekanisme Fail-Closed & Baseline dengan Konteks Jurnal
- Implementasi Baseline Mode (CACHE_MODE=none):
Pada mode ini, sistem bekerja seperti deteksi manual/dasar di mana setiap request langsung membebani database PostgreSQL untuk otentikasi. Dalam penelitian, ini disimulasikan untuk menguji apakah sistem tetap stabil meskipun tidak menggunakan teknik caching yang optimal untuk memproses identifikasi citra secara real-time.

- Logika Fail-Closed (Ketahanan Sistem):

    - Kegagalan Redis: Jika Redis tidak dapat diakses, sistem secara otomatis fallback langsung ke PostgreSQL untuk verifikasi kunci. Karena PostgreSQL juga menyimpan rate-limit counter, keamanan akses ke API deteksi penyakit tetap terjaga dan tidak bisa disalahgunakan.

    - Kegagalan PostgreSQL: Jika PostgreSQL tidak dapat diakses, sistem akan menolak seluruh request (mengembalikan error). Ini adalah langkah kritikal karena tanpa basis data signing_keys, sistem tidak bisa memverifikasi legitimasi pengguna yang akan mengakses model CNN, sehingga mencegah akses yang tidak sah terhadap model deteksi penyakit padi Anda.

- Integrasi dengan Model CNN:
Sesuai dengan jurnal, model InceptionV3 yang digunakan dalam penelitian tersebut menuntut efisiensi. Oleh karena itu, mekanisme caching (Redis) yang Anda rancang sangat relevan untuk menjaga agar resource server tidak habis terpakai hanya untuk proses verifikasi JWT, sehingga performa inference (klasifikasi penyakit) dapat berjalan lebih lancar dan real-time.
## 3. Skema Database (PostgreSQL)

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE rate_limits (
    client_ip INET PRIMARY KEY,
    request_count INTEGER DEFAULT 0,
    window_start TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE signing_keys (
    kid VARCHAR(50) PRIMARY KEY,
    key_data TEXT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE disease_info (
    id SERIAL PRIMARY KEY,
    disease_name VARCHAR(100) NOT NULL, 
    description TEXT,
    treatment_suggestion TEXT
);

CREATE TABLE detection_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    image_path VARCHAR(255) NOT NULL,
    predicted_class_id INTEGER REFERENCES disease_info(id),
    accuracy_score DECIMAL(5, 4) NOT NULL, 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_signing_keys_active ON signing_keys(kid) WHERE is_active = TRUE;
CREATE INDEX idx_detection_history_user ON detection_history(user_id);
```
sistem mencatat metrik trafik secara mendalam ke dalam tabel traffic_logs dan rate_limits. Data ini mencakup metadata permintaan, status pemblokiran akses, hingga latensi inferensi model yang diukur dalam milidetik. Pengumpulan data secara permanen (non-TTL) ini menjadi fondasi krusial bagi Tahap 4, di mana pola trafik akan diekstraksi untuk membedakan antara legitimate traffic dan upaya serangan (DDoS atau brute force). Data tersebut kemudian dikorelasikan dengan tingkat akurasi serta efisiensi model InceptionV3 yang telah dilatih, guna membuktikan ketahanan operasional sistem dalam lingkungan produksi yang dinamis.

## 4. Skema Redis (Murni L1 Cache JWKS)

| Key Pattern | Tipe | TTL | Tujuan |
|---|---|---|---|
| `jwks:kid:<kid>` | STRING (JSON) | ~300s | Positive cache untuk kunci valid |
| `jwks:negative:<kid>` | STRING (`"1"`) | ~60s | Negative cache untuk kunci tidak valid |
| `infer:img_hash:<hash>` | STRING (JSON) | ~600s |Inference cache (menyimpan hasil prediksi gambar yang sama) |

## 5. Keputusan Teknis (Final)

1. **Mode eksperimen**: Satu binary gateway dengan toggle CACHE_MODE=none|hybrid. Fokus eksperimen adalah membandingkan latensi respons total saat sistem melakukan inferensi CNN, di mana $D_{perf}$ (penurunan performa) dihitung dari dampak verifikasi JWT terhadap throughput deteksi penyakit.
2. **Framework Gateway**: **Echo** Dipilih karena overhead yang sangat rendah, memungkinkan efisiensi CPU yang krusial untuk menjalankan pre-processing citra (augmentasi brightness 25%) sebelum masuk ke model CNN.
3. **Rate limiting**: counter permanen di **PostgreSQL**. Menggunakan atomic UPSERT untuk memastikan keamanan model dari serangan denial-of-service yang akan membebani GPU/CPU saat proses klasifikasi penyakit berlangsung.
4. **Identity Service**: **PostgreSQL `signing_keys` sebagai backing store. Arsitektur yang ramping untuk menjaga memory footprint server agar tetap fokus pada loading model InceptionV3 (yang memori-intensif).
5. **Redis client**: `go-redis/redis/v9` Digunakan untuk menekan latensi lookup JWKS hingga di bawah 1ms, memastikan proses verifikasi tidak menghambat latency deteksi penyakit padi yang seharusnya bisa diakses secara real-time.
6. **PostgreSQL driver**: `pgx` (dengan connection pooling). Penting untuk menangani traffic simultan dari petani/pengguna yang melakukan upload citra daun padi secara bersamaan.
7. **Skenario issuer**: Single issuer yang disederhanakan, sejalan dengan batasan dataset penelitian (3 jenis penyakit) guna memastikan fokus penelitian tetap pada efektivitas metode CNN dan efisiensi sistem pendukungnya.
