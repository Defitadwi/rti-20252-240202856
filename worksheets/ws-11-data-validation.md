# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

```
Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data
```

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|-------|----------|-------------------|
| **Accuracy** | Nilai dalam range masuk akal | Akurasi = 1.5 (di luar [0,1]) |
| **Consistency** | Format seragam di semua run | Run 1: CSV, Run 2: JSON |
| **Completeness** | Tidak ada data hilang dari plan | 97 dari 100 run tercatat |
| **Validity** | Data sesuai desain eksperimen | Parameter baseline tercampur treatment |

### Proses Validasi Progresif

1. **Format validation** — Tipe file, header, kolom
2. **Range validation** — Nilai dalam batas logis
3. **Consistency validation** — Format seragam antar-run
4. **Logic validation** — Data cocok dengan desain eksperimen

Jika gagal di langkah awal → tidak perlu lanjut.

### Anomaly Detection — 3 Jenis

| Jenis | Deskripsi | Deteksi |
|-------|----------|---------|
| **Statistical outlier** | Nilai di luar distribusi normal | IQR: < Q1-1.5×IQR atau > Q3+1.5×IQR |
| **Contextual anomaly** | Normal absolut, abnormal dalam konteks | Run 1-10: ~91%, Run 11-20: ~88% |
| **Pattern anomaly** | Pola sistematis (bukan random) | Performa menurun berurutan |

**Prinsip:** Detect → Investigate → Document → Decide — **JANGAN langsung hapus.**

### Engineering vs Research Validation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Data sesuai spesifikasi bisnis | Data layak untuk analisis statistik |
| Missing data | Impute / set default | Investigasi penyebab → dokumentasi |
| Outlier | Bug → fix | Mungkin temuan → investigasi |
| Dokumentasi | Minimal (log error) | Komprehensif (anomali + keputusan) |

### Jebakan Kognitif

1. "Logging otomatis ≠ data benar" → bisa ada bug di logger
2. "Outlier = hapus" → bisa jadi temuan penting
3. "Dataset kecil tidak perlu validasi" → justru lebih rentan
4. "Mean normal = data benar" → [94, 95, 93, **44**, 94] → mean 84% terlihat wajar

---

## Template A.11 — Data Validation Checklist

```
DATA VALIDATION CHECKLIST

Completeness:
  [X] Semua skenario tercakup
  [X] Jumlah run sesuai rencana
  [X] Tidak ada file output hilang
  Missing: ____s dari ____ data points

Format Consistency:
  [X] Semua file format sama (CSV/JSON/...)
  [X] Header konsisten
  [X] Tipe data konsisten (numerik tetap numerik)

Range & Logic:
  [X] Nilai dalam range masuk akal
  [X] Tidak ada waktu negatif
  [X] Metrik 0–100%, tidak di luar range
  Anomali ditemukan: ____________________

Cross-Validation:
  [X] Run identik → hasil mendekati
  [X] Trend konsisten dengan ekspektasi teori

Keputusan:
  [X] Data siap analisis
  [X] Perlu cleaning
  [ ] Perlu re-run (skenario: ____)
```

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul.

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
|----------|-----------------|-------------|---------|--------|
| BERT, DS-1 |10 | 10 |0 | *—* | -
| LSTM, DS-3 | 10 |8 | 2 | *OOM pada run 7 & 9 |
|InceptionV3 (Model AI) | 5 | 5 | 0 |- |
| Pengujian SUS | 35 | 35 | 0 | Semuanya mengisi kuesioner dengan lengkap |

**Total expected:** 40 | **Total actual:** 40 | **Missing:** 0

**Keputusan untuk data missing:**
> Karena tidak ada data yang hilang (missing data = 0), seluruh data point dari log training InceptionV3 dan kuesioner SUS dinyatakan lengkap secara kuantitas dan siap untuk masuk ke tahap investigasi kualitas.
---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Gunakan metode IQR atau z-score.

**Dataset sampel (atau data Anda sendiri):**

| Run | Accuracy (%) |
|-----|-------------|
| 1 | 91.2 |
| 2 | 90.8 |
| 3 | 91.5 |
| 4 | 78.3 |
| 5 | 91.0 |

**Deteksi outlier:**
- Q1 = 90.8| Q3 = 91.2 | IQR = 0.4
- Batas bawah (Q1 - 1.5×IQR) =  90.8 - (1.5x0.4) = 90.2
- Batas atas (Q3 + 1.5×IQR) = 91.2+(1.5x0.4)=91.8
- Outlier terdeteksi: Run 4 (Nilai 78.3) karena nilainya berada jauh di bawah batas bawah toleransi (90.2).

**Investigasi (untuk setiap outlier):**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
|---------|-------|---------------------|-----------|
| Run 4 | 78.3 | Terjadi thermal throttling pada GPU/CPU laptop saat melakukan proses training data citra daun padi secara beruntun. | *Re-run dengan cooling interval* | Melakukan re-run (pelatihan ulang) khusus untuk skenario tersebut dengan memberikan jeda waktu pendinginan perangkat (cooling interval). |

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

**1. Completeness:** 100% data terkumpul
**2. Format:** [X] Konsisten / [ ] Ada inkonsistensi: -
**3. Range check (anomali):** Terdeteksi 1 data outlier pada pengujian performa model (Run 4) dan 2 data anomali pada kuesioner akibat responden tidak konsisten membaca soal selang-seling.
**4. Logic check:** [X] Parameter sesuai plan / [ ] Ada ketidaksesuaian: -

**Kesimpulan:** [ ] Data siap analisis / [X] Perlu tindakan: Melakukan cleaning (pembersihan) dengan membuang data responden kuesioner yang tidak valid, serta melakukan re-run pada proses kodingan model AI yang terkena thermal throttling agar nilai akurasi kembali stabil.

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

> _Data yang benar adalah data yang secara faktual tercatat dan tersimpan apa adanya di dalam sistem (misalnya komputer otomatis mencatat angka akurasi 78.3%). Sedangkan data yang dipercaya (trusted data) adalah data yang tidak hanya benar secara angka, tetapi juga valid secara metodologi ilmiah, bebas dari gangguan luar (seperti gangguan perangkat panas atau responden asal-asalan), serta memiliki akurasi representasi yang kuat terhadap konsep yang diteliti (construct validity).
Proses validasi formal tetap diperlukan meskipun data dikumpulkan secara otomatis karena sistem otomatis hanya bertugas merekam, bukan menganalisis kewajaran konteks. Otomatisasi tidak bisa mendeteksi apakah suatu angka rusak akibat kegagalan perangkat keras keras (hardware glitch), bias algoritma, atau anomali lingkungan luar. Validasi formal dengan metode seperti IQR bertindak sebagai penyaring (filter) ilmiah guna menjamin bahwa kesimpulan riset dibangun di atas data yang bersih dan dapat dipertanggungjawabkan di sidang akademik

