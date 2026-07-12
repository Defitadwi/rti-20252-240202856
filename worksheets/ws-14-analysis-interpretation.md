# WS-14: Analysis, Interpretation & Failure Analysis

> **Bab 14 — Analisis Data, Interpretasi & Failure Analysis**

---

## Ringkasan Materi

### Data → Knowledge Model

```
Data → Analysis → Interpretation → Explanation → Knowledge
```

Tiga level yang berbeda:
- **Analysis** — "Apa yang terjadi?" (deskriptif + inferensial)
- **Interpretation** — "Apa artinya?" (konteks RQ + literatur)
- **Failure Analysis** — "Mengapa tidak berhasil?" (boundary conditions)

### Beyond p-value

**Statistical significance ≠ practical significance.** Selalu laporkan:
1. p-value (signifikansi statistik)
2. Effect size (besarnya efek)
3. Confidence interval (rentang ketidakpastian)

| Effect Size (Cohen's d) | Interpretasi |
|-------------------------|-------------|
| < 0.2 | Small |
| 0.2 – 0.8 | Medium |
| > 0.8 | Large |

### Pemilihan Uji Statistik

| Kondisi | Uji yang Tepat |
|---------|---------------|
| 2 grup, normal, paired | Paired t-test |
| 2 grup, non-normal | Wilcoxon signed-rank |
| > 2 grup, normal | One-way ANOVA + post-hoc |
| > 2 grup, non-normal | Kruskal-Wallis + post-hoc |
| 2 variabel kontinu | Pearson (normal) / Spearman (rank) |

### Failure Analysis as Contribution

Hipotesis yang ditolak adalah **temuan yang berharga**:

| Dataset | New (F1) | Baseline (F1) | p-value | Cohen's d |
|---------|---------|--------------|---------|-----------|
| DS-1 (small, clean) | 94.2±1.1 | 89.3±1.5 | <0.001 | **3.7** |
| DS-4 (medium, noisy) | 78.3±3.2 | 82.1±2.8 | 0.008 | **-1.3** |
| DS-5 (large, noisy) | 71.6±4.1 | 80.5±3.0 | <0.001 | **-2.5** |

**Insight:** Metode baru unggul di data bersih tapi gagal di data noisy → asumsi Gaussian dilanggar → **boundary condition** ditemukan → hybrid approach direkomendasikan.

**Partial failure + deep analysis = kontribusi lebih kaya daripada full success tanpa analisis.**

### Limitation Types

| Jenis | Contoh |
|-------|--------|
| Internal validity | Confounders yang tidak dikontrol |
| External validity | Generalisasi ke domain lain |
| Construct validity | Metrik mengukur apa yang dimaksud? |
| Statistical limitation | Sample size, asumsi distribusi |

### Jebakan Kognitif

1. "Signifikan statistik = penting secara praktis" → cek effect size
2. "Hipotesis tidak didukung → cari sudut baru" → p-hacking
3. "Kegagalan tidak perlu dilaporkan detail" → missed insight
4. "Limitasi cukup disebutkan, tidak perlu dianalisis" → kedalaman hilang

---

## Template A.14 — Analysis & Interpretation Report

```
ANALYSIS & INTERPRETATION

1. Statistik Deskriptif:
   | Skenario | Mean | Std | Median | Min | Max | n |
   |----------|------|-----|--------|-----|-----|---|
   | Epoch 75 (Intervensi)| 96.8%| 0.6%| 96.9%  | 95.8%| 97.5%| 5 |
   | Epoch 10 (Baseline)  | 75.4%| 2.3%| 75.1%  | 72.1%| 78.3%| 5 |

2. Uji Hipotesis:
   Uji yang digunakan  : Paired t-test (Uji t-berpasangan)
   Justifikasi          : Membandingkan rata-rata akurasi dari dua kelompok skenario (Baseline vs Intervensi) yang berasal dari run replikasi dataset terkontrol yang sama, serta data berdistribusi normal.
   Hasil: p = 0.0003, effect size (Cohen's d) = 3.92
   CI 95%               : [18.25%, 24.55%]

3. Keputusan:
   [X] H₀ ditolak → H₁ diterima (Penerapan InceptionV3 + Keras Tuner + Augmentasi Cahaya berpengaruh sangat signifikan secara statistik terhadap akurasi model).
   [ ] H₀ tidak ditolak
   
4. Interpretasi:
   Hubungan ke RQ       : Kombinasi intervensi berhasil menjawab Research Question (RQ) dengan mendongkrak akurasi validasi secara masif hingga menyentuh nilai puncak 97.5% (mendekati target hipotesis 98%).
   Practical significance: Nilai Cohen's d > 0.8 (3.92) membuktikan efek peningkatan performa sangat besar dan stabil untuk diterapkan pada sistem deteksi riil di lapangan.
   Perbandingan literatur: Hasil ini melampaui benchmark Christiawan dkk. (2023) yang menggunakan model CNN standar dengan batas batasan kapasitas komputasi perangkat keras.

5. Limitation:
   | Jenis | Ancaman | Dampak | Mitigasi |
   |-------|---------|--------|----------|
   | External Validity | Pengambilan sampel data dari satu sumber repositori online tunggal. | Kemampuan generalisasi model bisa menurun saat dihadapkan pada varietas padi lokal yang berbeda di Kabupaten Kebumen. | Menerapkan augmentasi distorsi kecerahan (-25% hingga -75%) untuk mensimulasikan fluktuasi cuaca riil di sawah. |
   | Statistical | Ukuran batch pelatihan dikunci konstan pada ukuran 32. | Potensi variasi lompatan konvergensi pada ukuran batch lain (misal 16 atau 64) belum tereksplorasi. | Menjadwalkan grid search tambahan khusus batch size pada riset lanjutan. |
   
6. Failure Analysis (jika H₀ tidak ditolak):
   Penyebab potensial  : Terjadinya pelonjakan akumulasi gradien error (gradient explosion) pada epoch awal ketika intensitas cahaya dikurangi secara ekstrem melebihi ambang batas -25%.
   Boundary condition   : Model InceptionV3 sangat kokoh menghadapi reduksi pencahayaan hingga batas -25%. Namun, performa mengalami degradasi jika citra diganggu dengan manipulasi reduksi cahaya di atas -50%.
   Insight              : Teknik augmentasi cahaya membutuhkan pembatasan ambang batas distorsi agar struktur geometri bintik penyakit daun tidak hilang tertutup kegelapan visual.
```

---

## Latihan 1 — Pemilihan Uji Statistik

Tentukan uji statistik yang tepat untuk eksperimen Anda.

| Pertanyaan | Jawaban |
|-----------|---------|
| Berapa grup yang dibandingkan? | 2 grup (Kondisi Baseline / Own Model vs Kondisi Intervensi / InceptionV3 + Keras Tuner). |
| Apakah data berpasangan (paired)? | Ya. Karena kedua model dilatih dan diuji menggunakan partisi porsi citra dari dataset 1.630 yang sama persis secara berpasangan per run.|
| Apakah distribusi normal? (uji normalitas) | Ya. Hasil uji Shapiro-Wilk menunjukkan nilai p > 0.05 yang berarti variabilitas sebaran data akurasi berdistribusi normal.|
| **Uji yang dipilih:** | Paired t-test|
| **Justifikasi:** | Digunakan karena penelitian membandingkan rata-rata dari dua kelompok sampel berpasangan dengan skala data numerik kontinu dan memenuhi asumsi sebaran normal.|

**Effect size yang akan dilaporkan:** [X] Cohen's d / [ ] Eta-squared / [ ] Lainnya: ____

---

## Latihan 2 — Interpretasi Hasil

Gunakan data berikut (atau data riil Anda) untuk berlatih interpretasi.

**Data:**
| Model | Accuracy (mean ± std) | n |
|-------|----------------------|---|
| A | 96.8 ± 0.6% | 5 |
| B | 75.4 ± 2.3% | 5 |

p = 0.0003, Cohen's d = 3.92, CI 95% = [18.25, 24.55]

| Aspek | Interpretasi |
|-------|-------------|
| Signifikansi statistik | p < 0.05 (0.0003) → Sangat signifikan secara statistik pada α = 0.05$. Perbedaan performa bukan karena faktor kebetulan acak. |
| Effect size | d = 3.92 →  Termasuk dalam kategori Large Effect (efek sangat besar karena jauh melampaui ambang batas standar 0.8). |
| Practical significance | Peningkatan akurasi rata-rata sebesar ~21.4% memberikan dampak praktis yang masif dalam meminimalkan risiko salah diagnosis klasifikasi penyakit tanaman padi oleh petani di lapangan.|
| Hubungan ke RQ | Menjawab Research Question secara tuntas bahwa intervensi optimasi otomatis dan augmentasi terarah sukses menaikkan performa klasifikasi piksel-ke-piksel daun padi secara kokoh.|
| Perbandingan literatur | Hasil akurasi intervensi (96.8% hingga puncaknya 97.5%) terbukti lebih unggul dibanding penelitian terdahulu yang menggunakan arsitektur MobileNetV1 (92%).|

---

## Latihan 3 — Failure Analysis

Latih kemampuan failure analysis: hipotesis TIDAK didukung. Apa yang bisa dipelajari?

**Skenario:** Metode baru Anda mendapat F1 = 83.2%, baseline = 84.7%. p = 0.12 (tidak signifikan).

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah ini "gagal"? | Bukan gagal total, melainkan penemuan batas batas kemampuan (boundary condition) model dalam menoleransi kegelapan gambar objek. |
| Kemungkinan penyebab? | Pengurangan tingkat kecerahan sebesar 75% melenyapkan informasi tekstur esensial, geometri warna bercak blas, dan lesi patogen pada daun padi, sehingga citra kehilangan fitur pembeda. |
| Boundary condition? | Model komputasi pintar InceptionV3 ini hanya adaptif dan efektif mempertahankan akurasi tinggi pada rentang gangguan fluktuasi cahaya sawah maksimal sebesar -Terdapat batas kritis trade-off antara augmentasi kegelapan dengan visibilitas fitur patogen. Rekomendasi sistem aplikasi web "Padisick" harus menyertakan fitur peringatan intensitas cahaya minimum saat petani mengambil foto daun. |
| Apakah layak dilaporkan? Mengapa? | Ya, sangat layak. Melaporkan negative results dan ambang batas kegagalan komputasi mencegah peneliti lain melakukan duplikasi kesalahan yang sama dan memberikan batasan operasional yang jujur bagi penggunaan aplikasi di dunia nyata. |

**Limitation terkait:**
| Jenis | Ancaman | Dampak |
|-------|---------|--------|
| *Contoh: Statistical* | Menggunakan metrik evaluasi tunggal (Accuracy) saat data mengalami drop di skenario ekstrem. | Distribusi salah klasifikasi per kelas penyakit (misal, apakah penyakit Blas salah dideteksi sebagai HDB) tidak terbaca dengan detail. |
| Internal Validity| Fluktuasi performa dipengaruhi oleh suhu perangkat komputasi keras laptop saat melakukan proses iterasi 75 epoch.| Memicu terjadinya thermal throttling yang bisa bias pada pencatatan training time.|

---

## Refleksi

> Apakah "failure" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?

> Hasil negatif (failure) bukanlah kegagalan, melainkan kontribusi ilmiah yang berharga. Hasil yang menolak hipotesis berfungsi memberikan informasi jujur mengenai batas kemampuan maksimum (boundary conditions) suatu metode saat dihadapkan pada skenario ekstrem.
Failure analysis mengubah cara pandang saya untuk tidak menyembunyikan hasil buruk. Dokumentasi yang jelas mengenai alasan penurunan akurasi (misalnya akibat manipulasi cahaya berlebih atau kendala memori laptop) sangat penting untuk mencegah peneliti lain melakukan kesalahan yang sama, sekaligus menjadi petunjuk arah bagi riset hibrida di masa mendatang.
