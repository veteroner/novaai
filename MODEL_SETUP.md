# 🚀 Nova AI Model Kurulum Rehberi

## 📂 Model Dosyalarını Hazırlama

Model dosyaları GitHub'a yüklenemez (çok büyük). İki seçeneğiniz var:

### 🔥 Seçenek 1: Yerel Model Klasörü Oluşturma

```bash
# 1. Nova AI model klasörünü oluşturun
mkdir nova-ai-model

# 2. Model dosyalarınızı bu klasöre kopyalayın:
nova-ai-model/
├── config.json
├── tokenizer.json
├── tokenizer.model
├── tokenizer_config.json
├── special_tokens_map.json
├── generation_config.json
├── pytorch_model.bin (veya .safetensors dosyaları)
└── model.safetensors.index.json
```

### 🌐 Seçenek 2: Hugging Face'den İndirme

```python
# download_mistral.py dosyasını düzenleyin:
MODEL_NAME = "your-username/your-nova-ai-model"  # Kendi modeliniz
LOCAL_DIR = "nova-ai-model"

# Sonra çalıştırın:
python download_mistral.py
```

### 📱 Seçenek 3: Google Colab

```python
# Nova_AI_Colab.py dosyasını kullanın
# Model dosyalarınızı ZIP olarak yükleyin
# Otomatik olarak /content/nova-ai-model'e çıkartılır
```

## 🔧 Kurulum Tamamlandıktan Sonra

```bash
# Web arayüzünü başlatın
python app.py

# Veya Gradio arayüzünü
python gradio_app.py

# Veya konsol modunu
python main.py
```

## 🎯 Model Dosya Formatları

Nova AI şu formatları destekler:
- ✅ PyTorch (.bin)
- ✅ SafeTensors (.safetensors)
- ✅ Hugging Face format
- ✅ Transformers uyumlu

## 💡 İpuçları

- 🔸 Model dosyaları toplam ~13GB boyutunda
- 🔸 SSD'de saklayın (daha hızlı)
- 🔸 GPU için CUDA kurulu olmalı
- 🔸 En az 16GB RAM önerili

## 🚀 Teknova Nova AI

Model dosyalarınızı hazırladıktan sonra Nova AI tamamen çalışır durumda olacak!

---

**Not:** Bu repository kod dosyalarını içerir. Model dosyalarını ayrıca indirmeniz gerekir. 