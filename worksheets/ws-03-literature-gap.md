# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database**: IEEE Xplore, ACM DL, Scopus, Google Scholar
2. **Boolean query** yang terdokumentasi eksplisit
3. **Snowballing**: backward (telusuri referensi) + forward (cari yang mengutip)
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : Klasifikasi Penyakit Daun Padi menggunakan Deep Learning.
Database   : Google Scholar.
Query      : Rice leaf disease classification CNN InceptionV3 accuracy  ``24
Tahun      : ____________________
Hasil awal : ____ paper → Screening → ____ paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
| Siti Aminah dkk.      | 2022      | CNN (InceptionV3)       | 1.500 citra (Blas, Brownspot, HDB)     |Akurasi 93,3% pada 30 epoch.        |Kapasitas perangkat membatasi jumlah dataset. |
| Prajapati, dkk. | 2021 | SVM & K-Means | Citra lab terkontrol | Akurasi 88% | Kurang akurat pada citra dengan background kompleks. |
| Kundu, dkk.| 2021 | VGG16 | Dataset Kaggle | Akurasi 91% | Model terlalu berat (large parameters) untuk mobile. |
| Chen, dkk. | 2020 | MobileNet-V2 | Citra lapangan | Akurasi 90% | Akurasi menurun pada pencahayaan rendah.|

Pola yang ditemukan:
  Metode dominan     : Convolutional Neural Networks (CNN) dengan berbagai arsitektur (Inception, V3, VGG, ResNet).
  Dataset umum       : Citra penyakit Blas (Blast), Bercak Coklat (Brownspot), dan Hawar Daun Bakteri (HDB).
  Limitasi berulang  : Akurasi tinggi hanya tercapai pada lingkungan terkontrol atau dataset yang sudah bersih; kinerja menurun pada dataset terbatas atau hardware spesifik.
GAP IDENTIFICATION

Gap 1: [Jenis: performance / method]
  Deskripsi    : Kurangnya pemahaman tentang titik jenuh (saturation point) optimasi jumlah epoch pada arsitektur InceptionV3 ketika menghadapi dataset kecil
  Bukti        : Siti Aminah (2022) menunjukkan kenaikan drastis dari 10 ke 30 epoch, namun belum menguji apakah penambahan lebih lanjut akan mengakibatkan overfitting.
  Signifikansi : Mengetahui epoch optimal mencegah pemborosan daya komputasi pada perangkat terbatas. 
Gap 2: [Jenis: Data / Context]
  Deskripsi    : Kesenjangan antara akurasi model di lingkungan pengembangan dengan performa pada perangkat mobile dengan spesifikasi rendah (low-end device).
  Bukti        : Adanya pengakuan batasan perangkat keras pada penelitian sebelumnya yang menghambat penggunaan dataset dalam skala besar.
  Signifikansi : Menjamin solusi TI dapat benar-benar digunakan oleh petani di daerah terpencil dengan alat seadanya.
Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
| Siti Aminah (2022)          | Sangat Tinggi; menggunakan metode dan objek yang identik. | Mewakili tren penggunaan CNN InceptionV3 untuk penyakit padi di Indonesia. | Jurnal Nasional Komputasi dan Teknologi Informasi. |
| Kundu, dkk. (2021) | Tinggi; sebagai pembanding performa antar arsitektur CNN (VGG vs Inception). | Mewakili standar performa global pada dataset publik. | Journal of Computers and Electronics in Agriculture. |

