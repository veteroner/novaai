@echo off
chcp 65001 >nul
title Teknova Nova AI - Konsol Uygulaması
echo.
echo 🚀 ===================================
echo    TEKNOVA NOVA AI KONSOL UYGULAMASI
echo    Özgün yapay zeka teknolojisi
echo ===================================
echo.
echo 🌟 Bu tamamen özgün bir Teknova Nova AI modelidir!
echo 💡 Hugging Face token gerektirmez - Kendi modeliniz!
echo 🖥️  Konsol uygulaması başlatılıyor...
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
echo 💬 Nova AI ile sohbet başlatılıyor...
echo 🔤 Mesajınızı yazıp Enter tuşuna basın
echo ⏹️  Çıkmak için 'exit' yazın
echo.

python main.py

echo.
echo 🚀 Teknova Nova AI - Konsol uygulaması kapatıldı
echo 💡 Tekrar çalıştırmak için bu dosyayı çalıştırın
pause 