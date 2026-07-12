# WS-13: Data Preprocessing

> **Bab 13 — Preprocessing & Persiapan Data untuk Analisis**

---

## Ringkasan Materi

### Data Refinement Pipeline

```
Raw Data → Cleaning → Transformation → Normalization → Processed Data → Analysis Ready
```

Setiap tahap memiliki tujuan berbeda. **Preprocessing bukan langkah teknis biasa** — setiap keputusan preprocessing adalah keputusan riset yang bisa mengubah kesimpulan.

### Empat Prinsip Preprocessing

| Prinsip | Deskripsi |
|---------|----------|
| **Consistency** | Metode sama untuk data yang sama |
| **Transparency** | Setiap langkah terdokumentasi |
| **Reproducibility** | Orang lain bisa mengulang dengan hasil sama |
| **Minimal Distortion** | Ubah sesedikit mungkin; jika normalisasi tidak perlu, jangan lakukan |

### Cleaning Triad

| Masalah | Strategi | Risiko |
|---------|---------|--------|
| **Missing values** | | |
| — Listwise deletion | Missing < 5%, random | Data loss |
| — Mean/median imputation | Sedikit missing, dist. normal | Mengurangi variabilitas |
| — Model-based imputation | Banyak missing, pola sistematis | Introduces dependency |
| — Flag & separate | Missing karena alasan substantif | Kompleksitas analisis |
| **Duplikat** | Identifikasi → verifikasi → hapus | False positive (data mirip ≠ duplikat) |
| **Error format** | Standardisasi tipe, encoding | Kehilangan informasi saat konversi |

### Normalisasi — Kapan & Metode Mana

| Metode | Formula | Output | Sensitif Outlier? |
|--------|---------|--------|-------------------|
| Min-max | (x-min)/(max-min) | [0, 1] | Ya |
| Z-score | (x-mean)/std | Unbounded | Lebih robust |
| Robust scaling | (x-median)/IQR | Unbounded | Paling robust |

**Kunci:** Parameter normalisasi harus dihitung dari **training set saja** — bukan seluruh data. Pelanggaran = **data leakage**.

### Data Leakage Prevention

Data leakage terjadi ketika informasi dari test set "bocor" ke preprocessing:
- Normalisasi parameter dari seluruh dataset ← **SALAH**
- Cross-validation dilakukan sebelum split ← **SALAH**
- Feature selection menggunakan label test set ← **SALAH**

### Jebakan Kognitif

1. "Preprocessing cuma teknis — tidak perlu detail" → bisa ubah kesimpulan
2. "Lebih banyak preprocessing = lebih bersih = lebih baik" → over-processing distorsi data
3. "Normalisasi selalu diperlukan" → belum tentu, tergantung metode analisis
4. "Imputation sama untuk semua situasi" → strategi harus sesuai konteks

---

## Template A.13 — Preprocessing Documentation Log

```
PREPROCESSING LOG

Dataset           : Dataset Sekunder Citra Penyakit Daun Padi (Blas, HDB, Brownspot)
Jumlah data awal  : 1.638 data citra mentah 

Cleaning:
| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing | 0 Kasus     | -          | Semua file citra terdokumentasi lengkap dalam folder kelas masing-masing. |
| Duplikat| 0 Kasus     | -          | Dataset sekunder dari repositori online sudah melalui kurasi awal. |
| Error   | 8 Kasus     | Pembuangan file korup / bukan gambar | File berukuran 0 KB atau rusak secara struktur dieliminasi agar tidak memicu error batching. |

Transformation:
| Transformasi | Variabel | Detail | Alasan |
|-------------|----------|--------|--------|
| Resizing    | Piksel Citra | Mengubah resolusi gambar secara seragam menjadi 299 x 299 piksel | Menyesuaikan dengan standar dimensi matriks input wajib arsitektur InceptionV3. |
| Color Conv  | Channel Warna | Konversi citra ke ruang warna RGB standar | Menghilangkan variasi gambar grayscale atau alpha channel yang dapat merusak shape tensor. |

Normalization:
  Metode    : Min-Max Rescaling (Skala 1./255)
  Alasan    : Mengubah rentang nilai kecerahan piksel [0, 255] menjadi range matriks [0.0, 1.0] agar proses gradient descent saat training lebih cepat konvergen.
  Parameter : (dihitung dari: training set)

Leakage Check:
  [X] Parameter normalisasi dari training set saja
  [X] Tidak ada informasi test set dalam preprocessing
  [X] Cross-validation dilakukan setelah split

Jumlah data akhir : 1.630 citra (Blas: 630, HDB: 500, Brownspot: 500)
Script tersedia   : [X] Ya → path: scripts/preprocess.py | [ ] Belum
```