```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan Google Scholar atau database lain.

**Topik riset:** Klasifikasi Penyakit Daun Padi Menggunakan Deep Learning (CNN).
**Query pencarian:** Rice leaf disease classification CNN InceptionV3 accuracy validation
**Database:** Google Scholar

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | Siti Aminah dkk. | 2022 | CNN((InceptionV3)) | 1.500 citra (Blas, Brownspot, HDB) | Acc 93,3% pada 30 epoch | Terkendala kapasitas perangkat (dataset dibatasi). |
| 2 |Prajapati et al. | 2021 | SVM & K-Means | Citra lab terkontrol | Acc 88% | Kurang stabil pada citra dengan latar belakang kompleks. |
| 3 | Kundu et al. | 2021 | VGG16 & Transfer Learning | Dataset Kaggle | Acc 91% | Arsitektur model terlalu berat untuk deployment mobile. |
| 4 | Chen et al. | 2020 | MobileNet-V2 | Citra lapangan asli | Acc 90% | Akurasi menurun drastis pada kondisi cahaya rendah. |
| 5 | Ahmed et al. | 2023 | ResNet-50 | 3.000 citra multi-varietas | Acc 94% | Memerlukan waktu komputasi (training) yang sangat lama.|

**Pola yang terlihat — Metode dominan:** Penggunaan arsitektur Convolutional Neural Networks (CNN) dengan pendekatan Transfer Learning (menggunakan model yang sudah terlatih seperti Inception atau VGG) lebih dominan dibandingkan metode tradisional seperti SVM atau K-Means karena kemampuannya dalam mengekstraksi fitur visual yang kompleks secara otomatis.
**Limitasi yang berulang:** Kebutuhan akan sumber daya komputasi yang tinggi dan ketergantungan pada kualitas serta jumlah dataset. Sebagian besar riset masih terkendala pada performa model ketika dipindahkan dari lingkungan server/laboratorium ke perangkat lapangan (laptop standar atau smartphone) yang memiliki spesifikasi terbatas.
---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [X] Ya / [ ] Tidak | Akurasi model InceptionV3 menunjukkan fluktuasi signifikan (74% ke 93%) pada rentang epoch awal, namun belum diketahui titik saturasi efisiensinya. |
| Method Gap | [X] Ya / [ ] Tidak | Sebagian besar penelitian menggunakan parameter standar; belum ada studi mendalam tentang optimasi hyperparameter (seperti epoch) khusus untuk kondisi dataset terbatas. |
| Data Gap | [X] Ya / [ ] Tidak | Adanya keterbatasan jumlah dataset (hanya 500 citra per kelas) karena hambatan kapasitas memori perangkat keras peneliti. |
| Context Gap | [X] Ya / [ ] Tidak | Model yang dilatih pada lingkungan terkontrol sering kali tidak diuji pada variasi low-end device yang sebenarnya dimiliki oleh petani lokal. |

**Gap utama yang dipilih:** Method Gap (Optimasi Parameter pada Dataset Terbatas)
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Gap ini penting karena dalam implementasi nyata di bidang pertanian, peneliti sering kali tidak memiliki akses ke superkomputer atau dataset raksasa berjumlah puluhan ribu citra. Jika kita tidak menemukan jumlah epoch dan konfigurasi parameter yang paling efisien untuk dataset kecil, maka model Deep Learning akan menjadi sangat berat, memakan waktu lama untuk dilatih, atau justru mengalami overfitting. Dengan menutup gap ini, kita bisa menciptakan solusi TI yang tetap akurat namun ringan dan adaptif terhadap keterbatasan infrastruktur yang ada di lapangan.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | CNN (InceptionV3) | Menggunakan arsitektur dan objek (penyakit padi) yang sama persis. | Menjadi standar acuan utama dalam klasifikasi citra medis dan botani karena efisiensi fiturnya. | Ya, salah satu arsitektur terbaik untuk transfer learning. | Siti Aminah dkk., 2022 |
| 2 | CNN (VGG16) | Sama-sama berbasis Convolutional Neural Network namun dengan kedalaman layer berbeda. | Mewakili arsitektur "berat" yang sering digunakan sebagai pembanding efisiensi terhadap model Inception. | Bukan, tapi merupakan benchmark industri yang sangat stabil. | Kundu et al., 2021 |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [X] Tidak
> Justifikasi: Pemilihan baseline ini bukan straw man karena kedua model (InceptionV3 dan VGG16) adalah standar industri yang tangguh dan memiliki performa tinggi. Saya tidak memilih metode yang sengaja dibuat lemah untuk dimenangkan (seperti membandingkan CNN dengan algoritma jadul yang tidak relevan), melainkan membandingkan arsitektur Deep Learning tingkat lanjut yang memang bersaing ketat dalam hal akurasi dan penggunaan sumber daya.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Penelitian ini bertujuan untuk mengatasi tingginya risiko subjektivitas pada diagnosis manual penyakit padi melalui pendekatan Positivis dan Design Science dengan mengimplementasikan arsitektur CNN InceptionV3 sebagai solusi digital. Masalah riset difokuskan pada optimasi performa model melalui analisis variasi Epoch (10, 20, 30) untuk menemukan titik akurasi paling efisien di tengah kendala keterbatasan dataset dan kapasitas perangkat keras yang dialami petani di lapangan. Berdasarkan hasil Literature Mapping, ditemukan adanya Method Gap di mana penelitian sebelumnya seperti oleh Siti Aminah dkk. (2022) telah mencapai akurasi 93,3%, namun belum mengeksplorasi batas jenuh efisiensi parameter pada kondisi data kecil. Dengan membandingkan hasil terhadap Baseline standar industri seperti VGG16, riset ini berkontribusi dalam menyediakan pengetahuan baru mengenai konfigurasi Deep Learning yang ringan namun tetap akurat, sehingga mampu menghasilkan Outcome berupa alat deteksi dini yang praktis untuk mencegah penurunan hasil panen secara efektif.
