# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Run # | Skenario | Seed | Parameter | Status | Waktu | Output File |
|-------|----------|------|-----------|--------|-------|-------------|
| 1     | InceptionV3 Base | 42   | Epoch=75, BS=32, Aug=0.25 | Planned | 45 Mins | log_run_001.json |
| 2     | InceptionV3 Base | 123  | Epoch=75, BS=32, Aug=0.25 | Planned | 45 Mins | log_run_002.json |
| 3     | InceptionV3 Base | 999  | Epoch=75, BS=32, Aug=0.25 | Planned | 45 Mins | log_run_003.json |
| 4     | InceptionV3 Base | 777  | Epoch=75, BS=32, Aug=0.25 | Planned | 45 Mins | log_run_004.json |
| 5     | InceptionV3 Base | 2026 | Epoch=75, BS=32, Aug=0.25 | Planned | 45 Mins | log_run_005.json |

Jumlah runs per skenario :5 Run (Seed berbeda untuk validasi statistik berkelanjutan)
Total runs               : 5 Run

DATA LOG (per run):
  Run ID    : RICE-INCEPTIONV3-RUN001
  Timestamp : 2026-06-24T09:00:00+07:00
  Skenario  : Evaluasi Reproduksibilitas Arsitektur InceptionV3 pada Daun Padi
  Input     : 1.630 Citra Daun Padi (Resized 299x299, Augmentasi Kecerahan 25%)
  Output    : File model `rice_leaf_inceptionv3_run001.h5` & Metrik Akurasi Akhir
  Anomali   : Tidak ditemukan / Terjadi Thermal Throttling minor pada Epoch > 50
  Catatan   : Dijalankan langsung melalui Terminal Terintegrasi VS Code
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| 1 | InceptionV3 Daun Padi | 42| Epoch=75, Batch Size=32 | Planned|
| 2 | InceptionV3 Daun Padi | 123| Epoch=75, Batch Size=32 |Planned |
| 3 |InceptionV3 Daun Padi |999 |Epoch=75, Batch Size=32 |Planned |
| 4 |InceptionV3 Daun Padi |777| |Epoch=75, Batch Size=32 |Planned|
| 5 |InceptionV3 Daun Padi |2026 |Epoch=75, Batch Size=32 |Planned |

**Total skenario:** 1 Skenario Utama (InceptionV3 Base)
**Run per skenario:** 5 Run dengan Seed Berbeda
**Total run keseluruhan:** 5 Run

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh |
|-------|--------|
| Run ID | rice-leaf-cnn-001 |
| Timestamp | 2026-06-24T09:45:00 |
|Platform Environment |VS Code Terminal (Python 3.12.10, TensorFlow 2.15.0) |

**Konfigurasi:**
| Field | Contoh |
|-------|--------|
| Seed | *42* |
| Code version | commit f752a44 |
|Hyperparameters |commit f752a44 |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| Training Accuracy | *float* | 0.0 – 1.0 (Target: ~0.99) |
| Validation Accuracy| *float*  |0.0 – 1.0 (Target Jurnal: ~0.9734) |
| Validation Loss| *float*  |≥ 0.0 (Target Jurnal: ~0.7853) |
|Execution Time|  *float* |Jam/Menit (Estimasi per run: ± 45 menit via CPU)
**Format output:** [ ] CSV / [X] JSON / [ ] Database / [ ] Lainnya: ____

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Run gagal (crash) | Laptop Mengalami OOM saat memuat 1.630 gambar sekaligus. | Dokumentasikan eror, bersihkan session (backend.clear_session()), aktifkan fitur TensorFlow Memory Growth, atau gunakan tf.data.Dataset generator untuk memuat data secara bertahap.|
| Hasil ekstrem |Akurasi tiba-tiba jatuh ke 33% (seperti tebakan acak pada 3 kelas). |Selidiki apakah terjadi kebocoran data gradients (exploding gradients), dokumentasikan grafik loss, dan turunkan learning rate model melalui file konfigurasi. |
| Waktu eksekusi anomali |Satu epoch memakan waktu > 5 menit akibat laptop panas (thermal throttling). |Hentikan training sementara, lakukan pendinginan laptop Lenovo, dokumentasikan lonjakan suhu, dan jalankan ulang pengujian di kondisi suhu ruangan stabil. |
| Inkonsistensi dengan run lain |Run 3 menghasilkan akurasi yang terpaut jauh dibanding Run 1 dan Run 2. |Cari tahu apakah urutan pengacakan data generator tidak sengaja berubah, dokumentasikan distribusinya, dan jangan hapus data tersebut melainkan laporkan sebagai deviasi standar riset. |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Ya, dalam pengerjaan tugas-tugas pemrograman, basis data, atau analisis statistik sederhana sebelumnya, saya sering kali hanya melakukan satu kali eksekusi (single run) kode program. Jika program sudah berjalan tanpa error dan menghasilkan angka akurasi yang dirasa cukup bagus, saya langsung menyalin hasilnya ke dalam laporan.
Risikonya adalah bias eksperimen yang sangat tinggi. Angka keberhasilan dari single run bisa jadi hanyalah sebuah kebetulan (fluke) karena model kebetulan mendapatkan pembagian bobot awal acak yang menguntungkan. Riset seperti ini tidak memiliki fondasi ilmiah yang valid karena tingkat reproduksibilitasnya rendah—ketika program dijalankan ulang oleh orang lain, hasilnya bisa drop secara drastis.
**Yang akan dilakukan berbeda:**
> Mulai dari eksperimen klasifikasi daun padi ini, saya akan menerapkan protokol Multiple Run secara ketat (minimal 5 kali running dengan mengunci variasi random seed yang berbeda di setiap run).
Pendekatan multiple run ini mengubah total tingkat kepercayaan hasil riset karena saya tidak lagi menyajikan satu angka mutlak secara naif. Saya dapat menghitung nilai rata-rata (mean), standar deviasi, hingga melihat distribusi error-nya. Hal ini membuktikan secara ilmiah bahwa akurasi tinggi yang dihasilkan oleh arsitektur InceptionV3 (~97.34%) murni karena keandalan konfigurasi sistem yang saya bangun, bukan karena faktor keberuntungan komputasi semata.