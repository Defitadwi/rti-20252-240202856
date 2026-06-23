# WS-08: Proposal Integration (UTS)

> **Bab 8 — Proposal & Checkpoint**

---

## Ringkasan Materi

### Proposal = Satu Argumen Utuh

Proposal riset bukan kumpulan bab yang independen. Ia adalah **satu argumen** yang mengalir dari masalah ke rencana solusi. Jika satu koneksi putus, seluruh proposal kehilangan koherensi.

### Integration Map — 6 Koneksi Kritis

```
Problem (Bab 2) → Gap (Bab 3) → RQ & H (Bab 4) → Metrik (Bab 5) → Sistem (Bab 6) → Eksperimen (Bab 7)
```

| Koneksi | Pertanyaan Verifikasi |
|---------|----------------------|
| Problem → Gap | Apakah gap muncul dari analisis literatur terhadap masalah? |
| Gap → RQ | Apakah RQ langsung menjawab gap yang teridentifikasi? |
| RQ → Metrik | Apakah setiap variabel di RQ punya metrik terdefinisi? |
| Metrik → Sistem | Apakah setiap metrik bisa diukur oleh komponen sistem? |
| Sistem → Eksperimen | Apakah desain eksperimen menggunakan sistem sebagai instrumen? |

### Koherensi Vertikal + Horizontal

- **Vertikal** — Alur logis atas-ke-bawah (problem → experiment)
- **Horizontal** — Konsistensi terminologi (nama variabel di RQ = di hipotesis = di metrik = di desain)

### Jebakan Kognitif

| Jebakan | Deskripsi |
|---------|----------|
| "Selling" Introduction | Menulis promosi, bukan menyajikan data dan gap |
| Copy-paste Methodology | Menyalin deskripsi tekstbook tanpa menyesuaikan ke RQ |
| Optimistic Timeline | Meremehkan waktu implementasi; selalu tambah buffer 30-50% |
| No Possibility of Failure | Mengimplikasikan hasil pasti sukses — proposal jujur mengakui H₀ mungkin tidak ditolak |

### Struktur Proposal

1. **Pendahuluan** — Latar belakang + problem statement (Bab 1-2)
2. **Tinjauan Pustaka** — Literature review + gap + baseline (Bab 3)
3. **RQ / Kontribusi / Hipotesis** — (Bab 4)
4. **Metodologi** — Metrik + sistem + desain eksperimen (Bab 5-7)
5. **Timeline & Output**

### Istilah Penting

- **Integration Map** — Diagram 6 koneksi kritis antar komponen proposal
- **Vertical Coherence** — Alur logis atas-ke-bawah
- **Horizontal Coherence** — Konsistensi terminologi di semua bagian
- **Checkpoint** — Titik self-assessment sebelum transisi dari desain ke eksekusi

---

## Template A.8 — Integration Checklist

```
PROPOSAL INTEGRATION CHECKLIST

Koneksi Vertikal (Flow Atas-Bawah):
  [X] Problem → Gap: masalah terdokumentasi di literatur
  [X] Gap → RQ: pertanyaan menjawab gap spesifik
  [X] RQ → Hypothesis: hipotesis memprediksi jawaban
  [X] Hypothesis → Metric: metrik mengukur variabel dalam hipotesis
  [X] Metric → System: komponen sistem menghasilkan/mengukur metrik
  [X] System → Experiment: desain eksperimen menggunakan sistem

Koneksi Horizontal (Konsistensi):
  [X] Istilah sama di semua bagian
  [X] Variabel di RQ = variabel di hipotesis = metrik di desain
  [X] Scope tidak berubah dari masalah ke eksperimen

Rubrik Self-Assessment:
| Kriteria | 1 (Lemah) | 2 (Cukup) | 3 (Baik) | Skor |
|----------|-----------|-----------|----------|------|
| Koherensi |          |           |          |  3   |
| Specificity |        |           |          |  3   |
| Feasibility |        |           |          |  3   |
| Rigor     |          |           |          |  3   |
```

---

## Latihan 1 — Kompilasi Proposal Mini

Kumpulkan hasil dari WS-02 sampai WS-07 menjadi satu ringkasan proposal.

