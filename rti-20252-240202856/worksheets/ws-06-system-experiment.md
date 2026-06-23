# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

```
SYSTEM-EXPERIMENT MAPPING

Research Question: Sejauh mana peningkatan jumlah epoch (10, 20, 30) memengaruhi akurasi klasifikasi penyakit padi menggunakan arsitektur InceptionV3?

Variable → Component Mapping:
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi/Pengukuran |
|----------|------|-----------------|---------------------------|
|Jumlah Epoch          | IV   | Training Configuration Module                |Mengubah nilai parameter epochs di dalam skrip pelatihan (10, 20, 30)                           |
|Akurasi & Loss          | DV   |Evaluation & Logger Module                 |Menghasilkan nilai Accuracy dan Categorical Crossentropy setiap iterasi selesai                           |
|Model InceptionV3          | CV   |Feature Extraction Module                 |Mengunci arsitektur model agar tidak berubah selama eksperimen berlangsung                           |

4 Prinsip Desain:
  [X] Traceability — Setiap modul (pelatihan, ekstraksi, evaluasi) melayani variabel tertentu
  [X] Variable Isolation — Nilai epoch dapat diubah tanpa memengaruhi struktur model atau dataset.
  [X] Measurement Integration — Sistem otomatis mencatat log akurasi ke dalam file CSV/Grafik.
  [X] Reproducibility — Seluruh parameter pelatihan disimpan dalam file konfigurasi.

Experimental Setup:
  Input data     : 1.500 citra daun padi (Blas, Brownspot, HDB).
  Parameter      : Learning rate tetap, Batch size tetap, InceptionV3.
  Output format  : Confusion Matrix, Grafik Akurasi/Loss, dan Tabel Hasil.
```

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Apakah variasi epoch meningkatkan akurasi deteksi penyakit padi pada model InceptionV3?

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
| Iterasi Pelatihan| IV | Trainer Engine | Toggle jumlah iterasi pada config file. |
| Performa Model | DV |Auto-logging akurasi per epoch.| |
|Arsitektur Model | CV |Core Model (InceptionV3) |Hardcoded atau dikunci pada satu tipe model.   |

**Apakah semua variabel bisa di-map?** [X] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? ya

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| Traceability | *Contoh: ✅ — setiap modul punya label variabel* |Komponen pelatihan terhubung langsung ke variabel Independent (Epoch). |
| Modularity |✅ |Modul Preprocessing terpisah dari modul Training, memudahkan isolasi variabel. |
| Controllability |✅ |Parameter epoch dieksternalisasi, bukan ditanam di dalam kode inti. |
| Measurability |✅ |Sistem secara otomatis menghitung Confusion Matrix di akhir pengujian. |

**Prinsip mana yang paling sulit dipenuhi?** 
**Strategi untuk mengatasinya:**
> Menggunakan file konfigurasi .yaml atau .json untuk menyimpan semua parameter eksperimen agar tidak ada yang tersembunyi di dalam kode program.

---

## Latihan 3 — Ablation Study Planning

Jika sistem memiliki 3 komponen utama, rencanakan ablation study.

| Kondisi | Komponen A | Komponen B | Komponen C | Hasil yang Diharapkan |
|---------|-----------|-----------|-----------|----------------------|
| Full | ✅ InceptionV3 |✅ Augmentasi Citra | ✅ Resizing & Normalization | Baseline Penuh: Akurasi maksimal (target ~93%).|
| – A | ❌ (Ganti VGG16) | ✅ | ✅ |Performa berubah; menguji efektivitas ekstraksi fitur InceptionV3 dibanding baseline lain. |
| – B | ✅ | ❌ (tanpa temporal) | ✅ |Akurasi diprediksi menurun drastis dan model cenderung overfitting pada dataset terbatas. |
| – C | ✅ | ✅ | ❌ (tanpa normalisasi) |Proses konvergensi (pelatihan) menjadi lebih lambat dan tidak stabil. |

**Komponen mana yang diprediksi paling berkontribusi?** Komponen A (Arsitektur InceptionV3)
**Mengapa?**
> Karena arsitektur model bertindak sebagai instrumen utama dalam melakukan ekstraksi fitur hierarki dari citra daun padi. Tanpa arsitektur yang tepat (seperti Inception modules yang menangkap fitur pada berbagai skala), komponen pendukung seperti augmentasi atau normalisasi tidak akan mampu menghasilkan representasi data yang cukup kuat untuk membedakan kelas penyakit yang mirip secara visual, seperti Blas dan Brownspot. Arsitektur adalah variabel kontrol (CV) utama yang memastikan bahwa Independent Variable (Epoch) dapat bekerja secara optimal.

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Risiko utama jika sistem dibangun seperti produk monolitik dengan fitur lengkap sebelum eksperimen dilakukan adalah terjadinya kerancuan variabel (confounding variables), di mana fitur-fitur tambahan yang tidak relevan dengan pertanyaan riset justru menimbulkan noise yang mengaburkan hasil pengujian utama. Dalam sistem yang monolitik, peneliti akan kesulitan melakukan isolasi variabel, sehingga jika terjadi kegagalan atau penurunan performa, peneliti tidak dapat memastikan apakah hal tersebut disebabkan oleh algoritma inti atau oleh komponen pendukung lainnya.
> Arsitektur modular sangat penting untuk riset karena memungkinkan peneliti untuk melakukan Variable Isolation, yaitu mengubah satu variabel independen secara spesifik sambil memastikan variabel kontrol lainnya tetap konstan. Modularitas memfasilitasi teknik seperti Ablation Study, di mana kontribusi tiap komponen dapat diuji secara terpisah dengan cara melepas atau menggantinya tanpa harus merombak seluruh kode program. Hal ini menjamin aspek Traceability (keterlacakan) dan Reproducibility (kemampuan pengulangan), yang merupakan syarat mutlak bagi sebuah eksperimen ilmiah yang valid.
