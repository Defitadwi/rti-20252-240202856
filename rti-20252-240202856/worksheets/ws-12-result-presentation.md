# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

```
Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight
```

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|--------|-------------|
| Perbandingan antar-skenario | Bar chart (grouped/stacked) |
| Distribusi per-skenario | Box plot / violin plot |
| Tren temporal | Line chart |
| Korelasi dua variabel | Scatter plot |
| Proporsi (total = 100%) | Pie chart (hati-hati!) |

### Contoh Tabel Hasil yang Baik

| Model | Accuracy (%) | F1-Score (%) | Training Time (min) |
|-------|-------------|-------------|---------------------|
| BERT | 88.4 ± 1.2 | 87.1 ± 1.4 | 45.2 ± 3.1 |
| LSTM | 86.1 ± 1.8 | 84.5 ± 2.0 | 12.8 ± 1.2 |
| SVM | 82.3 ± 0.9 | 80.7 ± 1.1 | 0.3 ± 0.1 |

*N=10 per model. Mean ± std. Diurutkan berdasarkan Accuracy.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|------|----------|--------|
| Truncated axis | Y tidak dari 0 | Memperbesar perbedaan kecil |
| Inconsistent scale | Dua grafik skala beda | Perbandingan menyesatkan |
| Cherry-picked data | Hanya tampilkan yang "menang" | Selektif, tidak jujur |
| 3D effects | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| Missing error bar | Tidak ada variabilitas | Menyembunyikan ketidakpastian |

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan grafik | Dashboard monitoring | Mendukung argumen ilmiah |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value |
| Bias handling | Less critical | Wajib dihindari (peer-review) |

---

## Template A.12 — Result Presentation Plan

```
RESULT PRESENTATION PLAN

Research Question : Sejauh mana peningkatan jumlah epoch (10, 20, 30) memengaruhi akurasi klasifikasi penyakit padi menggunakan arsitektur InceptionV3 pada dataset terbatas?
Metrik Utama      : Accuracy Score (%) dan Training Loss

Tabel Hasil:
| Skenario | Accuracy Score (mean ± std) | Training Loss (mean ± std) | n |
|----------|-----------------------------|----------------------------|---|
| Epoch 30 | 96.8 ± 0.6%                 | 0.08 ± 0.02                | 5 |
| Epoch 20 | 91.2 ± 1.1%                 | 0.15 ± 0.04                | 5 |
| Epoch 10 | 75.4 ± 2.3%                 | 0.42 ± 0.09                | 5 |

Visualisasi yang Direncanakan:
| # | Jenis Grafik | Pesan Utama | Metrik |
|---|-------------|-------------|--------|
| 1 | Line Chart + Error Bar | Tren peningkatan akurasi dari epoch 10 ke 30 dan tingkat kestabilannya. | Mean Accuracy ± std |
| 2 | Grouped Bar Chart | Evaluasi trade-off penurunan nilai Loss seiring bertambahnya Epoch. | Mean Training Loss |

Bias Check:
  [X] Y-axis mulai dari 0 (atau dijustifikasi)
  [X] Error bar/CI ditampilkan
  [X] Semua data disertakan (tidak cherry-picked)
  [X] Tidak menggunakan 3D tanpa alasan
```

---

## Latihan 1 — Tabel Hasil

Buat tabel hasil eksperimen Anda (boleh dengan data simulasi jika belum punya data riil).

| Skenario | Metrik 1 (mean ± std) | Metrik 2 (mean ± std) | n |
|----------|----------------------|----------------------|---|
| Epoch 30 | 96.8 ± 0.6% | *45.2 ± 2.1 min| 5 |
| Epoch 20 | 91.2 ± 1.1% | 30.5 ± 1.4 min | 5 |
| Epoch 10 | 75.4 ± 2.3% | 15.8 ± 0.8 min | 5 |

**Checklist tabel:**
- [X] Self-contained (judul jelas, satuan ada, N tercantum)
- [X] Mean ± std (bukan single number)
- [X] Diurutkan berdasarkan metrik utama
- [X] Format konsisten di semua baris

---

## Latihan 2 — Rencana Visualisasi

Rencanakan 2-3 grafik untuk menyajikan data dari Latihan 1. Setiap grafik = satu pesan.

| # | Jenis Grafik | Pesan | Data yang Digunakan |
|---|-------------|-------|---------------------|
| 1 | Line Chart + Error Bar | Menunjukkan pola kenaikan akurasi yang signifikan seiring bertambahnya jumlah epoch komputasi. | Mean Accuracy ± std dari tiap skenario epoch |
| 2 | Box Plot | Menampilkan sebaran stabilitas dan konsistensi nilai akurasi pada setiap run eksperimen. | Seluruh data akurasi dari total 15 run |
| 3 | Scatter plot | Menggambarkan trade-off (hubungan timbal balik) antara peningkatan akurasi dan durasi waktu training yang dibutuhkan. | Mean Accuracy vs Mean Waktu Training |

---

## Latihan 3 — Bias Detection

Evaluasi visualisasi berikut untuk bias (skenario dari contoh):

**Skenario:** Metode A = 91.2%, Metode B = 90.8%. Bar chart dengan Y-axis mulai dari 90%.

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah Y-axis menyesatkan? | Ya. Pemotongan sumbu Y (truncated axis) membuat Metode A terlihat menghasilkan akurasi dua kali lipat lebih hebat dari Metode B, padahal selisih aslinya sangat tipis hanya 0.4%. |
| Apakah error bar ditampilkan? | Tidak. Ketiadaan nilai deviasi standar menyembunyikan potensi tumpang tindih (overlap) variabilitas data antar kedua metode.|
| Apakah semua kondisi ditampilkan? | Tidak. Hanya menampilkan visualisasi visual "pemenang" tanpa menyertakan variansi performa secara menyeluruh (cherry-picked).|
| Apa solusinya? | Sumbu Y wajib dimulai dari angka 0% agar proporsi visualisasi tinggi batang grafik mencerminkan nilai aslinya secara objektif, serta wajib menambahkan error bar.|

**Evaluasi grafik Anda sendiri dari Latihan 2:**
- [X] Semua bias check lulus
- [X] Ada yang perlu diperbaiki: — (Memastikan konfigurasi pustaka Matplotlib/Seaborn di Python dikunci pada ylim(0, 100) untuk akurasi).

---

## Refleksi

> Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja? Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?

> TTabel dan grafik saling melengkapi karena fungsinya berbeda: Tabel memberikan akurasi angka yang presisi secara detail, sedangkan grafik memberikan gambaran pola, tren, dan perbandingan secara cepat dan instan. Menggunakan salah satu saja akan membuat pembaca kehilangan fokus—baik kehilangan detail angka maupun kehilangan arah tren data.
Mengenai grafik yang menyesatkan, hal itu sering terjadi secara tidak sengaja akibat fitur auto-scale otomatis pada aplikasi (seperti Excel atau Python). Ketika sumbu Y tidak dimulai dari angka 0, perbedaan nilai yang sangat kecil (misal hanya selisih 0.5%) akan terlihat sangat besar dan dramatis secara visual. Hal ini menciptakan ilusi optik yang bisa mengecoh pembaca jika tidak divalidasi dengan hati-hati.