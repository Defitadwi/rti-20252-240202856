# 00-outline

Outline, peta sumber data, dan daftar klaim kunci untuk draf manuskrip ilmiah — **Tahap 5**.

---

## 1. Peta Sumber Data & Keselarasan Berkas

Dokumen ini berfungsi sebagai peta kendali untuk memastikan seluruh data statistik yang ditulis pada naskah bersumber dari data empiris yang valid:

* **Sumber Data Mentah:** `04-data/rice_leaf_diseases_cleaned` (Dataset citra penyakit daun padi yang terbagi ke dalam 3 folder kelas).
* **Sumber Output Statistik:** `06-output/grafik_akurasi_inception.png` dan `06-output/hasil_terminal_riset.png` (Hasil visualisasi pelatihan dan log terminal dari TensorFlow).
* **Target Publikasi:** Sinta 2 (Jurnal RESTI / Telematika) atau Scopus Q3-Q4.

---

## 2. Struktur Outline Manuskrip (Template IMRAD)

Naskah lengkap pada file `naskah-jurnal.md` wajib mengikuti struktur standar jurnal ilmiah berikut:

### Judul Penelitian
* *Klasifikasi Penyakit Daun Padi Menggunakan Algoritma Deep Learning dengan Arsitektur Inception V3 berbasis Transfer Learning*

### Abstrak (Abstract)
* Memuat ringkasan latar belakang otomasi diagnosis penyakit tanaman pangan, metode eksperimen ekstraksi fitur Convolutional Neural Network (CNN), hasil grafik akurasi konvergensi model, dan implikasi efisiensi komputasi transfer learning. Tersedia dalam versi Bahasa Indonesia dan English.

### 1. Pendahuluan
* **Latar Belakang:** Pentingnya produktivitas padi bagi ketahanan pangan, kendala identifikasi penyakit daun secara manual, dan urgensi otomatisasi computer vision di bidang pertanian.
* **Rumusan Masalah:** Bagaimana efektivitas pemanfaatan transfer learning arsitektur Inception V3 dalam mengenali pola penyakit lesi daun secara cepat dengan batasan dataset latih yang minimal?
* **Tujuan Penelitian:** Mengembangkan dan mengevaluasi performa model Deep Learning berbasis Inception V3 dalam mengklasifikasikan 3 jenis infeksi penyakit daun padi secara presisi.

### 2. Tinjauan Pustaka
* Kajian teori *Deep Learning*, *Convolutional Neural Network* (CNN), dan keunggulan struktur *Inception Module* dalam menangkap fitur multi-skala.
* Analisis perbandingan dengan riset terdahulu (Machine Learning tradisional) serta identifikasi celah penelitian (*research gap*) terkait optimalisasi parameter pelatihan jaringan saraf dalam kondisi dataset terbatas.

### 3. Metodologi Penelitian
* Desain eksperimen komputasi, prapemrosesan citra (*resizing* 224x224 piksel), konfigurasi arsitektur jaringan (*freezing base layer*, penambahan *GlobalAveragePooling2D*, *Dropout* 0.3, dan *Dense Layer* kustom), serta konfigurasi parameter pengujian (Optimizer Adam, Learning Rate 0.0001, Epoch 25, Validation Split 0.2).

### 4. Hasil dan Analisis
* Pemaparan statistik performa latih per epoch, kurva akurasi (*learning curve*), visualisasi nilai penurunan *loss*, serta analisis fenomena konvergensi cepat model pada lingkungan data terkontrol.

### 5. Kesimpulan dan Saran
* Kesimpulan utama mengenai keandalan arsitektur Inception V3 dalam mencapai akurasi mutlak 100% semenjak iterasi awal tanpa gejala overfitting.
* Saran pengembangan sistem pengujian lapangan menggunakan data riil berskala makro dengan variasi pencahayaan alami.

---

## 3. Daftar Klaim Kunci (Key Claims) yang Harus Konsisten

Untuk menghindari kesalahan penulisan atau ketidaksesuaian data antar bab, seluruh draf modul wajib mengacu pada angka-angka kunci di bawah ini:

1.  **Klaim Jumlah Sampel:** Total data gambar yang digunakan dalam pengujian awal adalah **9 citra** yang terbagi rata ke dalam **3 kelas penyakit** daun padi (N = 9).
2.  **Klaim Pembagian Data (Validation Ratio):** Alokasi pemisahan data uji menggunakan nilai rasio **0.2** (80% untuk data latih eksklusif dan 20% untuk validasi).
3.  **Klaim Iterasi Pelatihan (Epoch):** Durasi komputasi siklus pelatihan ditetapkan secara konsisten sebanyak **25 Epoch**.
4.  **Klaim Titik Konvergensi Sempurna:** Model sukses meraih tingkat akurasi mutlak **1.0000 (Akurasi 100%)** baik pada data latih maupun validasi semenjak **Epoch ke-3**.
5.  **Klaim Nilai Kerugian Akhir (Final Loss):** Nilai fungsi kerugian akhir pada Epoch ke-25 berhasil ditekan hingga menyentuh angka **0.4568 (Training Loss)** dan **0.4436 (Validation Loss)**.