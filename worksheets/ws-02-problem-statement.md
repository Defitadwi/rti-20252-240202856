# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Computer Vision / Agriculture Technology (Agroteknologi).
  Konteks  : Identifikasi otomatis penyakit tanaman padi (Blas, Brownspot, HDB) untuk membantu petani di Indonesia dalam deteksi dini.

System Context
  Input       : Citra digital (foto) daun tanaman padi yang diambil melalui kamera perangkat mobile.
  Process     : Preprocessing (resize & normalisasi), ekstraksi fitur menggunakan arsitektur InceptionV3, dan pelatihan model CNN.
  Output      : Label kategori penyakit (Blas, Brownspot, atau HDB) beserta nilai akurasi klasifikasi.
  Outcome     : Meningkatkan akurasi dan kecepatan petani dalam mendiagnosis penyakit padi tanpa harus bergantung sepenuhnya pada pakar manual.
  Constraints : Keterbatasan perangkat keras (device) untuk pemrosesan dataset besar dan variasi pencahayaan pada foto lapangan.
  Stakeholders: Petani, penyuluh pertanian, dan pengembang sistem informasi pertanian.

Fenomena → Problem
  Fenomena yang diamati             : Identifikasi penyakit daun padi oleh petani saat ini masih dilakukan secara manual dan konvensional.
  Gejala (symptom) yang terukur     : Tingkat kesalahan diagnosis manual yang tinggi dan keterlambatan penanganan penyakit yang menyebabkan penurunan hasil panen.
  Masalah yang didiagnosis          : Belum adanya sistem otomatis yang cukup tangguh dan cepat dalam mengenali ciri visual penyakit padi secara objektif.
  Masalah riset (researchable)      : Bagaimana performa arsitektur CNN InceptionV3 dengan variasi jumlah epoch (10, 20, 30) dalam membedakan pola visual penyakit Blas, Brownspot, dan HDB pada dataset citra yang terbatas?
  Variabel yang terukur             : Akurasi klasifikasi (%), loss score, dan jumlah epoch.

Problem Quality Check
  [X] Clarity — Masalah didefinisikan secara spesifik pada metode CNN (InceptionV3) dan objek penyakit padi (Blas, Brownspot, HDB), bukan sekadar "masalah pertanian" secara umum.
  [X] Measurability — Menggunakan metrik kuantitatif yang jelas yaitu Akurasi (%) dan Loss melalui variasi Epoch (10, 20, 30).
  [X] Relevance — Sangat relevan bagi domain agroteknologi di Indonesia mengingat padi adalah komoditas pangan utama yang sering terdampak penyakit.
  [X] Testability — Eksperimen ini bisa gagal jika ternyata penambahan epoch tidak meningkatkan akurasi atau jika model mengalami overfitting.
  [X] Impact — Jika terjawab, penelitian ini berkontribusi pada efisiensi deteksi dini penyakit tanaman yang dapat mencegah gagal panen.

Problem Statement (1 paragraf):
Identifikasi penyakit pada daun tanaman padi saat ini masih didominasi oleh pengamatan manual yang berisiko tinggi terhadap subjektivitas dan keterlambatan diagnosis. Meskipun metode Deep Learning seperti Convolutional Neural Network (CNN) dengan arsitektur InceptionV3 menawarkan solusi otomatisasi, efektivitas performanya sangat dipengaruhi oleh parameter pelatihan seperti jumlah epoch, terutama ketika dihadapkan pada keterbatasan jumlah dataset. Oleh karena itu, penelitian ini bertujuan untuk mengatasi kesenjangan akurasi pada deteksi manual dengan menguji dan menganalisis pengaruh variasi epoch (10, 20, dan 30) terhadap tingkat akurasi klasifikasi penyakit Blas, Brownspot, dan HDB, guna menghasilkan model yang optimal dan dapat diandalkan untuk membantu petani dalam pengambilan keputusan di lapangan.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Otomatisasi Deteksi Penyakit Tanaman Padi menggunakan Computer Vision.
| Tahap | Hasil |
|-------|-------|
| Reality | Petani kesulitan membedakan jenis penyakit daun padi (Blas, Brownspot, HDB) secara akurat di lapangan tanpa bantuan pakar. |
| Observed Issue (Symptom) | Sering terjadi kesalahan diagnosis manual yang mengakibatkan kesalahan penggunaan pestisida dan penurunan hasil panen.|
| Diagnosed Problem (Root Cause) |Kurangnya instrumen deteksi objektif yang mampu mengenali pola visual penyakit secara cepat dalam berbagai kondisi data. |
| Researchable Problem |Sejauh mana efektivitas arsitektur CNN InceptionV3 dalam mempertahankan akurasi klasifikasi pada dataset yang terbatas melalui optimasi epoch? |
| Measurable Variable |Akurasi (%) sebagai metrik keberhasilan dan Loss Value sebagai indikator performa pelatihan model. |

