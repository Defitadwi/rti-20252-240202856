# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (artefak dibuat sebagai instrumen pengujian hipotesis, bukan tujuan akhir).

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : Defita Dwi Wulandary
Tanggal          : 12 April 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: Apakah akurasi ini diuji pada data yang benar-benar baru (test set) atau terjadi overfitting karena dataset yang terlalu homogen
   - Data yang dibutuhkan untuk verifikasi: Rincian pembagian dataset (train/val/test split), nilai Loss untuk mendeteksi overfitting, dan Confusion Matrix untuk melihat apakah ada kelas penyakit tertentu yang sering salah tebak. 

2. Posisi paradigma:
   - Pendekatan: [ ] Positivis  [ ] Interpretivis  [ ] Design Science  [X] Mixed
   - Alasan: Riset ini bersifat Positivis karena menguji hipotesis secara objektif melalui metrik angka (akurasi), sekaligus menerapkan Design Science karena membangun sebuah artefak berupa model sistem klasifikasi untuk memecahkan masalah praktis petani.

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Peneliti mengasumsikan bahwa foto yang diambil oleh pengguna di lapangan akan memiliki kualitas, sudut pandang, dan pencahayaan yang serupa dengan dataset yang digunakan dalam pelatihan.
   - Sumber bias potensial: Sampling Bias, karena jumlah dataset dibatasi hanya 500 gambar per kategori akibat keterbatasan perangkat, sehingga mungkin tidak mencakup semua varietas padi atau kondisi lingkungan.
   - Langkah mitigasi: Menerapkan teknik Data Augmentation (seperti rotasi dan penyesuaian kecerahan) untuk menambah variasi data dan melakukan pengujian pada data independen yang diambil langsung dari area persawahan berbeda.
4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Peneliti mengasumsikan bahwa foto yang diambil oleh pengguna di lapangan akan memiliki kualitas, sudut pandang, dan pencahayaan yang serupa dengan dataset yang digunakan dalam pelatihan.
   - Batasan yang diakui sejak awal: Keterbatasan kapasitas perangkat komputasi yang membatasi jumlah dataset, serta ruang lingkup penelitian yang hanya terbatas pada tiga jenis penyakit daun padi (Blas, Brownspot, dan HDB).
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

**Paper yang dipilih:**
> Judul: Penerapan Metode Convolutional Neural Network (CNN) Dalam Mengklasifikasikan Penyakit Daun Tanaman Padi
> Penulis (Tahun): Gracia Yoel Christiawan, Roy Andani Putra, Azis Sulaiman, Evy Poerbaningtyas, Syntia Widyayuningtias, Putri Listio

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengamati kondisi alami penyakit Blas, Brownspot, dan HDB pada tanaman padi di sawah.| Kondisi cuaca, pergerakan angin, atau bayangan benda lain yang mengaburkan gejala asli penyakit. |
| Data → Processing | Mengambil 1.500 foto daun padi menggunakan kamera HP (500 per jenis penyakit). |Foto hanya diambil dari sudut tertentu dan jumlahnya terbatas (500/kelas), sehingga tidak mewakili seluruh populasi daun padi di dunia nyata |
| Processing → Analysis | Melakukan resizing citra ke 224x224 piksel dan normalisasi nilai pixel untuk input model CNN. |Pengurangan resolusi (downsampling) menghilangkan detail tekstur penting yang mungkin menjadi ciri khas penyakit. |
| Analysis → Inference | Melatih model InceptionV3 dengan variasi 10, 20, dan 30 epoch untuk melihat tren akurasi. |Jika epoch terlalu sedikit (10), model belum belajar (underfit). Jika terlalu banyak, model hanya menghafal data latihan. |
| Inference → Knowledge |Menarik kesimpulan dari kurva akurasi bahwa 30 epoch adalah jumlah optimal untuk model ini. |Menyimpulkan bahwa 30 epoch adalah yang terbaik secara absolut, padahal mungkin ada angka lain (misal 25 atau 40) yang tidak diuji. |

**Distorsi paling besar di tahap:** Data → Processing

**Dua distorsi spesifik yang teridentifikasi:**
1. **Sampling Bias:** Dataset dibatasi hanya 500 data per kategori karena keterbatasan perangkat (device), sehingga mungkin tidak mewakili seluruh variasi visual penyakit di lapangan.
   
