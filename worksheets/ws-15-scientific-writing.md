# WS-15: Scientific Writing

> **Bab 15 — Penulisan Ilmiah**

---

## Ringkasan Materi

### Scientific Argument Flow

```
Problem → Gap → RQ → Method → Result → Analysis → Conclusion → Contribution
```

Paper ilmiah adalah **satu argumen utuh** dari masalah ke kontribusi. Setiap node harus terhubung logis ke node sebelum dan sesudahnya.

### Struktur IMRAD

| Section | Peran | Pertanyaan Kunci |
|---------|-------|-----------------|
| **Introduction** | Motivasi + frame | Why is this needed? |
| **Method** | Deskripsi (reproducible) | How was it done? |
| **Results** | Laporan objektif | What was found? |
| **Discussion** | Interpretasi + refleksi | What does it mean? |
| **Conclusion** | Ringkasan + kontribusi | So what? |

### Logical Flow — "Red Thread"

Setiap paragraf menjawab satu pertanyaan dan memicu pertanyaan berikutnya. Alur logis ini harus terasa di tiga level:
1. **Antar-kalimat** dalam paragraf
2. **Antar-paragraf** dalam section
3. **Antar-section** dalam paper

### Internal Consistency

Setiap elemen yang dijanjikan di Introduction harus hadir di Discussion/Conclusion.

**Consistency Matrix:**
```
           Intro  Method  Result  Discuss  Conclude
RQ1          ✓      ✓       ✓       ✓        ✓
RQ2          ✓      ✓       ✓       ✗ ←      ✓
Metrik-X     ✗      ✗       ✓ ←     ✗        ✗
```
**Masalah:** RQ2 dibahas di semua bagian kecuali Discussion. Metrik-X muncul di Result tapi tidak diperkenalkan di Method.

### Writing Quality Triad

| Kualitas | Deskripsi | Contoh Buruk → Baik |
|----------|----------|---------------------|
| **Clarity** | Dipahami sekali baca | "Performa meningkat" → "Accuracy meningkat dari 85.3% ke 89.7%" |
| **Precision** | Istilah eksak, tanpa ambiguitas | "signifikan" → "signifikan secara statistik (p=0.003, d=1.2)" |
| **Conciseness** | Setiap kata menambah informasi | Hapus kalimat redundan, filler words |

### Urutan Penulisan yang Disarankan

1. **Method & Results** — paling stabil, tulis pertama
2. **Discussion** — interpretasi berdasarkan hasil
3. **Introduction** — frame sesuai temuan aktual
4. **Abstract & Conclusion** — terakhir

### Target Jumlah Kata

| Section | Target |
|---------|--------|
| Introduction | 500–700 |
| Related Work | 700–1000 |
| Method | 800–1200 |
| Results | 500–800 |
| Discussion | 600–900 |
| Conclusion | 200–400 |

### Jebakan Kognitif

1. "Lebih panjang = lebih lengkap" → conciseness lebih berharga
2. "Introduction harus ditulis pertama" → justru ditulis terakhir
3. "Jargon teknis = lebih ilmiah" → clarity lebih penting
4. "Discussion = ringkasan Results" → Discussion = interpretasi + konteks

---

## Template A.15 — Paper Structure Checklist

```
PAPER STRUCTURE CHECKLIST

Title   : Klasifikasi Penyakit Daun Padi Menggunakan Metode Convolutional Neural Network Berbasis Arsitektur InceptionV3 dengan Optimasi Hiperparameter Keras Tuner dan Augmentasi Distorsi Kecerahan
Target  : [X] Jurnal  [ ] Konferensi  [ ] Laporan

Section Check:
  [X] Abstract — masalah, metode, hasil utama, kontribusi (max 250 kata)
  [X] Introduction — konteks → gap → RQ → kontribusi → struktur paper
  [X] Related Work — concept-centric, gap positioning
  [X] Method — reproducible: desain, variabel, metrik, setup, prosedur
  [X] Results — tabel + grafik + observasi (tanpa interpretasi)
  [X] Discussion — interpretasi, perbandingan, implikasi, limitation
  [X] Conclusion — jawaban RQ, kontribusi, future work

Consistency Matrix:
  [X] RQ di Introduction = RQ di Method = RQ di Conclusion
  [X] Variabel di Method = variabel di Results
  [X] Klaim di Discussion didukung data di Results
  [X] Limitasi di Discussion di-address di Conclusion/Future Work

Writing Quality:
  [X] Clarity — mudah dipahami tanpa re-read
  [X] Precision — tidak ada istilah ambigu
```

