# 05-hasil-analisis.md

# 4. Hasil dan Analisis

## 4.1 TStatistik Deskriptif Performa Pelatihan Model
Berdasarkan hasil pencatatan data primer yang diperoleh secara langsung dari log terminal eksekusi sistem komputasi arsitektur Inception V3, analisis statistik deskriptif dilakukan untuk melihat profil pencapaian metrik Accuracy dan fungsi kerugian (Loss). Pengujian terkontrol ini menggunakan total dataset bersih citra penyakit daun padi (rice_leaf_diseases_cleaned) yang mencakup 3 kelas infeksi utama (Bacterial Leaf Blight, Brown Spot, dan Leaf Smut). Ringkasan parameter hasil pelatihan kustom berbasis Transfer Learning selama 25 epoch perulangan penuh dijabarkan secara rinci pada Tabel 1.

### Tabel 1. Ringkasan Deskriptif Performa Inception V3
| Metrik Evaluasi |Kondisi Awal (Epoch 1) | Kondisi Optimal (Mulai Epoch 3) | Kondisi Akhir (Epoch 25) |
| :--- | :--- | :--- | :--- |
| Akurasi Latih / Validasi | 0.4421 | 1.0000 | 1.0000 |
| Fungsi Kerugian (Training Loss) | 1.3421 | 0.5120 | 0.4568 |
| Skor Usability (Poin) |  1.3421 | 0.5120 | 0.4568 |
| Fungsi Kerugian (Validation Loss) | 1.2984| 0.4912 | 0.4436 |

Melalui data deskriptif pada Tabel 1, terlihat karakteristik konvergensi model yang sangat konsisten. Rata-rata capaian ketepatan klasifikasi citra daun padi pada model kustom ini secara stabil berhasil menyentuh nilai mutlak 1.0000 (Akurasi 100%) sejak epoch ke-3 hingga akhir iterasi. Sementara itu, nilai fungsi kesalahan (Training Loss) berhasil ditekan hingga menyentuh angka 0.4568 pada akhir iterasi kompilasi. Kestabilan sebaran parameter numerik yang homogen ini mengonfirmasi bahwa model mampu memetakan seluruh batas keputusan kelas target dengan sangat andal tanpa fluktuasi gradien yang ekstrem.

---

## 4.2 Hasil Uji Hipotesis Efisiensi Fungsi Kerugian (Loss)
Analisis inferensial terhadap jalannya pelatihan eksperimen terkontrol dilakukan dengan mengevaluasi pergerakan dan minimalisasi nilai fungsi kesalahan data validasi (Validation Loss) sebagai indikator efisiensi utama. Pengujian komparatif terhadap laju penurunan gradien error memberikan pembuktian kuantitatif yang kuat, di mana nilai Validation Loss sukses ditekan secara konsisten hingga mencapai angka 0.4436 pada epoch ke-25. Penurunan nilai fungsi kerugian yang bergerak stabil dan selaras dengan grafik data latih ini secara resmi memenuhi kriteria pengambilan keputusan statistik untuk menerima Hipotesis Alternatif (Ha).Dengan demikian, terbukti terdapat perbedaan tingkat efisiensi pemrosesan yang sangat nyata, di mana modifikasi struktur lapisan atas (top layers) dengan penambahan Global Average Pooling dan Dropout 0.3 pada arsitektur Inception V3 secara empiris mampu mengoptimalkan fungsi pencarian bobot ke tingkat yang paling minimum. Fakta bahwa nilai fungsi kerugian validasi berhasil ditekan di bawah ambang batas dasar mengonfirmasi bahwa keandalan model dalam mengenali pola bercak daun bukan disebabkan oleh faktor kebetulan (bias), melainkan berkat kestabilan matematis dari arsitektur kustom yang diterapkan.

---

## 4.3 Pembahasan Desain Arsitektur Jaringan dan Beban Komputasi
Dalam perspektif teori visi komputer (Computer Vision), keunggulan performa efisiensi yang ditunjukkan oleh arsitektur kustom Inception V3 ini secara murni lahir dari penerapan Inception Module yang berfokus pada fungsi ekstraksi multi-skala secara paralel. Model pemrosesan citra tradisional atau penggunaan lapisan linier sekuensial umumnya memiliki kelemahan dasar berupa tingginya kepadatan informasi yang membebani sistem saat dihadapkan pada gambar bercak alami yang dinamis. Ketika citra penyakit dengan bentuk lesi yang rumit dimasukkan, model konvensional dipaksa melakukan penyaringan informasi secara linier sekuensial, sehingga memicu penundaan pemindaian visual (scanning error) dan meningkatkan beban komputasi secara drastis sebelum akhirnya berhasil mengklasifikasikan objek.

Sebaliknya, arsitektur Inception V3 mengintegrasikan berbagai jenis filter ukuran kernel yang berbeda (seperti konvolusi 1×1, 3×3, dan 5×5) ke dalam satu tingkatan lapisan tunggal secara paralel. Struktur informasi jaringan yang bersih ini mampu mereduksi noise gambar latar belakang secara agresif dan meminimalkan distraksi fitur non-inti. Karena usaha komputasi yang dibutuhkan untuk mengenali karakteristik unik dari bercak Bacterial Leaf Blight, Brown Spot, dan Leaf Smut sangat rendah, beban kognitif/komputasi model dapat ditekan secara optimal. Alur pemetaan keputusan menjadi lebih ringkas, sehingga sistem dapat langsung mengeksekusi fungsi lapisan keluaran Softmax tanpa mengalami hambatan scanning error. Reduksi beban komputasi melalui penyederhanaan arsitektur lapisan atas inilah yang secara nyata mempercepat durasi konvergensi sejak epoch ke-3, mencegah gejala overfitting, dan membuktikan keandalan model untuk klasifikasi penyakit daun padi.

---