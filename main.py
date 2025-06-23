from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

def load_nova_model():
    """Teknova Nova AI modelini yükle - Özgün model"""
    # Nova AI model path
    model_path = "./nova-ai-model"  # Yerel Nova AI model
    colab_path = "/content/nova-ai-model"  # Colab için path
    
    # Path kontrolü
    actual_path = colab_path if os.path.exists(colab_path) else model_path
    
    print("🚀 Teknova Nova AI konsol uygulaması başlatılıyor...")
    print("🌟 Bu tamamen özgün bir Teknova Nova AI modelidir!")
    print("💡 Hugging Face token gerektirmez - kendi modeliniz!")
    
    try:
        tokenizer = AutoTokenizer.from_pretrained(actual_path, trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(
            actual_path, 
            torch_dtype=torch.float16, 
            device_map="auto",
            trust_remote_code=True
        )
        print("✅ Teknova Nova AI konsol uygulaması hazır!")
        print("🎉 Özgün Nova AI teknolojisi aktif!")
        return model, tokenizer
    except Exception as e:
        print(f"❌ Nova AI model yükleme hatası: {e}")
        print("💡 Nova AI model dosyalarınızı doğru konuma yüklediğinizden emin olun.")
        return None, None

def generate_text(prompt, model, tokenizer, max_new_tokens=128):
    """Nova AI ile metin üret"""
    # Nova AI konuşma formatı
    conversation = f"Kullanıcı: {prompt}\nNova AI:"
    
    inputs = tokenizer(conversation, return_tensors="pt").to(model.device)
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs, 
            max_new_tokens=max_new_tokens,
            temperature=0.7,
            top_p=0.9,
            do_sample=True
        )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    nova_response = response[len(conversation):].strip()
    return nova_response

def main():
    """Teknova Nova AI konsol uygulaması"""
    print("=" * 60)
    print("🚀 TEKNOVA NOVA AI - KONSOL UYGULAMASI")
    print("🌟 Özgün yapay zeka teknolojisi")
    print("💡 Token gerektirmez - Tamamen özgün model")
    print("=" * 60)
    
    # Nova AI modelini yükle
    model, tokenizer = load_nova_model()
    
    if model is None or tokenizer is None:
        print("❌ Nova AI modeli yüklenemedi. Program sonlandırılıyor.")
        return
    
    print("\n🎉 Nova AI sohbet moduna geçiliyor...")
    print("💬 Mesajınızı yazın (çıkmak için 'exit' yazın)")
    print("-" * 60)
    
    while True:
        try:
            user_input = input("\n👤 Siz: ")
            
            if user_input.lower() in ['exit', 'çıkış', 'quit', 'q']:
                print("\n🚀 Teknova Nova AI - Görüşmek üzere!")
                break
            
            if not user_input.strip():
                print("🤖 Nova AI: Lütfen bir mesaj yazın.")
                continue
            
            print("🤖 Nova AI düşünüyor...")
            output = generate_text(user_input, model, tokenizer)
            print(f"🤖 Nova AI: {output}")
            
        except KeyboardInterrupt:
            print("\n\n🚀 Teknova Nova AI - Program sonlandırıldı!")
            break
        except Exception as e:
            print(f"❌ Hata: {e}")

if __name__ == "__main__":
    main()
