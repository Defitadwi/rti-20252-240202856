# Tahap 2 — Implementasi API Gateway (Go)

**Status:** Selesai
**Acuan arsitektur:** [tahap-1-arsitektur-dan-skema-database.md] Penelitian ini merancang sistem deteksi penyakit daun padi yang terdiri dari tiga proses utama: pre-processing, process, dan post-processing.
Pengembangan API Gateway ini bertujuan untuk menyediakan lapisan keamanan yang efisien agar model *InceptionV3* yang digunakan dalam klasifikasi penyakit daun padi (Blas, *Brownspot*, dan *Hawar Daun Bakteri*) dapat beroperasi secara optimal tanpa kendala latensi akibat verifikasi identitas yang berat.

**Lokasi kode:** [../05-kode/gateway/](../05-kode/gateway/)

---

## Tujuan
Sistem diimplementasikan dengan dua mode operasi melalui variabel lingkungan `CACHE_MODE` untuk tujuan eksperimen performa:
* **none (Baseline)**: Setiap permintaan melakukan *query* langsung ke `signing_keys` di PostgreSQL untuk menguji performa sistem tanpa lapisan *caching*.
* **hybrid (Mitigasi)**: Implementasi penuh *Redis L1 Cache* (positif/negatif) dan *rate-limit counter* permanen di PostgreSQL guna melindungi *resource* komputasi model CNN dari beban trafik berlebih.

## Deliverable

Pengembangan sistem telah memenuhi target deliverable berikut:
- [x] **Struktur Project Go**: DDD-lite per *bounded-context* (`jwks`, `ratelimit`, `jwtauth`, `httpapi`, `platform`, `metrics`).
- [x] **Infrastruktur**: `docker-compose.yml` (gateway, postgres, redis) dilengkapi dengan *healthcheck* dan dependensi layanan.
- [x] **Database & Migration**: Migrasi SQL melalui Sqitch untuk tabel `signing_keys`, `rate_limit_counters`, dan fungsi `upsert_rate_limit_counter`.
- [x] **Seed & Testing**: Skrip otomatis (`scripts/seed`) untuk menghasilkan RSA-2048 keypair dan contoh JWT.
- [x] **Middleware**: Implementasi verifikasi JWT (RS256) dengan resolusi `kid` yang menerapkan prinsip *fail-closed* saat PostgreSQL tidak tersedia.
- [x] **Observabilitas**: Endpoint `/metrics` (Prometheus, prefix `jwksgw_`) untuk memantau *hit/miss ratio*, *query count*, dan durasi request.
- [x] **Konfigurasi & Monitoring**: Konfigurasi via `.env.example` dan `/healthz` untuk verifikasi operasional sistem secara real-time.
- [x] **Dokumentasi**: *README.md* lengkap dengan perintah operasional (sqitch deploy, seed, run, dsb).

## Hasil Verifikasi End-to-End

Pengujian sistem divalidasi melalui *docker compose* dan *curl*:
* **Mode Hybrid**: *Valid Request* berhasil (200 OK dengan *cache hit*). *Unknown KID* terblokir oleh *negative cache* (401). *Flood concurrent* memicu respon 429 *rate_limited* setelah melampaui >20 req/s.
* **Mode Baseline**: *Valid Request* konsisten mendapatkan 200 OK dengan beban *query* basis data yang linier (1:1), tanpa limitasi trafik.
* **Mekanisme Fail-Closed**: PostgreSQL *down* memicu 503 *service_unavailable*. Redis *down* memicu *fallback* ke PostgreSQL untuk *KID* yang sudah ter-*cache*, dengan status `/healthz` melaporkan `redis:false`.

## Catatan Lingkungan

* **Manajemen Port PostgreSQL**: *Container* diekspos pada port 5433 untuk menghindari konflik port lokal. Gateway tetap mengakses internal database melalui port 5432.
* **Migrasi Basis Data**: Proyek Sqitch digunakan untuk manajemen siklus hidup basis data. Migrasi diverifikasi menggunakan file `deploy/*.sql` melalui psql pada mesin pengembangan yang belum memiliki driver `DBD::Pg`.
