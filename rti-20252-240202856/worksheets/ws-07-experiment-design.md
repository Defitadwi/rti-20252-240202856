# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

Research Question : Bagaimana performa metode Convolutional Neural Network (CNN) dengan arsitektur InceptionV3 yang dioptimasi menggunakan Keras Tuner dalam meningkatkan akurasi klasifikasi pada dataset citra penyakit daun padi (Blas, HDB, dan Bercak Coklat) dibandingkan dengan baseline model CNN standar tanpa teknik augmentasi distorsi kecerahan?
Hypothesis        : Penerapan arsitektur InceptionV3 yang dikombinasikan dengan Keras Tuner dan teknik augmentasi berupa distorsi pengurangan kecerahan citra sebesar 25% secara signifikan dapat meningkatkan akurasi klasifikasi penyakit daun padi hingga mencapai titik optimal dan mencegah terjadinya overfitting.
Tipe Eksperimen   : [X] Comparison  [ ] Ablation  [X] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control |Kondisi ini menggunakan model jaringan saraf tiruan dasar buatan sendiri tanpa adanya optimasi parameter tambahan. |Arsitektur CNN standar (Own Model) non-pre-trained tanpa modifikasi hiperparameter.|Dataset diatur tetap menggunakan total 1.630 citra penyakit daun padi dengan rasio partisi data sebesar 75% untuk training dan 25% untuk testing.|
| Treatment |Kondisi ini menerapkan arsitektur deep learning tingkat lanjut yang telah dioptimasi secara otomatis menggunakan pustaka Keras Tuner. |Arsitektur model CNN InceptionV3 yang dikombinasikan dengan teknik augmentasi berupa pengurangan kecerahan gambar sebesar 25%.|Dataset dan rasio pembagian data dijaga benar-benar identik dengan kelompok kontrol, yaitu 1.630 citra daun padi dengan perbandingan partisi training dan testing sebesar 75:25.|

Fairness Checklist:
  [X] Dataset identik untuk semua kondisi
  [X] Preprocessing setara
  [X] Tuning effort setara
  [X] Environment identik
  [X] Metrik evaluasi sama

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    |Munculnya ancaman berupa ketidakstabilan performa model dan tingginya potensi risiko overfitting saat pengujian awal menggunakan model dasar buatan sendiri.                 |Peneliti mengatasinya dengan beralih ke arsitektur InceptionV3 yang memiliki modul konvolusi paralel efisien untuk mereduksi jumlah parameter serta menerapkan teknik augmentasi kecerahan.          |
| External    |Keterbatasan jumlah sampel gambar asli lapangan yang hanya berjumlah 500 hingga 630 citra per jenis penyakit padi akibat keterbatasan kapasitas perangkat keras komputer yang dimiliki peneliti.                 |Peneliti memitigasi ancaman keterbatasan generalisasi ini dengan mengimplementasikan teknik augmentasi data berupa manipulasi tingkat kecerahan gambar piksel ke piksel guna memperluas variasi visual buatan.          |
| Construct   |Adanya risiko kesalahan penafsiran performa keandalan sistem jika evaluasi pengujian hanya terpaku pada nilai tingkat akurasi data pelatihan (training) saja yang berpotensi bias.                 |Peneliti mengatasinya dengan menggunakan kombinasi metrik evaluasi penyeimbang yang valid di dalam deep learning, yaitu menyelaraskan grafik Validation Accuracy yang tinggi dengan grafik Validation Loss yang rendah.          |
| Conclusion  |Risiko penarikan kesimpulan statistik yang keliru atau bias mengenai pengaruh hiperparameter akibat kurangnya variasi jumlah iterasi pelatihan model.                 |Peneliti menyusun rencana pengujian berulang secara terstruktur menggunakan variasi parameter epoch yang bertahap (mulai dari 10, 20, 30, 50, hingga 75 epoch) guna membuktikan kestabilan nilai akurasi akhir model.          |

