@echo off
chcp 65001 >nul
title Teknova Nova AI - Web Arayüzü
echo.
echo 🚀 ================================
echo    TEKNOVA NOVA AI WEB ARAYÜZÜ
echo    Özgün yapay zeka teknolojisi
echo ================================
echo.
echo 🌟 Bu tamamen özgün bir Teknova Nova AI modelidir!
echo 💡 Hugging Face token gerektirmez - Kendi modeliniz!
echo ⚡ Web arayüzü başlatılıyor...
echo.
echo 📂 Model konumu kontrol ediliyor:
if exist "nova-ai-model" (
    echo ✅ Nova AI model dosyaları bulundu
) else (
    echo ⚠️  Nova AI model dosyaları bulunamadı
    echo 📝 Lütfen nova-ai-model klasörünüze model dosyalarınızı yükleyin
    echo.
)
echo.
echo 🌐 Web arayüzü başlatılıyor...
echo 💻 Tarayıcınızda açılacak adres: http://localhost:8000
echo.
echo ⏹️  Durdurmak için Ctrl+C tuşlayın
echo.

python app.py

echo.
echo 🚀 Teknova Nova AI - Web arayüzü kapatıldı
echo 💡 Tekrar çalıştırmak için bu dosyayı çalıştırın
pause