| Komponen | Sumber | Isi (1-2 kalimat) |
|----------|--------|-------------------|
| Problem Statement | WS-02 | Proses identifikasi penyakit daun tanaman padi (seperti Brownspot, Blas, dan HDB) oleh petani saat ini masih dilakukan secara manual, sehingga memakan waktu lama dan rentan terjadi kesalahan diagnosis obat atau dosis pestisida yang memicu kegagalan panen.|
| Gap | WS-03 | Penelitian klasifikasi penyakit padi sebelumnya menggunakan CNN standar sering kali mengalami ketidakstabilan nilai validation loss (overfitting), serta belum menguji pengaruh variasi arsitektur InceptionV3 yang dipadukan dengan manipulasi data augmentasi kecerahan (brightness). |
| RQ | WS-04 | Apakah penerapan arsitektur Deep Learning berbasis arsitektur InceptionV3 dan rekayasa data augmentasi reduksi brightness dapat menstabilkan nilai validation loss sekaligus meningkatkan akurasi klasifikasi citra penyakit daun padi?|
| Hipotesis | WS-04 | H₁: Penerapan model CNN dengan arsitektur InceptionV3 dan optimasi parameter mampu menghasilkan tingkat akurasi pengujian (validation accuracy) lebih dari 97% serta grafik loss yang stabil (bebas overfitting). |
| Variabel & Metrik | WS-05 | IV (Variabel Bebas): Variasi arsitektur CNN (InceptionV3), jumlah epoch, dan tingkat augmentasi kecerahan gambar.


DV (Variabel Terikat): Validation Accuracy (persentase) dan Validation Loss (skala desimal). |
| Sistem | WS-06 |Sistem yang dikembangkan adalah aplikasi berbasis website bernama Padisick yang dibangun menggunakan framework Python/Keras untuk backend klasifikasi citra dan antarmuka web bagi pengguna untuk mengunggah foto daun padi. |
| Desain Eksperimen | WS-07 |Eksperimen dilakukan dengan menguji dataset citra sebanyak 1.630 gambar daun padi yang dibagi dengan partisi data sebesar 75% untuk training dan 25% untuk testing, lalu dioptimasi parameter kodenya menggunakan Keras Tuner. |

---

## Latihan 2 — Integration Checklist

Verifikasi 6 koneksi kritis. Isi dengan merujuk tabel di Latihan 1.

| Koneksi | Status | Bukti |
|---------|--------|-------|
| **Problem → Gap** | ✅ | Gap muncul dari analisis terhadap 10 paper utama di Bab 3 (termasuk Saputra 2021 dan Bari 2021) di mana sebagian besar penelitian deep learning masih berfokus pada akurasi training murni tanpa mencari solusi konkret atas masalah *overfitting* (*validation loss* yang melonjak tinggi). |
| **Gap → RQ** | ✅ | RQ secara eksplisit langsung mempertanyakan solusi atas gap tersebut, yaitu apakah modifikasi arsitektur tingkat lanjut berupa *InceptionV3* dan rekayasa kecerahan gambar (reduksi *brightness*) mampu menstabilkan nilai *validation loss* sekaligus menaikkan *accuracy*. |
| **RQ → Hypothesis** | ✅ | Hipotesis secara presisi memprediksi jawaban dari RQ dengan menargetkan parameter performa berupa grafik *loss* yang melandai secara stabil (bebas dari *overfitting*) serta raihan angka *validation accuracy* yang terukur tinggi (lebih dari 97%). |
| **Hypothesis → Metric** | ✅ | Variabel performa yang ada pada hipotesis diukur secara akurat menggunakan dua metrik komparatif standar kecerdasan buatan, yaitu tingkat *Validation Accuracy* (persentase data benar) dan *Validation Loss* (nilai penalti eror dalam skala desimal). |
| **Metric → System** | ✅ | Komponen *core backend* pada website *Padisick* (yang ditenagai framework Keras dan TensorFlow) dirancang khusus memiliki modul kalkulasi yang mampu mengekstrak, menghitung, dan memproses grafik *accuracy* dan *loss* dari setiap *epoch* jalannya pelatihan model. |
| **System → Experiment** | ✅ | Desain eksperimen menggunakan sistem *Padisick* sebagai instrumen utama, di mana performa sistem diuji langsung lewat skenario pembagian 1.630 data citra (75% data *training* dan 25% data *testing*) dibantu dengan pustaka otomatis *Keras Tuner*. |

