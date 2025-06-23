@echo off
chcp 65001 >nul
echo.
echo 🚀 ========================
echo    Nova AI Token Kurulumu
echo    by Teknova
echo ========================
echo.

echo 📝 Hugging Face Token alma adımları:
echo.
echo 1️⃣ Tarayıcınızda şu adresi açın:
echo    👉 https://huggingface.co/settings/tokens
echo.
echo 2️⃣ "New token" butonuna tıklayın
echo.
echo 3️⃣ Token bilgilerini doldurun:
echo    📛 Name: NovaAI-Token
echo    🔑 Role: Read
echo.
echo 4️⃣ "Generate a token" tıklayın
echo.
echo 5️⃣ Token'ı kopyalayın (hf_xxx... ile başlar)
echo.
echo 🔧 Token'ı nasıl kullanacağınız:
echo.
echo   💻 Seçenek 1 - Environment Variable:
echo      set HF_TOKEN=hf_xxxxxxxxxxxxxxxxxx
echo.
echo   📝 Seçenek 2 - Kod içinde:
echo      gradio_app.py dosyasındaki ilgili satırı düzenleyin
echo.
echo ⚡ EN KOLAY: Yerel model kullanın (token gerekmez!)
echo    ✅ Tüm dosyalar zaten düzenlendi
echo.
echo 🚀 Nova AI başlatmak için:
echo    👉 baslat_api.bat (Web arayüzü)
echo    👉 baslat_konsol.bat (Konsol)
echo.
echo 💡 Teknova ile güçlendirilmiştir
echo.
pause 