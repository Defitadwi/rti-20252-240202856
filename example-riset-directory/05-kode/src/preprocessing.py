import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def load_and_preprocess_data(dataset_dir, batch_size=32, split_ratio=0.2):
    """
    Membuat generator data citra daun padi dengan normalisasi.
    Menggunakan generator terpisah tanpa validation_split internal Keras 
    agar tidak memicu ValueError pada jumlah dummy data yang sedikit.
    """
    # Generator untuk training (dengan augmentasi ringan)
    train_datagen = ImageDataGenerator(
        rescale=1.0/255,
        rotation_range=20,
        zoom_range=0.15,
        horizontal_flip=True
    )
    
    # Generator untuk validasi (hanya normalisasi piksel)
    val_datagen = ImageDataGenerator(rescale=1.0/255)
    
    # Ambil data langsung dari folder utama
    train_generator = train_datagen.flow_from_directory(
        dataset_dir,
        target_size=(224, 224),
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=True
    )
    
    val_generator = val_datagen.flow_from_directory(
        dataset_dir,
        target_size=(224, 224),
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=False
    )
    
    return train_generator, val_generator

if __name__ == "__main__":
    print("Modul Preprocessing Citra Daun Padi (Mode Simulasi) Siap.")