import tensorflow as tf
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam

def build_inception_v3_model(num_classes=3, learning_rate=0.0001):
    """
    Membangun model arsitektur Inception V3 untuk klasifikasi penyakit daun padi.
    """
    # Memuat basis model Inception V3 dengan bobot prapelatihan ImageNet
    base_model = InceptionV3(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    
    # Membekukan layer dasar agar bobot fitur asli tidak rusak
    base_model.trainable = False
    
    # Menambahkan layer kustom untuk klasifikasi penyakit daun padi
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(128, activation='relu')(x)
    predictions = Dense(num_classes, activation='softmax')(x)
    
    # Menggabungkan menjadi satu kesatuan model
    model = Model(inputs=base_model.input, outputs=predictions)
    
    # Kompilasi model
    model.compile(
        optimizer=Adam(learning_rate=learning_rate),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model

if __name__ == "__main__":
    model = build_inception_v3_model()
    model.summary()