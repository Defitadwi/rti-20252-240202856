# Proposal Penelitian: Klasifikasi Penyakit Daun Padi Menggunakan Algoritma Deep Learning dengan Arsitektur Inception V3 berbasis Transfer Learning

## 1. Latar Belakang

Sektor pertanian, khususnya komoditas padi, memegang peranan krusial dalam menjaga ketahanan pangan nasional. Namun, produktivitas tanaman padi seringkali terancam oleh penyebaran berbagai jenis penyakit tanaman, seperti Blas (Rice Blast), Hawar Daun Bakteri (HDB), dan Bercak Coklat (Brownspot). Keterlambatan atau kesalahan dalam mengidentifikasi gejala penyakit ini pada daun padi dapat mengakibatkan kegagalan panen skala besar dan penurunan kualitas produksi.

Metode identifikasi konvensional yang mengandalkan pengamatan visual oleh petani atau tenaga ahli memiliki keterbatasan dalam hal waktu, subjektivitas, dan ketersediaan tenaga di lapangan. Sebagai solusi, pemanfaatan teknologi informasi di bidang kecerdasan buatan, khususnya Deep Learning dengan arsitektur Convolutional Neural Network (CNN), menawarkan alternatif deteksi dini yang cepat, objektif, dan otomatis.

Penelitian ini menerapkan arsitektur Inception V3, sebuah model CNN tingkat lanjut yang dikembangkan oleh Google. Inception V3 memiliki keunggulan berupa penggunaan Inception modules yang menerapkan operasi konvolusi secara paralel dengan ukuran filter bervariasi ( 1 x 1,3 x 3, dan 5 x 5 ) di dalam layer yang sama. Karakteristik ini memungkinkan model untuk menangani ekstraksi fitur citra penyakit daun padi secara multi-skala, baik tekstur bercak halus maupun pola lesi daun yang lebih luas, tanpa membebani biaya komputasi secara ekstrem.

Meskipun model deep learning dikenal andal, performa klasifikasinya sangat dipengaruhi oleh konfigurasi parameter pelatihan, seperti jumlah iterasi pelatihan (epoch) dan representasi distribusi sebaran dataset. Oleh karena itu, pengujian performa secara kuantitatif melalui visualisasi kurva akurasi dan metrik evaluasi yang rigor sangat diperlukan untuk memastikan model terhindar dari kondisi underfitting maupun overfitting sebelum diimplementasikan pada sistem produksi nyata.

## 2. Rumusan Masalah

Berdasarkan latar belakang di atas, rumusan masalah dalam penelitian ini adalah:

1. Bagaimana performa akurasi model Inception V3 dalam mengklasifikasikan tiga jenis penyakit daun padi (Blas, Hawar Daun Bakteri, dan Bercak Coklat)?
2. Bagaimana pengaruh peningkatan jumlah epoch (dari 1 hingga 75) terhadap stabilitas nilai Train Accuracy dan Validation Accuracy?
3. Apakah model Inception V3 mampu mencapai konvergensi yang optimal tanpa mengalami gejala overfitting pada distribusi dataset yang ditentukan?
## 3. Tujuan Penelitian
Berdasarkan latar belakang di atas, rumusan masalah dalam penelitian ini adalah:

1. Bagaimana performa akurasi model Inception V3 dalam mengklasifikasikan tiga jenis penyakit daun padi (Blas, Hawar Daun Bakteri, dan Bercak Coklat)?
2. Bagaimana pengaruh peningkatan jumlah epoch (dari 1 hingga 75) terhadap stabilitas nilai Train Accuracy dan Validation Accuracy?
3. Apakah model Inception V3 mampu mencapai konvergensi yang optimal tanpa mengalami gejala overfitting pada distribusi dataset yang ditentukan?

## 4. urgensi

Deteksi dini penyakit tanaman padi secara akurat memiliki dampak langsung pada efisiensi penanganan pertanian dan stabilitas hasil panen. Dengan adanya data evaluasi empiris mengenai performa model Inception V3 ini, pengembang sistem atau peneliti di bidang pertanian digital (smart agriculture) dapat memperoleh acuan parameter yang teruji. Implementasi model yang optimal dapat meminimalkan kesalahan diagnosis penyakit, mengurangi penggunaan pestisida yang berlebihan akibat salah prediksi, serta mempercepat proses pengambilan keputusan klinis tanaman di tingkat desa.