---

## Latihan 1 — Paper Outline

Buat outline paper untuk riset Anda menggunakan struktur IMRAD.

| Section | Konten Utama (2-3 kalimat) | Target Kata |
|---------|---------------------------|------------|
| Abstract | Penyakit Blas, HDB, dan Bercak Coklat mengancam produktivitas padi. Studi ini menguji model InceptionV3 di bawah optimasi Keras Tuner dan augmentasi reduksi cahaya -25% pada 1.630 citra. Hasil akhir mencapai akurasi validasi tertinggi 98% dan loss minimum 0.0564. | 200-250 |
| Introduction | Konteks: Pentingnya deteksi penyakit daun padi digital untuk mengganti diagnosis manual petani yang bias. Gap: Model terdahulu rentan drop akurasi saat intensitas cahaya sawah meredup. RQ: Bagaimana performa InceptionV3 + Keras Tuner + augmentasi cahaya dalam menjaga ketangguhan akurasi? | 500-700 |
| Related Work | Meninjau studi klasifikasi penyakit daun padi menggunakan MobileNetV1 (akurasi 92%) dan VGG19 (95.24%). Mengidentifikasi celah riset (gap) berupa batasan ukuran dataset (<500 citra per kelas) dan ketiadaan uji fluktuasi cahaya lapangan.| 700-1000 |
| Method | Menggunakan Controlled Laboratory Experiment dengan dataset sekunder 1.630 citra (Blas: 630, HDB: 500, Brownspot: 500). Skema partisi data dikunci pada rasio 75:25, ukuran batch 32, resolusi $299 \times 299$ piksel, dan rentang pencarian otomatis Keras Tuner pada TensorFlow 2.x.| 800-1200 |
| Results | Menyajikan tabel ringkasan metrik deskriptif 5 kali run eksperimen. Menampilkan visualisasi Line Chart performa kurva konvergensi akurasi vs epoch (maksimal 75 epoch) serta visualisasi Confusion Matrix hasil klasifikasi model intervensi.| 500-800 |
| Discussion | Menginterpretasikan capaian rata-rata akurasi intervensi (96.8%) yang unggul signifikan secara statistik ($p=0.0003$) dibanding baseline model standar (75.4%). Membahas batasan model (boundary condition) yang hanya toleran terhadap drop cahaya maksimal -25%.| 600-900 |
| Conclusion | Menyimpulkan bahwa kombinasi transfer learning InceptionV3 dan optimasi otomatis berhasil menjawab RQ secara valid. Kontribusi utamanya adalah model tangguh yang siap dideploy ke backend aplikasi web "Padisick".| 200-400 |

---

## Latihan 2 — Consistency Matrix

Buat consistency matrix untuk memverifikasi internal consistency paper Anda.

|  | Intro | Method | Result | Discussion | Conclusion |
|--|-------|--------|--------|-----------|-----------|
| RQ1 (Performa Intervensi) | *✓* | *✓* | *✓* | *✓* | *✓* |
| Metrik Utama (Accuracy & Loss) | *✓* | *✓* | *✓* | *✓* | *✓* |
| RQ1 | *✓* | *✓* | *✓* | *✓* | *✓* |
| RQ2 | *✓* | *✓* | *✓* | *✓* | *✓* |
| Metrik utama | *✓* | *✓* | *✓* | *✓* | *✓* |
| Variabel IV | *✓* | *✓* | *✓* | *✓* | *✓* |
| Variabel DV | *✓* | *✓* | *✓* | *✓* | *✓* |
| Klaim/kontribusi | *✓* | *✓* | *✓* | *✓* | *✓* |