**Koneksi mana yang paling lemah?** Koneksi Metric → System.
**Bagaimana cara memperkuatnya?**
> Cara memperkuatnya adalah dengan memastikan bahwa arsitektur backend pada website Padisick tidak hanya sekadar menerima output akhir model, melainkan diintegrasikan dengan modul logging performa atau dashboard visualisasi realtime (seperti TensorBoard). Hal ini penting agar metrik Validation Loss dan Validation Accuracy dari core model Deep Learning (InceptionV3) dapat terekam dan ditampilkan ke antarmuka sistem secara akurat di setiap epoch, tanpa ada risiko kehilangan data (data loss) saat proses testing oleh pengguna berlangsung

**Konsistensi horizontal — apakah istilah dan scope konsisten?** [X] Ya / [ ] Tidak
> Jika tidak, di bagian mana terjadi inkonsistensi? Scope dan istilah sudah konsisten sepenuhnya dari awal sampai akhir. Ruang lingkup penyakit daun padi yang diteliti tetap fokus pada 3 jenis kelas penyakit, yaitu Blas, Hawar Daun Bakteri (HDB), dan Bercak Coklat (Brownspot). Selain itu, terminologi metrik performa yang digunakan pada bab awal secara konsisten diukur menggunakan parameter Validation Accuracy dan Validation Loss hingga ke bab desain eksperimen tanpa mengalami perubahan atau perluasan ruang lingkup riset

---

## Latihan 3 — Rubrik Self-Assessment

Evaluasi proposal mini menggunakan rubrik.

| Kriteria | Skor (1-3) | Justifikasi |
|----------|-----------|-------------|
| **Koherensi** | 3 | Alur proposal mengalir sangat logis dari latar belakang masalah nyata petani hingga solusi berupa pembuatan sistem klasifikasi berbasis website bernama *Padisick*. |
| **Specificity** | 3 | Seluruh metrik dan variabel riset sudah terdefinisi secara numerik dan sangat spesifik, yaitu menggunakan dataset sebanyak 1.630 gambar dengan target akurasi $\ge$ 97%. |
| **Feasibility** | 3 | Tingkat keterlaksanaan riset sangat tinggi karena dataset menggunakan sumber online yang sudah tersedia dan arsitektur model menggunakan InceptionV3 bawaan Google yang efisien. |
| **Rigor** | 3 | Kedalaman metodologi sangat baik karena pengujian tidak hanya melihat akurasi murni, tetapi juga mengevaluasi pengaruh variasi jumlah epoch, ukuran kernel, hingga augmentasi tingkat kecerahan gambar. |

**Skor total:** 12 / 12

**Apakah proposal siap untuk fase eksekusi?** [X] Ya / [ ] Belum
> Jika belum, apa yang perlu diperbaiki? (Proposal sudah siap sepenuhnya untuk masuk ke fase eksekusi karena seluruh kriteria penilaian mandiri telah mencapai skor maksimal, serta jalur integrasi vertikal maupun horizontalnya sudah sinkron dan terbukti kokoh berdasarkan literatur rujukan).

**Skor total:** 12 / 12

**Apakah proposal siap untuk fase eksekusi?** [X] Ya / [ ] Belum
> Jika belum, apa yang perlu diperbaiki? __________________

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-08, bagian mana yang paling mudah dan paling sulit? Mengapa? Apa yang akan dilakukan berbeda jika mengulang dari awal?

**Bagian termudah:** Bagian Pendahuluan dan Problem Statement (WS-01 dan WS-02).
**Bagian tersulit:** Bagian Metodologi, Desain Eksperimen, dan Parameter Tuning (WS-06 dan WS-07).
**Yang akan dilakukan berbeda:**
> Jika mengulang dari awal, saya akan melakukan *literature review* secara lebih terstruktur sejak awal bab. Saya juga akan langsung berfokus pada pencarian *dataset* online yang bervariasi serta mempelajari konfigurasi *hyperparameter* lebih awal agar tidak memakan waktu lama saat menyelaraskan metrik pengujian dengan komponen sistem aplikasinya.