## 5. Metodologi (Ringkasan)

### 5.1. Skenario Eksperimen dan Sebaran Data
Tabel 1. Sebaran Dataset Penyakit Daun Padi
Penelitian ini membagi dataset ke dalam tiga kelas penyakit utama ditambah dengan perhitungan total citra seperti yang tertera pada Tabel 1.

| Kelas Penyakit | Data Training (75%) | Data Testing (25%) | Total Citra |
|----------------|---------------------|--------------------|-------------|
| `Blas (Rice Blast)` | 472 | 158 | 630 |
| `Hawar Daun Bakteri (HDB)` | 375 | 125 | 500 |
| `Bercak Coklat (Brownspot)` | 375 | 125 | 500 |
| Total Keseluruhan | 1.222 | 408 | 1.630 |

### 5.2. Konfigurasi Pengujian dan Evaluasi Kurva

- **Tool**: Inception V3 Arsitektur
- **Replikasi**: 75 Epoch (Interval evaluasi sumbu grafik: 1, 15, 30, 45, 60, 75)
- **Metrik**: Hold-out validation dengan rasio 75:25
- **Lingkungan**: Tren performa kestabilan model dipetakan melalui kurva akurasi pada Figure 1 berikut.
  <img width="752" height="452" alt="image" src="https://github.com/user-attachments/assets/a30bf6d1-8df5-4f76-a787-239c014c7e17" />
**Figure 1.** Grafik Kurva Akurasi Pelatihan (Train Accuracy) dan Akurasi Validasi (Validation Accuracy) Model Inception V3.

### 5.3. Metrik Evaluasi
Pengukuran kinerja akhir model deep learning dalam mengklasifikasikan citra penyakit tanaman padi pada penelitian ini dievaluasi menggunakan metrik akurasi (accuracy). Persamaan untuk menghitung nilai akurasi tersebut ditunjukkan pada Persamaan (1).
                 <img width="844" height="109" alt="image" src="https://github.com/user-attachments/assets/cc1a0591-5444-4848-8c53-908d921a2475" />  
     
Keterangan dari simbol atau variabel yang digunakan pada Persamaan (1) adalah sebagai berikut: TP (True Positive) merupakan jumlah citra penyakit daun padi yang berhasil diprediksi dengan benar oleh model sesuai kelas aslinya; TN (True Negative) adalah jumlah citra dari kelas lain/sehat yang berhasil diprediksi secara benar sebagai bukan bagian dari kelas penyakit tersebut; FP (False Positive) menandakan jumlah citra sehat atau kelas lain yang salah diprediksi oleh model sebagai kelas penyakit tertentu; sedangkan FN (False Negative) yaitu jumlah citra penyakit daun padi yang gagal dikenali dan malah salah diprediksi sebagai kelas penyakit lain atau kelas sehat.

## 6. Daftar Pustaka (Preliminary)

[1] T. Purwanto. "Analisa Perbandingan Kinerja Arsitektur CNN untuk Klasifikasi Citra Penyakit Tanaman." Scientia Sacra, vol. 3, no. 4, pp. 75-82, Des. 2023.

[2] M. Siahaan, R. Wijaya. "Performance Comparison of Image Classification on Agricultural Sector Using Deep Learning." JITE, vol. 7, no. 2, pp. 580-589, Jan. 2024.

[3] W. Hadinata, L. Stianingsih. "Analisis Perbandingan Performa Eksperimen Model Transfer Learning Pada Deteksi Penyakit Daun Padi." JITET, vol. 12, no. 1, pp. 610-619, Jan. 2024. https://doi.org/10.23960/jitet.v12i1.3910

[4] H. Santoso, dkk. "Implementasi Ekstraksi Fitur Multi-Skala Menggunakan Model Inception untuk Identifikasi Gejala Blas pada Padi." Jurnal Teknologi Pertanian, vol. 15, no. 3, pp. 201-210, Nov. 2024.

[5]  A. S. Azzahidi, B. Wijayanto, A. Darmawan. "Performance Evaluation of Deep Learning Frameworks for Plant Disease Detection: A Comparative Study of VGG16, ResNet50, MobileNetV2, and Inception V3." JUTIF, vol. 6, no. 4, pp. 4922, 2025. https://doi.org/10.52436/1.jutif.2025.6.4.4922
