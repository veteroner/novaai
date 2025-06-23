---
title: Nova AI Chat
emoji: 🚀
colorFrom: red
colorTo: blue
sdk: gradio
sdk_version: 4.7.1
app_file: gradio_app.py
pinned: false
license: mit
models:
- mistralai/Mistral-7B-Instruct-v0.1
---

# 🚀 Teknova Nova AI - Özgün Yapay Zeka Modeli

**Teknova** tarafından geliştirilen tamamen **özgün** Nova AI yapay zeka modeli.

## 🌟 Özellikler

- 🧠 **Özgün AI Teknolojisi**: Tamamen Teknova tarafından geliştirilmiş
- ⚡ **Token Gerektirmez**: Hugging Face token'a ihtiyaç duymaz
- 🎯 **Özelleştirilebilir**: Kendi modelinizi kullanın
- 🚀 **Hızlı**: GPU optimizasyonu ile hızlı yanıtlar
- 🌐 **Web Arayüzü**: Modern ve kullanıcı dostu
- 💻 **Konsol Modu**: Terminal üzerinden kullanım
- 📱 **API**: RESTful API desteği

## 🏗️ Kurulum

### 1️⃣ Gereksinimleri Yükleyin

```bash
pip install -r requirements.txt
```

### 2️⃣ Nova AI Modelinizi Hazırlayın

```bash
# Kendi Nova AI modelinizi nova-ai-model klasörüne yerleştirin
mkdir nova-ai-model
# Model dosyalarınızı bu klasöre kopyalayın
```

### 3️⃣ Uygulamayı Başlatın

#### 🌐 Web Arayüzü
```bash
# Windows
baslat_api.bat

# Linux/Mac
python app.py
```

#### 💻 Konsol Modu
```bash
# Windows  
baslat_konsol.bat

# Linux/Mac
python main.py
```

#### 🔄 Gradio Arayüzü
```bash
python gradio_app.py
```

## 📂 Dosya Yapısı

```
NovaAI/
├── 🐍 gradio_app.py          # Gradio web arayüzü
├── 🌐 app.py                 # FastAPI web uygulaması  
├── ⚡ api.py                 # API servisi
├── 🖥️ main.py                # Konsol uygulaması
├── 📂 nova-ai-model/         # Nova AI model dosyaları
├── 🚀 baslat_api.bat         # Web başlatıcı
├── 🖱️ baslat_konsol.bat      # Konsol başlatıcı
├── 🔧 download_nova.py       # Model indirme scripti
├── 📋 requirements.txt       # Python paketleri
└── 📄 README.md             # Bu dosya
```

## 🔧 Konfigürasyon

### Model Path Ayarlama

```python
# gradio_app.py içinde
MODEL_NAME = "./nova-ai-model"  # Yerel model
MODEL_PATH = "/content/nova-ai-model"  # Colab için
```

### API Kullanımı

```bash
# POST /chat
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Merhaba Nova AI!"}'
```

## 🎯 Kullanım Senaryoları

- 💬 **Sohbet Botu**: Müşteri hizmetleri
- 📝 **İçerik Üretimi**: Blog yazıları, makaleler
- 🎓 **Eğitim**: Öğrenci asistanı
- 💼 **İş Uygulamaları**: Rapor analizi
- 🔍 **Araştırma**: Bilgi arama ve analiz

## 🌐 Deployment

### Google Colab
```python
# Nova_AI_Chat.ipynb dosyasını Colab'da açın
# Tüm hücreleri çalıştırın
```

### Hugging Face Spaces
```bash
# gradio_app.py dosyasını Space'e yükleyin
# Otomatik deploy edilir
```

### Yerel Sunucu
```bash
python app.py
# http://localhost:8000 adresinde çalışır
```

## 🛡️ Güvenlik

- 🔐 **Veri Güvenliği**: Verileriniz güvende
- 🏠 **Yerel İşlem**: Model yerel olarak çalışır
- 🚫 **Token Gerektirmez**: Harici bağımlılık yok

## 📊 Performans

- ⚡ **Hızlı Yanıt**: 2-5 saniye
- 🧠 **Düşük Bellek**: 8-bit quantization
- 🔥 **GPU Desteği**: CUDA optimizasyonu

## 🤝 Ktkı

Bu proje **Teknova** tarafından geliştirilmiştir.

## 📄 Lisans

Bu proje Teknova'ya aittir. Ticari kullanım için izin gereklidir.

## 🚀 Teknova

**Teknova** - Türkiye'nin öncü yapay zeka teknoloji şirketi

---

🌟 **Tamamen özgün Nova AI teknolojisi ile güçlendirilmiştir**
