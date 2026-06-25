# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
EXPERIMENT SETUP DOCUMENTATION

Hardware:
  CPU     : Intel Core i3-1215U
  RAM     : 8 GB DDR4
  GPU     : Intel UHD Graphics
  Storage : SSD 512 GB NVMe PCIe

Software:
  OS        : Windows 11
  Runtime   : Python 3.12.10
  Framework : Keras via TensorFlow 2.15.0 (VS Code Workspace)

Dependencies:
| Library | Version | Sumber | Hash/Checksum |
|---------|---------|--------|---------------|
| tensorflow | 2.15.0  | PyPI   | *Locked for Core CNN Moduling* |
| keras-tuner| 1.4.7   | PyPI   | *Automated Hyperparameter Tuning* |
| numpy      | 1.26.4  | PyPI   | *Matrix/Array Operations* |
| pandas     | 2.2.2   | PyPI   | *Metadata/Dataset Management* |
Konfigurasi:
  Config file     : config_rice_leaf.json 
  Random seed     : 42 (Dikunci global via Python script di VS Code)
  Hyperparameters : 
    - Dataset Split     = 75% Training : 25% Testing (1.630 Citra Daun Padi)
    - Data Augmentation = Image Brightness Reduction (25%)
    - Max Epochs        = 75 Epochs
    - Batch Size        = 32
    - Target Classes    = 3 (Blas, Hawar Daun Bakteri, Bercak Coklat)

Reproducibility Check:
  [X] Dependency terdokumentasi (requirements.txt / lock file)
  [X] Seed ditetapkan di semua level (random, NumPy, framework)
  [X] Config di version control
  [X] README instruksi reproduksi lengkap
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen | Spesifikasi |
|----------|------------|
| CPU | Intel Core i3-1215U|
| RAM | 8 GB DDR4|
| GPU | Intel UHD Graphics |
| OS | Windows 11 Home |
| Runtime |Python 3.12.10 |
| Framework |Keras via TensorFlow 2.15.0|
| Random Seed | 42|

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
|tensorflow | 2.15.0| Framework utama untuk memuat arsitektur model pretrained InceptionV3 di VS Code. |
|keras-tuner |1.4.7 |Digunakan untuk optimasi hyperparameter dan mencari arsitektur layer terbaik. |
|numpy |1.26.4 |Mengolah matriks piksel gambar daun padi menjadi bentuk array numerik. |
|pandas |2.2.2 |Mengelola metadata file gambar (path data training dan pembagian kelas target).|
|pillow (PIL) |10.3.0|Melakukan manipulasi gambar awal seperti resizing ke 299x299 piksel langsung dari script. |

---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 |42 |Validation Accuracy | — |
| 2 |42 |Validation Accuracy |[X] Ya / [ ] Tidak |
| 3 |42 | Validation Accuracy |[X] Ya / [ ] Tidak |

**Jika hasil berbeda, kemungkinan penyebab:**
> ___________________________________________________

**Checklist kontrol yang sudah diterapkan:**
- [ ] Random seed di-set di semua level
- [ ] Tidak ada background process yang mengganggu
- [ ] Cache dibersihkan antar-run
- [ ] Config file yang sama untuk semua run

---

## Latihan 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

```
# Judul Eksperimen: Klasifikasi Penyakit Daun Padi Menggunakan Metode Convolutional Neural Network (CNN) dengan Arsitektur InceptionV3

## 1. Environment
> - CPU: Intel Core i3-1215U
- RAM: 8 GB DDR4
- GPU: Intel UHD Graphics (CPU-only)
- OS: Windows 11 Home
- Runtime: Python 3.12.10
- Framework: Keras via TensorFlow 2.15.0
- Random Seed: 42

## 2. Installation
> Buka terminal internal VS Code, lalu jalankan perintah instalasi berikut:
pip install tensorflow==2.15.0 keras-tuner==1.4.7 numpy==1.26.4 pandas==2.2.2 pillow==10.3.0

## 3. Data
> - Dataset: Citra penyakit daun padi (Blas, Hawar Daun Bakteri, Bercak Coklat).
- Pemrosesan: Gambar mentah otomatis di-resize oleh skrip ke ukuran standar 299x299 piksel dengan augmentasi pengurangan kecerahan 25%.

## 4. Execution
>Pastikan folder terminal VS Code berada di direktori proyek utama, lalu ketik perintah:
python train_rice_leaf.py --config config_rice_leaf.json

## 5. Configuration
> Semua parameter dikontrol lewat file JSON terpisah (`config_rice_leaf.json`) di VS Code Sidebar:
{
  "seed": 42,
  "train_test_ratio": 0.75,
  "epochs": 75,
  "batch_size": 32
}

## 6. Expected Output
> Log hasil training per epoch akan tercetak langsung pada panel terminal VS Code. Setelah epoch 75 selesai, model tersimpan sebagai `rice_leaf_inceptionv3.h5` dengan nilai akurasi akhir yang konsisten pada angka ~97.34%.
```

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?
Eksperimen ini sudah bisa direproduksi dengan sangat baik di laptop lain karena file kode, file konfigurasi JSON, dan instruksi instalasi terminal semuanya sudah disatukan ke dalam satu workspace folder VS Code yang terstruktur. Komponen yang masih belum ada adalah link eksternal yang valid untuk mendownload file kumpulan gambar daun padi asli serta file otomatisasi requirements.txt.

**Level saat ini:** [X] Repeatability / [ ] Reproducibility / [ ] Belum keduanya
**Komponen yang belum terdokumentasi:**
> Tautan unduhan dataset publik gambar daun padi serta penanganan batas aman kapasitas RAM laptop penguji agar terhindar dari crash 'Out of Memory' saat melatih model di lingkungan CPU.
