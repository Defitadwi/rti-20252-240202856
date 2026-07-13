# Rencana Penelitian: Mitigasi JWKS Endpoint Flooding dengan Redis-PostgreSQL Hybrid Caching

## 1. Ringkasan

| Item | Keterangan |
|---|---|
| Judul | Klasifikasi Penyakit Daun Padi Menggunakan Algoritma Deep Learning dengan Arsitektur Inception V3 berbasis Transfer Learning |
| Target Publikasi | Sinta 4/5 (Jurnal RESTI/Telematika) atau Scopus Q3-Q4 |
| Stack | Python (Keras/TensorFlow), Arsitektur InceptionV3, Keras Tuner  |
| Masalah |Deteksi penyakit padi secara manual memakan waktu lama, kurang akurat, dan ketergantungan petani pada pestisida tanpa diagnosis yang tepat  |
| Solusi |Sistem klasifikasi otomatis menggunakan metode Deep Learning (CNN) dengan arsitektur InceptionV3 dan augmentasi data untuk deteksi dini  |

## 2. Alur Kerja (Roadmap)

Setiap tahap memiliki file rencana detail tersendiri agar lebih rapi:

- [x] **Tahap 1** — [Perancangan Arsitektur & Skema Database] (Penelitian ini merancang sistem deteksi penyakit daun padi yang terdiri dari tiga proses utama: pre-processing, process, dan post-processing). — *Selesai*
- [x] **Tahap 2** — [Implementasi API Gateway (Go)] Tahapan ini tercermin pada implementasi arsitektur CNN sebagai "otak" sistem.) — *Selesai*
- [x] **Tahap 3** — [Skrip Pengujian k6 (Legitimate vs Attack Traffic)] Penulis melakukan berbagai uji coba training dengan membandingkan parameter seperti jumlah epoch, variasi partisi data, dan tingkat pengurangan brightness untuk augmentasi. — *Selesai*
- [x] **Tahap 4** — [Ekstraksi Data & Visualisasi] Visualisasi hasil training ditampilkan dalam bentuk grafik Loss dan Accuracy (seperti pada Own Model, Tuned, dan InceptionV3) untuk memantau performa model. — *Selesai*
- [x] **Tahap 5** — [Draf Paper Jurnal] Hasil akhir penelitian menunjukkan bahwa model CNN yang dilatih dengan 75 epoch, batch size 32, dan augmentasi brightness 25% mencapai akurasi tinggi.   — *Berikutnya*

---

## 3. Catatan

Dokumen ini adalah indeks utama. Detail teknis, skema, dan keputusan masing-masing tahap dicatat pada file `tahap-N-*.md` terkait dan diperbarui seiring progres pengerjaan.
