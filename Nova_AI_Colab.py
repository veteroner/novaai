# 🚀 Teknova Nova AI - Google Colab Özel Scripti
# 🌟 Tamamen özgün Teknova Nova AI modeli
# 💡 Colab'da kendi modelinizi çalıştırın

import gradio as gr
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import os
import zipfile
from google.colab import files

print("🚀 Teknova Nova AI - Google Colab Edition")
print("🌟 Tamamen özgün yapay zeka teknolojisi")
print("=" * 60)

# Colab için Nova AI model yolu
MODEL_PATH = "/content/nova-ai-model"

def upload_and_extract_model():
    """Nova AI modelini Colab'a yükle ve çıkart"""
    print("📂 Nova AI model dosyalarınızı yükleyin...")
    print("💡 ZIP dosyası olarak yüklemeniz önerilir")
    
    # Dosya yükleme
    uploaded = files.upload()
    
    for filename in uploaded.keys():
        print(f"📦 İşleniyor: {filename}")
        
        if filename.endswith('.zip'):
            # ZIP dosyasını çıkart
            with zipfile.ZipFile(filename, 'r') as zip_ref:
                zip_ref.extractall(MODEL_PATH)
            print(f"✅ {filename} başarıyla çıkartıldı")
            os.remove(filename)  # ZIP dosyasını sil
        else:
            # Tek dosyayı model klasörüne taşı
            os.makedirs(MODEL_PATH, exist_ok=True)
            os.rename(filename, os.path.join(MODEL_PATH, filename))
            print(f"✅ {filename} model klasörüne taşındı")
    
    print("🎉 Nova AI model dosyaları hazır!")

def load_nova_ai():
    """Nova AI modelini yükle"""
    print("🚀 Teknova Nova AI modeli yükleniyor...")
    
    if not os.path.exists(MODEL_PATH):
        print("❌ Nova AI model klasörü bulunamadı!")
        print("📤 Önce modelinizi yükleyin...")
        upload_and_extract_model()
    
    try:
        # Nova AI Tokenizer
        tokenizer = AutoTokenizer.from_pretrained(
            MODEL_PATH, 
            trust_remote_code=True
        )
        print("✅ Nova AI Tokenizer yüklendi")
        
        # Nova AI Model - Colab GPU optimizasyonu
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_PATH,
            torch_dtype=torch.float16,
            device_map="auto",
            trust_remote_code=True,
            load_in_8bit=True  # Colab T4 için optimize
        )
        print("✅ Nova AI Model yüklendi")
        print("🎉 Teknova Nova AI hazır!")
        
        return model, tokenizer
    
    except Exception as e:
        print(f"❌ Nova AI yükleme hatası: {e}")
        return None, None

def nova_chat(message, history, model, tokenizer):
    """Nova AI ile sohbet"""
    if model is None or tokenizer is None:
        return "❌ Nova AI modeli yüklenmedi. Lütfen modeli yükleyin."
    
    try:
        # Nova AI konuşma formatı
        conversation = ""
        for user_msg, bot_msg in history:
            conversation += f"Kullanıcı: {user_msg}\nNova AI: {bot_msg}\n"
        
        conversation += f"Kullanıcı: {message}\nNova AI:"
        
        # Nova AI yanıt üret
        inputs = tokenizer(
            conversation, 
            return_tensors="pt", 
            truncation=True, 
            max_length=2048
        ).to(model.device)
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=512,
                temperature=0.7,
                top_p=0.9,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        nova_response = response[len(conversation):].strip()
        
        return nova_response
    
    except Exception as e:
        return f"❌ Nova AI hatası: {str(e)}"

def create_nova_interface():
    """Nova AI Gradio arayüzü oluştur"""
    
    # Nova AI modelini yükle
    model, tokenizer = load_nova_ai()
    
    # Gradio arayüzü
    with gr.Blocks(
        theme=gr.themes.Soft(),
        title="Teknova Nova AI - Colab Edition"
    ) as demo:
        
        gr.HTML("""
        <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #ff6b6b, #4ecdc4); border-radius: 15px; margin-bottom: 20px;">
            <h1 style="color: white; font-size: 2.5rem; margin: 0;">
                🚀 Teknova Nova AI
            </h1>
            <p style="color: white; font-size: 1.2rem; margin: 10px 0;">
                <strong>Google Colab Edition</strong> - Özgün Yapay Zeka
            </p>
            <div style="background: rgba(255,255,255,0.3); padding: 10px; border-radius: 10px; display: inline-block;">
                🌟 Tamamen özgün model • ⚡ Token gerektirmez • 🧠 Colab GPU optimized
            </div>
        </div>
        """)
        
        chatbot = gr.Chatbot(
            height=500,
            show_label=False,
            show_copy_button=True,
            avatar_images=[None, "🤖"]
        )
        
        with gr.Row():
            msg = gr.Textbox(
                placeholder="Nova AI'ya mesajınızı yazın...",
                show_label=False,
                scale=4
            )
            send = gr.Button("🚀 Gönder", scale=1, variant="primary")
        
        with gr.Row():
            clear = gr.Button("🗑️ Temizle")
            reload = gr.Button("🔄 Model Yenile")
        
        gr.HTML("""
        <div style="text-align: center; padding: 15px; background: #f8f9fa; border-radius: 10px; margin-top: 15px;">
            <h3>💡 Nova AI Colab Rehberi</h3>
            <p>🔸 Kendi Nova AI modelinizi ZIP olarak yükleyin</p>
            <p>🔸 Model otomatik olarak /content/nova-ai-model klasörüne çıkartılır</p>
            <p>🔸 T4 GPU ile optimize edilmiş performans</p>
            <p style="color: #ff6b6b; font-weight: bold;">🚀 Teknova Nova AI - Tamamen Özgün</p>
        </div>
        """)
        
        # Event handlers
        def user_message(message, history):
            return "", history + [[message, None]]
        
        def bot_message(history):
            user_message = history[-1][0]
            bot_response = nova_chat(user_message, history[:-1], model, tokenizer)
            history[-1][1] = bot_response
            return history
        
        def reload_model():
            nonlocal model, tokenizer
            model, tokenizer = load_nova_ai()
            return "🔄 Nova AI modeli yeniden yüklendi!"
        
        msg.submit(user_message, [msg, chatbot], [msg, chatbot], queue=False).then(
            bot_message, chatbot, chatbot
        )
        send.click(user_message, [msg, chatbot], [msg, chatbot], queue=False).then(
            bot_message, chatbot, chatbot
        )
        clear.click(lambda: None, None, chatbot, queue=False)
        reload.click(reload_model, None, None)
    
    return demo

# Ana fonksiyon
if __name__ == "__main__":
    print("🎨 Nova AI Colab arayüzü oluşturuluyor...")
    
    demo = create_nova_interface()
    
    print("🌟 Nova AI Colab başlatılıyor...")
    demo.launch(
        share=True,  # Public link oluştur
        debug=True,
        show_error=True,
        server_name="0.0.0.0",
        server_port=7860
    ) 