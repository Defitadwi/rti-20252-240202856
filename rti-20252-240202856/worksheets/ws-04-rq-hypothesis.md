# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  :Belum adanya analisis mengenai efektivitas optimasi jumlah epoch pada arsitektur InceptionV3 untuk meningkatkan akurasi klasifikasi penyakit padi pada kondisi dataset terbatas.

Research Question:
  Tipe         : [ ] Comparison  [X] Improvement  [ ] Exploratory
  Formulasi    : Apakah peningkatan jumlah epoch (dari 10 ke 30) pada arsitektur InceptionV3 secara signifikan meningkatkan akurasi klasifikasi penyakit Blas, Brownspot, dan HDB pada dataset citra padi yang terbatas?
  Variabel IV  :Jumlah epoch (10, 20, 30).
  Variabel DV  : Akurasi klasifikasi.
  Metrik       : Percentage of Accuracy (%) dan Loss Score.
  Dataset      : 1.500 citra penyakit daun padi (500 per kelas).
  Baseline     : Model InceptionV3 dengan 10 epoch.
Quality Check RQ:
  [X] Variabel spesifik
  [X] Metrik jelas
  [X] Baseline ada
  [X] Konteks disebutkan
  [X] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Pengaruh penambahan iterasi (epoch) terhadap stabilitas akurasi pada arsitektur CNN tertentu saat menangani data kecil.
  Jenis kontribusi        : [X] Improvement  [ ] Comparison  [ ] Novel approach
  Gap yang diisi          : Kurangnya standar optimasi parameter pelatihan untuk hardware dan dataset terbatas.

Hypothesis Pair:
  H₀ : Tidak ada perbedaan signifikan pada nilai akurasi klasifikasi penyakit padi antara penggunaan 10 epoch dan 30 epoch menggunakan InceptionV3.
  H₁ : Penggunaan 30 epoch menghasilkan akurasi klasifikasi yang lebih tinggi secara signifikan dibandingkan 10 epoch pada arsitektur InceptionV3.
  Threshold              : Kenaikan akurasi sebesar ≥ 15%.
  Justifikasi threshold  : Berdasarkan jurnal acuan (Siti Aminah), kenaikan dari 10 ke 30 epoch meningkatkan akurasi dari 74% ke 93,3%.
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Kurangnya pemahaman tentang titik saturasi optimasi epoch pada InceptionV3 saat menghadapi dataset yang terbatas.
**RQ versi pertama (tulis bebas):**
> Bagaimana pengaruh jumlah epoch terhadap hasil akurasi deteksi penyakit padi?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | ya |InceptionV3 (CNN) |
| Metrik terukur |ya |Akurasi (%) |
| Baseline |ya |Perbandingan antar jumlah epoch (10 vs 30) |
| Dataset/konteks |ya |Penyakit daun padi (Blas, Brownspot, HDB) |

**Tipe RQ:** [ ] Comparison / [X] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Sejauh mana peningkatan jumlah epoch dari 10 menjadi 30 dapat meningkatkan akurasi model InceptionV3 dalam mengklasifikasikan tiga jenis penyakit daun padi pada dataset terbatas?
---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ |Tidak ada peningkatan akurasi yang signifikan (p > 0.05) pada klasifikasi penyakit padi saat jumlah epoch ditambah dari 10 ke 30. |
| H₁ |Penambahan jumlah epoch hingga 30 meningkatkan akurasi klasifikasi secara signifikan pada model InceptionV3. |
| Metrik |Accuracy Percentage. |
| Threshold |Akurasi ≥ 90% pada epoch 30. |
| Justifikasi threshold |Menyamai atau melampaui hasil penelitian Siti Aminah dkk. (2022). |

**Apakah hipotesis ini falsifiable?** [X] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Jika setelah eksperimen dilakukan, hasil akurasi pada epoch 30 tetap rendah atau tidak berbeda jauh dengan epoch 10 (misal: hanya naik 1-2%), maka H₁ ditolak dan H₀ diterima

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ |Apakah peningkatan epoch meningkatkan akurasi InceptionV3 pada klasifikasi penyakit padi?|
| Variable (IV) |Variasi jumlah epoch (10, 20, 30).|
| Variable (DV) |Performa klasifikasi model. |
| Metric |Accuracy dan Categorical Crossentropy Loss. |
| Data source |Dataset citra daun padi sebanyak 1.500 gambar. |
| Analysis method |Perbandingan nilai akurasi menggunakan Confusion Matrix. |

**Apakah rantai lengkap?** [X] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Penerapan Metode Convolutional Neural Network Dalam Mengklasifikasikan Penyakit Daun Tanaman Padi.
**RQ yang diekstrak:** Sejauh mana variasi jumlah epoch (10, 20, 30) memengaruhi nilai akurasi dan loss pada arsitektur InceptionV3 untuk mengklasifikasikan citra penyakit Blas, Brownspot, dan HDB?
**Komponen yang hilang:** Meskipun RQ tersebut sudah sangat baik dalam aspek internal (metode, metrik, dan konteks), komponen yang sering "hilang" atau tidak disebutkan secara eksplisit dalam banyak paper sejenis adalah Baseline Eksternal. Paper tersebut berfokus pada improvement internal (perbandingan antar epoch), namun tidak menyandingkan hasilnya dengan arsitektur lain (seperti ResNet atau MobileNet) sebagai pembanding standar industri pada dataset yang sama.