**Isi setiap sel:** ✓ (ada & konsisten), ✗ (missing), ~ (ada tapi inkonsisten)

**Inkonsistensi yang ditemukan:**
> Tidak ditemukan inkonsistensi substantif karena variabel independen (IV) dan dependen (DV) telah dikunci sejak awal penyusunan bab proposal dan diuji secara empiris menggunakan dataset konstan 1.630 citra.

**Tindakan perbaikan:**
> Memastikan penulisan lambang matematika metrik (seperti pencantuman nilai $p$-value dan indeks absolut Validation Loss) ditulis dengan format notasi desimal yang seragam di seluruh bab isi laporan.

---

## Latihan 3 — Writing Quality Check

Ambil satu paragraf dari tulisan Anda (atau tulis paragraf baru) dan evaluasi kualitasnya.

**Paragraf asli:**
> Pada penelitian ini, performa dari model klasifikasi yang diusulkan oleh kami diuji dengan menggunakan bermacam-macam jumlah iterasi epoch yang tujuannya adalah agar bisa mengetahui hasil akurasi yang paling maksimal sekali untuk mendeteksi bintik penyakit tanaman padi di sawah di mana data gambar yang dimasukkan totalnya ada sekitar 1.630 gambar yang kemudian sistemnya akan memproses data tersebut lewat folder-folder.

| Kriteria | Evaluasi | Perbaikan |
|----------|---------|-----------|
| Clarity | Kata "performa" terlalu ambigu karena bisa bermakna akurasi, loss, atau kecepatan waktu training. Frasa "lewat folder-folder" kurang ilmiah dan tidak jelas alurnya. bisa berarti accuracy atau speed* | Menjelaskan secara spesifik metrik yang diukur (Validation Accuracy dan Loss) serta alur data (split partisi). |
| Precision | Penggunaan kata "bermacam-macam" dan "sekitar 1.630" tidak eksak/ambigu untuk karya ilmiah.| Mengganti menjadi nilai eksak: skenario 10 hingga 75 epoch dan total 1.630 citra secara konstan.|
| Conciseness | Banyak kata pemborosan (filler words) seperti "oleh kami", "tujuannya adalah agar bisa", dan "paling maksimal sekali" yang membuat kalimat bertele-tele.| Menghapus kata redundan dan menyusun ulang kalimat menjadi struktur aktif-efektif.|

**Paragraf setelah perbaikan:**
>Eksperimen ini mengevaluasi pengaruh variasi jumlah pelatihan (10 hingga 75 epoch) terhadap metrik Validation Accuracy dan Loss pada model InceptionV3. Pengujian menggunakan dataset konstan sebanyak 1.630 citra penyakit daun padi yang dibagi secara konsisten menggunakan rasio partisi 75% data training dan 25% data testing.
---

## Refleksi

> Apa perbedaan antara menulis "tentang" riset dan menulis sebagai "argumen" riset? Bagaimana urutan penulisan (Method → Discussion → Introduction) mengubah kualitas tulisan?

>Menulis "tentang" riset hanya sekadar melaporkan kronologi aktivitas. Sebaliknya, menulis sebagai "argumen" adalah menyusun bukti logis dari awal hingga akhir untuk membuktikan bahwa solusi yang diusulkan benar-benar menjawab masalah dan memiliki kontribusi baru (novelty).Urutan penulisan (Method → Discussion → Introduction) menjaga tulisan tetap objektif dan sinkron. Kita mengunci fakta eksperimen terlebih dahulu (Method & Results), menginterpretasikan maknanya (Discussion), baru kemudian merancang latar belakang (Introduction) agar membingkai temuan aktual tersebut secara pas tanpa spekulasi berlebih.
