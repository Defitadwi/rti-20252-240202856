# 06-kesimpulan

## 5. Kesimpulan dan Saran

### 5.1 Kesimpulan
Berdasarkan seluruh rangkaian eksperimen terkontrol yang dijalankan menggunakan pendekatan desain *Within-Subject* terhadap 40 responden mahasiswa Universitas Putra Bangsa (UPB) Kebumen, serta melalui kalkulasi parameter data yang diperoleh secara mandiri, penelitian ini berhasil menarik beberapa kesimpulan mendalam sebagai berikut:

1. **Signifikansi Komparatif Efisiensi Kognitif:** Terdapat perbedaan efisiensi kognitif dan performa operasional yang sangat signifikan secara statistik antara model aplikasi finansial tunggal (*Stand-alone*) dan model aplikasi serbabisa (*Super App*). Melalui analisis inferensial *Paired Samples T-Test*, model *Stand-alone* terbukti secara nyata mampu memangkas durasi pengerjaan tugas (*Time-on-Task*) pengguna dalam mengakses fitur QRIS dari kondisi awal aplikasi mati hingga kamera aktif sepenuhnya. Perbedaan ini ditunjukkan oleh nilai *Mean Paired Differences* sebesar **1,18850 detik** lebih cepat dengan kekuatan uji yang sangat meyakinkan ($t\text{-hitung} = -10,104$, $p < 0,05$), yang menegaskan bahwa variasi durasi ini murni dipicu oleh struktur desain antarmuka, bukan faktor kebetulan.
2. **Optimalisasi Kecepatan Respons Motorik:**
   Penerapan model antarmuka *Stand-alone* terbukti unggul dalam meminimalkan hambatan mental pengguna, menghasilkan rata-rata waktu eksekusi yang sangat instan sebesar **4,8565 detik** (dengan tingkat sebaran data yang sangat homogen, $Std. Deviation = 0,65912$). Sebaliknya, model arsitektur *Super App* terbukti memperlambat respons motorik responden akibat adanya penundaan pemindaian visual (*scanning delay*), dengan rata-rata durasi interaksi yang signifikan lebih lama yaitu mencapai **6,0450 detik** ($Std. Deviation = 0,84165$).
3. **Implikasi Arsitektur Informasi terhadap Memori Kerja:**
   Secara teoritis, riset ini membuktikan bahwa pemusatan seluruh fungsi inti transaksi finansial dalam satu halaman utama yang bersih dan minimalis (seperti pada GoPay versi *Stand-alone*) jauh lebih efektif dalam menekan beban memori kerja pengguna (*working memory overload*). Sebaliknya, fragmentasi informasi visual dan penumpukan puluhan menu non-inti lintas sektor (seperti pada DANA versi *Super App*) memicu kepadatan elemen visual (*visual clutter*) pada layar. Hal ini memaksa sistem visual pengguna melakukan proses penyaringan informasi (*selective attention*) yang lebih berat, sehingga menghambat proses pemetaan mental (*mental mapping*) mahasiswa saat bertransaksi di lapangan.

---

### 5.2 Saran Penelitian Lanjutan
Guna menjembatani batasan ruang lingkup riset ini dan memberikan arah pengembangan bagi kajian ilmiah di masa mendatang, diajukan beberapa saran strategis sebagai berikut:

1. **Diversifikasi dan Inklusivitas Karakteristik Sampel:**
   Penelitian selanjutnya sangat disarankan untuk memperluas jangkauan populasi di luar kelompok mahasiswa Universitas Putra Bangsa yang secara umum sudah memiliki literasi digital tinggi (*tech-savvy*). Melibatkan kelompok masyarakat dengan rentang usia yang lebih tua (Generasi X atau *baby boomers*) serta masyarakat rural di wilayah Kabupaten Kebumen akan memberikan gambaran yang lebih objektif mengenai inklusivitas dan reliabilitas kedua model arsitektur informasi ini ketika dihadapkan pada tingkat kecakapan digital yang bervariasi.
2. **Ekspansi Kompleksitas Skenario Tugas (*Task Scenarios*):**
   Skenario pengujian dalam riset ini masih terbatas pada akses awal fitur pemindaian QRIS yang bersifat satu langkah langsung (*cold start*). Riset berikutnya dapat mengembangkan skenario tugas yang lebih kompleks, mendalam, dan bersifat *end-to-end*, seperti proses transfer antar-bank dengan verifikasi ganda, pengisian saldo (*top-up*) melalui *virtual account*, atau manajemen riwayat transaksi bulanan untuk memetakan tingkat efisiensi kognitif pada hierarki kedalaman menu yang berbeda.
3. **Integrasi Metrik Pengukuran Biometrik Objektif:**
   Untuk memperkuat analisis beban kognitif yang saat ini dievaluasi secara tidak langsung berbasis durasi waktu, penelitian lanjutan disarankan mengintegrasikan instrumen laboratorium yang lebih maju secara fisik. Pemanfaatan teknologi pelacakan mata (*eye tracker*) untuk menganalisis durasi fiksasi visual (*fixation duration*) atau pemindaian sensor elektroensefalografi (EEG) akan sangat berguna untuk menangkap data fluktuasi gelombang otak secara objektif, empiris, dan *real-time* tepat saat responden berinteraksi dengan komponen antarmuka aplikasi.