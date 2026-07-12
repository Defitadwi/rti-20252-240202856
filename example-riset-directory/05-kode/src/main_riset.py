import os
import matplotlib.pyplot as plt
from preprocessing import load_and_preprocess_data
from model_inception import build_inception_v3_model

def jalankan_eksperimen(epochs=25, split_ratio=0.2):
    print(f"\n=== Memulai Eksperimen (Epoch: {epochs}, Split Rasio Validasi: {split_ratio}) ===")
    
    # Path folder
    dataset_path = "04-data/rice_leaf_diseases_cleaned"
    output_dir = "06-output"
    
    # Membuat folder 06-output jika belum ada
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    if not os.path.exists(dataset_path):
        print(f"Error: Folder dataset di '{dataset_path}' tidak ditemukan!")
        return
    
    # 1. Load Data
    train_data, val_data = load_and_preprocess_data(dataset_path, split_ratio=split_ratio)
    
    # 2. Build Model
    model = build_inception_v3_model(num_classes=3)
    
    # 3. Proses Training
    history = model.fit(
        train_data,
        validation_data=val_data,
        epochs=epochs,
        verbose=1
    )
    
    print("\n=== Eksperimen Selesai, Menyimpan Grafik Performa ke 06-output ===")
    
    # 4. Visualisasi Grafik Performa Model
    plt.figure(figsize=(10, 5))
    plt.plot(history.history['accuracy'], label='Training Accuracy', color='blue', marker='o')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy', color='orange', marker='x')
    
    plt.title('Grafik Perkembangan Akurasi Model Inception V3 (Penyakit Daun Padi)')
    plt.xlabel('Epoch Ke-')
    plt.ylabel('Nilai Akurasi')
    plt.legend()
    plt.grid(True)
    
    # Menyimpan grafik otomatis ke folder 06-output
    path_grafik = os.path.join(output_dir, "grafik_akurasi_inception.png")
    plt.savefig(path_grafik, dpi=300)
    print(f"[Sukses] Grafik berhasil disimpan di: {path_grafik}")
    
    # Menampilkan pop-up gambar
    plt.show()
    
    return history

if __name__ == "__main__":
    jalankan_eksperimen(epochs=25, split_ratio=0.2)