2. **Resolution Distortion:** Proses resize gambar asli ke 224x224 piksel dapat menghilangkan detail tekstur halus yang mungkin penting untuk identifikasi penyakit secara medis.

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Peneliti harus melaporkan hasil apa adanya. Jika outlier dihapus, alasan penghapusannya harus berbasis kriteria teknis (misal: data korup atau error sensor), bukan demi mengejar signifikansi (p-hacking). |
| Transparansi |Peneliti wajib mendokumentasikan keberadaan 3 outlier tersebut di bagian metodologi atau lampiran, termasuk menjelaskan dampak keberadaannya terhadap nilai akurasi/signifikansi akhir. |
| Peer review |Penelaah (reviewer) membutuhkan data mentah yang utuh untuk menilai apakah outlier tersebut adalah "noise" yang sah untuk dibuang atau justru merupakan "kasus kritis" yang menunjukkan kelemahan model. |

**Keputusan akhir dan justifikasi:**
> Peneliti harus tetap melaporkan hasil eksperimen dalam dua versi—baik dengan maupun tanpa 3 data point outlier tersebut—disertai penjelasan teknis yang transparan mengenai kriteria penghapusannya. Hal ini dikarenakan dalam riset teknologi informasi, integritas pengetahuan jauh lebih penting daripada sekadar mengejar angka akurasi yang signifikan. Dengan menyajikan kedua hasil, peneliti menghindari praktik cherry-picking (memilih hanya data yang mendukung hipotesis) dan justru memberikan kontribusi ilmiah yang lebih dalam mengenai boundary conditions (batasan kondisi) metode yang diuji, sehingga pembaca dapat memahami dalam situasi apa algoritma tersebut bekerja optimal atau mengalami kegagalan.
---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Klasifikasi Penyakit Daun Tanaman Padi Menggunakan Metode Convolutional Neural Network (CNN) berbasis Arsitektur InceptionV3.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 5 | 1 | 4 |
| Jenis data yang dikumpulkan |Data kuantitatif objektif berupa nilai akurasi (%), skor loss, jumlah epoch, dan confusion matrix. |Data kualitatif berupa persepsi subjektif atau pengalaman emosional petani saat mengamati tanaman padi. |Artefak berupa model komputasi (.h5), kode program (Python), dan arsitektur jaringan saraf yang dibangun. |
| Limitasi paradigma |Cenderung mengabaikan faktor kontekstual di lapangan (seperti kondisi sosial atau cara petani memegang HP). |Hasilnya sangat subjektif dan sulit untuk diuji ulang secara statistik atau dijadikan standar baku. |Terlalu fokus pada "apakah sistem berhasil dibuat", terkadang kurang mendalami fenomena alami dari penyakit itu sendiri. |

**Paradigma yang dipilih:** Positivis (diperkuat oleh Design Science)
**Alasan:** Penelitian ini didominasi oleh paradigma Positivis karena bertujuan membuktikan sebuah hipotesis secara objektif melalui eksperimen yang dapat diukur dengan angka pasti (seperti pembuktian bahwa 30 epoch menghasilkan akurasi lebih baik daripada 10 epoch). Namun, penelitian ini juga mengadopsi Design Science karena peneliti menciptakan sebuah "artefak" (model klasifikasi penyakit) sebagai solusi praktis untuk memecahkan masalah deteksi manual yang selama ini dilakukan oleh petani.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Sebelumnya, saya cenderung menerima klaim "95% akurat" secara mentah-mentah dan menganggapnya sebagai indikator kesuksesan mutlak sebuah sistem. Namun, setelah memahami Rantai Distorsi Pengetahuan, saya menyadari bahwa angka tersebut hanyalah hasil akhir dari serangkaian proses yang rawan bias. Saat ini, ketika membaca sebuah paper, pertanyaan kritis yang akan saya ajukan adalah: "Bagaimana peneliti menangani distorsi dari tahap Reality ke Data?" >
Secara spesifik, saya akan memeriksa apakah dataset yang digunakan cukup representatif terhadap kondisi lapangan yang heterogen atau hanya "bersih" di lingkungan laboratorium. Selain itu, saya akan mempertanyakan apakah ada detail penting yang hilang selama proses preprocessing (seperti resizing pada citra daun padi di jurnal) yang sebenarnya bisa mengubah hasil klasifikasi jika diterapkan pada skenario dunia nyata.

