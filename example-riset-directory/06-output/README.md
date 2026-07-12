# 06-output

Hasil olahan data, visualisasi performa model, dan log eksperimen — **Tahap 5** (Analisis Performa Model).

Dihasilkan oleh skrip eksekusi di `05-kode/src/` berdasarkan dataset dari `04-data/`.

## Log Eksperimen (`logs/`)

| File | Isi |
| :--- | :--- |
| `eksperimen-log.md` | Catatan otomatis riwayat parameter training, durasi, dan loss setiap epoch. |

## Visualisasi Data (`figures/`)

| File | Isi |
| :--- | :--- |
| `grafik_akurasi_inception.png` | Kurva pembelajaran (*learning curve*) akurasi training vs validasi untuk arsitektur Inception V3. |
| `hasil_terminal_riset.png` | Tangkapan layar (*screenshot*) bukti eksekusi dan kestabilan training 25 epoch dari terminal. |

## Catatan Tambahan

* **Konvergensi Cepat:** Berdasarkan grafik, model mencapai akurasi maksimal (1.0000) sejak epoch ke-3, menunjukkan efisiensi transfer learning Inception V3 pada dataset penyakit daun padi.
* Data di folder ini digunakan sebagai dasar argumentasi dalam bab pembahasan di dokumen akhir laporan ilmiah.