---

## Latihan 1 — Cleaning Plan

Periksa dataset Anda (atau dataset contoh) dan dokumentasikan masalah yang ditemukan.

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing di kolom "label" | 12 dari 500 (2.4%) | Listwise deletion | < 5%, distribusi random (MCAR) |
| File citra duplikat (Double upload)| 8 dari 1.638| Eksklusi langsung dari folder dataset| < 5%, file rusak berukuran 0 KB akan menghentikan proses batch loading pada TensorFlow.|
| Format gambar rusak (Corrupt file)| 0 kasus| -| Dataset bersumber dari repositori publik yang sudah terkurasi.|

**Jumlah data sebelum cleaning:** 1638
**Jumlah data setelah cleaning:** 1630
**Persentase data yang hilang/berubah:** 0.49%

---

## Latihan 2 — Normalisasi Decision

Tentukan apakah data Anda perlu normalisasi, dan jika ya, metode apa yang tepat.

| Variabel | Range Asli | Distribusi | Outlier? | Metode Normalisasi | Alasan |
|----------|-----------|-----------|----------|-------------------|--------|
| Contoh: response_time | 0.1 – 45.2s | Right-skewed | Ya (45.2) | Robust scaling | Ada outlier, perlu robust |
| Nilai Piksel Citra| 0 – 255| Variatif| Nilai Piksel Citra|Min-Max Rescaling (1./255)| Mengubah nilai nilai intensitas piksel menjadi skala [0,1] untuk mempercepat komputasi jaringan saraf tiruan (CNN).|

**Apakah normalisasi diperlukan?** [X] Ya / [ ] Tidak
**Justifikasi:**
> Normalisasi nilai piksel sangat krusial dalam pemrosesan citra berbasis Deep Learning. Jika dibiarkan dalam skala asli (0-255), nilai aktivasi di dalam node-node paralel milik InceptionV3 akan terlalu besar dan menyebabkan ketidakstabilan matematis (exploding gradients) serta melambatkan waktu konvergensi model.
**Leakage check:**
- [X] Parameter dihitung dari training set saja
- [X] Normalisasi diterapkan setelah train-test split

---

## Latihan 3 — Preprocessing Report

Buat ringkasan preprocessing lengkap — dokumentasi yang cukup bagi orang lain untuk mereplikasi.

```
PREPROCESSING SUMMARY

1. Dataset: Dataset Sekunder Citra Penyakit Daun Padi
2. Data awal: 1.638 records, 3 features (Height, Width, Channels)
3. Cleaning:
   - Missing values: 0 kasus
   - Duplikat: 0 kasus
   - Error: 8 kasus, tindakan: Diabaikan dan dibuang dari folder input
4. Transformation: Image Resizing ke dimensi konstan 299x299 piksel dengan format matriks warna RGB
5. Normalisasi: Min-Max Rescaling (1./255), parameter diekstraksi murni dari training set saja
6. Data akhir: 1.630 records (images) -> Terbagi atas 1.222 data training (75%) dan 408 data testing (25%)
7. Leakage check: [X] Lulus / [ ] Ada masalah
```

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?

> Ya, di awal belajar saya sering menerapkan normalisasi secara otomatis hanya karena mengikuti template tutorial. Padahal, jika skala data bawaannya sudah seragam atau algoritma yang digunakan tidak sensitif terhadap jarak matriks (seperti Decision Tree), normalisasi sebenarnya tidak diperlukan dan hanya membuang waktu komputasi.
Risiko dari over-preprocessing adalah terjadinya distorsi data. Jika data asli dimanipulasi atau dibersihkan secara berlebihan, variabilitas alami yang penting dari citra akan hilang. Akibatnya, model AI akan belajar dari data yang "terlalu steril" dan akan mengalami penurunan akurasi (drop) yang tajam saat diuji pada kondisi dunia nyata yang penuh dengan variasi acak (noise).
> ___________________________________________________
