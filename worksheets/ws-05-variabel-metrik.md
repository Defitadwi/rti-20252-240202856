# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question: Sejauh mana peningkatan jumlah epoch (10, 20, 30) memengaruhi akurasi klasifikasi penyakit padi menggunakan arsitektur InceptionV3 pada dataset terbatas?
| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
|Jumlah Epoch| IV   |Intensitas Pelatihan|Nilai numerik iterasi|ratio|epoch|Menentukan jumlah perulangan saat training model.|Epoch adalah parameter kunci yang menentukan seberapa baik model belajar dari data.|
|Akurasi Klasifikasi| DV   |Performa Model|  Accuracy Score |ratio |persen (%)|Rasio prediksi benar dibanding total data uji.|Metrik standar untuk mengukur efektivitas model klasifikasi citra.|
|Arsitektur Model    | CV   |Struktur Jaringan|InceptionV3|Nominal|  -      |Mengunci model agar tetap menggunakan satu arsitektur.               |Agar perubahan hasil murni karena epoch, bukan karena perbedaan struktur model. |

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [X] Setiap langkah terdokumentasi
  [X] Tidak ada "lompatan logis"
  [X] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** __________________________________________________

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Iterasi Pelatihan | IV | Durasi Belajar | 10, 20, 30 Epoch| ratio |epoch |
|Ketepatan Prediksi | DV |Kualitas Klasifikasi |Overall Accuracy |epoch |persen (%) |
|Dataset & Spek | CV |Lingkungan Uji |1.500 citra & InceptionV3 |Nominal | - |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [X] Tidak
> Jika ya, di mana? ____________________________________

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 |Akurasi secara langsung mewakili kemampuan model membedakan penyakit padi.|
| Sensitive | |Cukup peka untuk melihat kenaikan performa dari 10 ke 30 epoch (74% ke 93%).|
| Feasible | |Sangat mudah dikumpulkan melalui library seperti Keras atau TensorFlow setelah training selesai. |

**Apakah perlu secondary metric?** [ ] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? _____________________________

**Contoh kasus ceiling effect untuk metrik ini:**
> ___________________________________________________

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | *Apakah semua data point terkumpul?* |Ya, semua 1.500 citra harus terproses |Melakukan checking jumlah file sebelum dan sesudah preprocessing. |
| Consistency | *Apakah ada kontradiksi internal?* |Mungkin ada label ganda. |Melakukan checking jumlah file sebelum dan sesudah preprocessing. |
| Validity | *Apakah benar-benar mengukur yang dimaksud?* | | |
| Representativeness | *Apakah sampel mewakili populasi target?* |Ya, mewakili 3 penyakit utama. |Memastikan distribusi jumlah gambar seimbang antar kelas (500 tiap kelas). |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?


**Jawaban:**
> Memilih metrik setelah melihat data dianggap p-hacking karena peneliti cenderung hanya akan memilih metrik yang menunjukkan hasil "bagus" atau "signifikan" (misal: hanya melaporkan akurasi tetapi menyembunyikan loss yang buruk) demi memenangkan hipotesis. Perbedaannya dengan eksplorasi data yang sah adalah pada niat dan pelaporannya: eksplorasi data bertujuan mencari pola baru untuk penelitian masa depan tanpa mengubah kesimpulan hipotesis utama, sedangkan p-hacking adalah manipulasi pelaporan untuk memvalidasi hipotesis yang sebenarnya gagal.
