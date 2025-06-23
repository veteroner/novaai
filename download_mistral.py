# Teknova Nova AI Model İndirme Scripti
# Bu script kendi Nova AI modelinizi yerel klasöre indirir
from huggingface_hub import snapshot_download
import os

# Nova AI Model bilgileri - Kendi modeliniz
MODEL_NAME = "your-username/nova-ai-model"  # Kendi Hugging Face model adresinizi yazın
LOCAL_DIR = "nova-ai-model"

print("🚀 Teknova Nova AI Model İndirme Scripti")
print("🌟 Bu script kendi Nova AI modelinizi indirir")
print("=" * 60)

if __name__ == "__main__":
    print(f"📦 Nova AI modeli indiriliyor: {MODEL_NAME}")
    print(f"📂 Hedef klasör: {LOCAL_DIR}")
    print("💡 Bu işlem biraz zaman alabilir...")
    
    try:
        # Nova AI modelinizi indirin
        snapshot_download(
            repo_id=MODEL_NAME, 
            local_dir=LOCAL_DIR, 
            local_dir_use_symlinks=False
        )
        print(f"✅ Nova AI modeli '{MODEL_NAME}' başarıyla '{LOCAL_DIR}' klasörüne indirildi!")
        print("🎉 Artık Nova AI uygulamanızı çalıştırabilirsiniz!")
        
    except Exception as e:
        print(f"❌ Nova AI model indirme hatası: {e}")
        print("\n💡 Çözüm önerileri:")
        print("1. MODEL_NAME değişkenini kendi model adresinizle değiştirin")
        print("2. Hugging Face token'ınızı ayarlayın (gerekirse)")
        print("3. İnternet bağlantınızı kontrol edin")
        print("4. Model adresinin doğru olduğundan emin olun")
        
    print("\n🚀 Teknova Nova AI ile güçlendirilmiştir!")
    input("Press Enter to continue...")
