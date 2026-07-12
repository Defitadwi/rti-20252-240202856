# 04-data

Repositori dataset mentah dan data hasil pembersihan (*preprocessing*) — input utama untuk **Tahap 4 (Pemodelan Deep Learning)**.

## Isi Berkas (Dataset)

* `rice_leaf_diseases_raw/` : Folder berisi citra digital asli penyakit daun padi yang belum diolah (format `.jpg` / `.png`).
* `rice_leaf_diseases_cleaned/` : Hasil *preprocessing* (proses *Image Resizing* menjadi 224×224 piksel, normalisasi nilai piksel, serta pembagian data) yang siap diumpankan ke dalam model arsitektur Inception V3.

## Metrik Metadata Data

* **Sumber Data**: Dataset publik penyakit tanaman padi (*Rice Leaf Diseases Dataset*).
* **Format**: Citra Digital / Gambar Terkompresi (`.jpg` / `.png`) dan berkas log log pelatihan (`.csv` / `.json`).
* **Struktur Label**:
    * `0` : Bacterial Leaf Blight (Hawar Daun Bakteri)
    * `1` : Brown Spot (Bercak Cokelat)
    * `2` : Leaf Smut (Gosong Palsu)