**Apakah terjebak solution-first thinking?** [ ] Ya / [X] Tidak
> Tidak, Karena alur di atas berawal dari masalah nyata di lapangan (petani salah diagnosis), bukan diawali dengan keinginan untuk "pokoknya harus pakai CNN". CNN baru muncul di tahap ke-4 sebagai metode yang diusulkan untuk menjawab masalah yang sudah didiagnosis sebelumnya.

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Citra digital (foto) daun padi yang terinfeksi (Blas, Brownspot, HDB) dalam format RGB. |
| Process |Image preprocessing (resizing 224x224), ekstraksi fitur menggunakan arsitektur InceptionV3, dan klasifikasi melalui Fully Connected Layer. |
| Output |Label prediksi kategori penyakit dan nilai probabilitas keyakinan (confidence score) |
| Outcome |Peningkatan akurasi diagnosis penyakit padi oleh petani yang berdampak pada ketepatan penanganan tanaman. |
| Constraints |Keterbatasan memori perangkat keras untuk pelatihan data, variasi pencahayaan pada data input, dan jumlah dataset yang terbatas (500 per kelas). |
| Stakeholders |Peneliti (sebagai pengembang model), Petani (pengguna akhir), dan Dinas Pertanian (pembuat kebijakan). |

**Komponen mana yang paling relevan dengan masalah riset?** 
Process dan Constraints.

Alasan:
Masalah riset ini (seperti dalam jurnal) berfokus pada bagaimana Process (arsitektur CNN dan variasi epoch) dapat menghasilkan output yang akurat meskipun menghadapi Constraints (keterbatasan data dan perangkat). Inti dari riset TI bukan sekadar membuat sistem yang jalan, melainkan mengoptimalkan bagian Process untuk mengatasi hambatan yang ada pada Constraints.

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 |Sangat jelas karena menyebutkan metode spesifik (InceptionV3), objek spesifik (penyakit padi), dan parameter yang diuji (epoch). |
| Measurability |5 |Memiliki metrik kuantitatif yang sangat terukur, yaitu nilai Akurasi (%) dan Loss yang dihasilkan dari eksperimen. |
| Relevance |5 |Sangat relevan dengan domain informatika (Computer Vision) dan sektor pertanian (ketahanan pangan). |
| Testability |5 |Sangat bisa diuji; hipotesis bisa terbukti benar (akurasi naik seiring epoch) atau gagal (terjadi overfitting/stagnasi). |
| Impact |4 |Memberikan kontribusi nyata dalam otomatisasi pertanian, meskipun dampaknya bergantung pada implementasi perangkat di lapangan. |

**Skor total:** 24 / 25

**Problem statement versi final (1 paragraf):**
> Identifikasi penyakit pada daun tanaman padi saat ini masih didominasi oleh pengamatan manual yang memiliki risiko subjektivitas dan keterlambatan diagnosis yang tinggi. Meskipun metode Deep Learning seperti Convolutional Neural Network (CNN) menawarkan solusi otomatisasi, kinerjanya sangat dipengaruhi oleh parameter pelatihan seperti jumlah epoch, terutama ketika dihadapkan pada keterbatasan jumlah dataset dan perangkat komputasi. Oleh karena itu, penelitian ini bertujuan untuk menganalisis pengaruh variasi jumlah epoch (10, 20, dan 30) menggunakan arsitektur InceptionV3 terhadap tingkat akurasi klasifikasi penyakit Blas, Brownspot, dan HDB, guna menghasilkan model yang optimal dan dapat diandalkan untuk membantu petani dalam pengambilan keputusan secara cepat dan akurat.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Perbedaan fundamental terletak pada tujuan akhir dan sifat ketidakpastiannya. Saat coding, masalah biasanya berupa bug atau error teknis yang memiliki solusi pasti; tujuannya adalah fungsionalitas ("bagaimana agar sistem jalan?"). Pendekatannya cenderung linier: mencari letak kesalahan sintaks atau logika, lalu memperbaikinya hingga sistem kembali normal.

Sebaliknya, dalam masalah riset, masalah didefinisikan sebagai kesenjangan pengetahuan (knowledge gap); tujuannya bukan sekadar membuat sistem jalan, melainkan mencari kebenaran yang dapat dibuktikan ("mengapa metode ini bekerja atau gagal?"). Masalah riset bersifat terbuka (open-ended), di mana kegagalan eksperimen (seperti akurasi yang rendah) tetap dianggap sebagai hasil ilmiah asalkan prosesnya terdokumentasi secara jujur. Pendekatannya bersifat kritis dan skeptis, di mana kita harus mempertanyakan validitas data dan metodologi, bukan hanya fokus pada hasil akhir.

| Dimensi | Masalah Coding (Engineering) | Masalah Riset (Research) |
|-------|------------|----------|
| Fokus Utama | Konstruksi dan Fungsionalitas. | Penemuan dan Validasi Pengetahuan. |
| Pertanyaan Inti | "Bagaimana cara membuatnya berfungsi?" | "Mengapa fenomena ini terjadi?" |
| Definisi Sukses | Sistem bebas error dan fitur berjalan | Klaim terbukti secara objektif (meski hasilnya negatif). |
| Cara Pendekatan| Trial and error hingga bug hilang. | Eksperimen sistematis dengan variabel terkontrol. |