Statistical Plan:
  Uji statistik   : Analisis matriks konfusi (Confusion Matrix) beserta visualisasi perbandingan kurva grafik konvergensi antara variasi tingkat Epoch terhadap nilai Loss dan Accuracy.
  Justifikasi      : Metode penentuan performa deskriptif kuantitatif ini merupakan standar baku di bidang deep learning untuk membuktikan secara empiris apakah model mengalami overfitting, underfitting, atau berhasil mencapai titik saturasi optimal.  
  Alpha            : Batas toleransi margin kesalahan ditentukan berdasarkan tingkat kepercayaan statistik di atas 0,95, yang setara dengan pencapaian akurasi validasi minimum sebesar 95% pada skenario model yang diuji.
  Effect size min  : Target ukuran efek minimal ditandai dengan penurunan nilai Validation Loss hingga berada di bawah ambang skor 0,10 serta peningkatan nilai Validation Accuracy yang stabil hingga melampaui ambang batas skor 0,95 atau 95%.
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Bagaimana performa metode Convolutional Neural Network (CNN) dengan arsitektur InceptionV3 yang dioptimasi menggunakan Keras Tuner dalam meningkatkan akurasi klasifikasi pada dataset citra penyakit daun padi (Blas, HDB, dan Bercak Coklat) dibandingkan dengan baseline model CNN standar tanpa teknik augmentasi distorsi kecerahan?
**Tipe eksperimen:** [X] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------- -----|
| Control |Skenario ini menggunakan arsitektur jaringan saraf tiruan dasar buatan sendiri tanpa adanya optimasi parameter tambahan. |Model CNN standar (Own Model) non-pre-trained tanpa modifikasi hiperparameter.|Dataset diatur tetap menggunakan total 1.630 citra penyakit daun padi dengan rasio partisi data sebesar 75% untuk training dan 25% untuk testing.|
| Treatment |Skenario ini menerapkan arsitektur deep learning tingkat lanjut yang dikombinasikan dengan teknik augmentasi data |Arsitektur model CNN InceptionV3 yang diintegrasikan dengan pengurangan tingkat kecerahan gambar sebesar 25%. |Dataset dan rasio pembagian data dijaga benar-benar identik, yaitu menggunakan 1.630 citra daun padi dengan perbandingan partisi training dan testing sebesar 75:25. |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | Ya |Baik kelompok kontrol (Own Model) maupun kelompok perlakuan (Treatment dengan InceptionV3) sama-sama diuji menggunakan dataset penyakit daun padi yang identik dengan total 1.630 gambar. |
| Preprocessing setara |Ya|Seluruh gambar pada semua skenario melalui proses prapemrosesan yang seragam, meliputi tahap anotasi data, pelabelan posisi dan kelas objek, serta penentuan ukuran matriks input gambar yang sama. |
| Tuning effort setara |Ya |Peneliti mengalokasikan beban iterasi pelatihan model yang sebanding dan terukur secara sistematis dengan melakukan proses pelatihan berulang pada berbagai skenario hiperparameter hingga menyentuh batas pengujian 75 epoch. |
| Environment identik |Ya |Proses training dan testing untuk model dasar maupun model optimasi dijalankan pada satu ekosistem library Keras dan arsitektur komputasi perangkat keras yang sama untuk menghindari bias performa.|
| Metrik evaluasi sama |Ya |Performa keberhasilan model diukur secara seragam dan konsisten menggunakan metrik evaluasi baku yang sama untuk semua kondisi, yaitu nilai akurasi validasi (Validation Accuracy) dan skor kerugian validasi (Validation Loss). |

**Ada yang tidak fair?** [ ] Ya / [X] Tidak
> Jika ya, bagaimana cara memperbaikinya? ________________

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Munculnya ancaman berupa ketidakstabilan performa model dan tingginya potensi risiko overfitting saat pengujian awal menggunakan model dasar buatan sendiri.| Peneliti mengatasinya dengan beralih ke arsitektur InceptionV3 yang memiliki modul konvolusi paralel efisien untuk mereduksi jumlah parameter serta menerapkan teknik augmentasi kecerahan. |
| External |Keterbatasan jumlah sampel gambar asli lapangan yang hanya berjumlah 500 hingga 630 citra per jenis penyakit padi akibat keterbatasan kapasitas perangkat keras komputer yang dimiliki peneliti. |Peneliti memitigasi ancaman keterbatasan generalisasi ini dengan mengimplementasikan teknik augmentasi data berupa manipulasi tingkat kecerahan gambar piksel ke piksel guna memperluas variasi visual buatan. |
| Construct |Adanya risiko kesalahan penafsiran performa keandalan sistem jika evaluasi pengujian hanya terpaku pada nilai tingkat akurasi data pelatihan (training) saja yang berpotensi bias. |Peneliti mengatasinya dengan menggunakan kombinasi metrik evaluasi penyeimbang yang valid di dalam deep learning, yaitu menyelaraskan kurva grafik Validation Accuracy yang tinggi dengan penurunan grafik Validation Loss secara konsisten. |
| Conclusion |Risiko penarikan kesimpulan statistik yang keliru atau bias mengenai pengaruh perubahan hiperparameter akibat kurangnya variasi jumlah iterasi pelatihan model. |Peneliti menyusun rencana pengujian berulang secara terstruktur menggunakan variasi parameter epoch yang bertahap (mulai dari 10, 20, 30, 50, hingga 75 epoch) guna membuktikan kestabilan nilai akurasi akhir model. |


**Ancaman mana yang paling sulit dimitigasi?** External Validity (Validitas Eksternal).
**Mengapa?**
>Hal ini dikarenakan mitigasi untuk mengatasi keterbatasan jumlah dataset (yang dibatasi maksimal 500 hingga 630 citra per kategori penyakit) sangat bergantung pada faktor eksternal berupa ketersediaan spesifikasi perangkat keras (device hardware) yang dimiliki oleh peneliti. Meskipun teknik augmentasi data telah digunakan untuk memanipulasi kecerahan gambar piksel ke piksel , model tetap belum diuji menggunakan variasi lingkungan dataset riil berskala besar di luar 3 jenis penyakit padi tersebut karena keterbatasan kapasitas komputasi perangkat saat proses pelatihan berlangsung

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. Apakah seluruh model baseline diuji menggunakan dataset, tahapan preprocessing, dan lingkungan ekosistem (environment) yang benar-benar identik?
2. Apakah upaya optimasi parameter (tuning effort) yang diberikan kepada model baseline sudah setara dan adil dengan metode yang diusulkan, atau baseline hanya dijalankan dengan pengaturan standar (default)?
3. Metrik evaluasi apa yang digunakan untuk mengukur keunggulan tersebut, dan apakah peningkatan performa yang dihasilkan signifikan secara statistik atau justru berisiko mengalami overfitting?