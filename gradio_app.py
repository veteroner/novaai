import gradio as gr
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import os

# Nova AI Model bilgileri - Teknova'nın özgün modeli
MODEL_NAME = "./nova-ai-model"  # Kendi Nova AI modelinizin yolu
MODEL_PATH = "/content/nova-ai-model"  # Colab için path

# Artık token gerekmiyor - kendi modeliniz
print("🚀 Teknova Nova AI - Özgün model yükleniyor...")
print("💡 Hugging Face token gerektirmez - tamamen özgün!")

# Global değişkenler
model = None
tokenizer = None

def load_model():
    """Teknova Nova AI modelini yükle - Özgün model"""
    global model, tokenizer
    
    print("🚀 Teknova Nova AI modeli yükleniyor...")
    print("🌟 Bu tamamen özgün bir Teknova Nova AI modelidir!")
    
    # Colab için model path kontrolü
    model_path = MODEL_PATH if os.path.exists(MODEL_PATH) else MODEL_NAME
    
    try:
        # Nova AI Tokenizer yükle
        tokenizer = AutoTokenizer.from_pretrained(
            model_path,
            trust_remote_code=True
        )
        
        # Nova AI Model yükle - Teknova optimizasyonu
        model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float16,
            device_map="auto",
            trust_remote_code=True,
            load_in_8bit=True  # Teknova memory optimization
        )
        
        print("✅ Teknova Nova AI modeli başarıyla yüklendi!")
        print("🎉 Özgün Nova AI teknolojisi aktif!")
        return "🚀 Teknova Nova AI hazır! Özgün AI teknolojisiyle sohbet edebilirsiniz."
        
    except Exception as e:
        print(f"❌ Nova AI model yükleme hatası: {e}")
        return f"❌ Hata: {str(e)}\n💡 Nova AI model dosyalarınızı doğru konuma yüklediğinizden emin olun."

def chat_response(message, history):
    """Teknova Nova AI ile sohbet yanıtı üret"""
    global model, tokenizer
    
    if model is None or tokenizer is None:
        return "❌ Teknova Nova AI henüz yüklenmedi. Lütfen model yüklenmesini bekleyin..."
    
    if not message.strip():
        return "❓ Nova AI'ya mesajınızı yazın."
    
    try:
        # Sohbet geçmişini Nova AI formatında hazırla
        conversation = ""
        for user_msg, bot_msg in history:
            conversation += f"Kullanıcı: {user_msg}\nNova AI: {bot_msg}\n"
        
        # Yeni mesajı ekle
        conversation += f"Kullanıcı: {message}\nNova AI:"
        
        # Nova AI Tokenizer ile işle
        inputs = tokenizer(
            conversation, 
            return_tensors="pt", 
            truncation=True, 
            max_length=2048
        ).to(model.device)
        
        # Nova AI yanıt üret - Teknova optimizasyonu
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=512,
                temperature=0.7,
                top_p=0.9,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id,
                eos_token_id=tokenizer.eos_token_id
            )
        
        # Nova AI yanıtını decode et
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Sadece Nova AI'ın yeni yanıtını al
        new_response = response[len(conversation):].strip()
        
        return new_response
        
    except Exception as e:
        return f"❌ Nova AI yanıt üretirken hata: {str(e)}"

# Model yüklemeyi başlat
load_model()

# Gradio arayüzü oluştur
with gr.Blocks(
    theme=gr.themes.Soft(),
    title="Nova AI Chat - Teknova",
    css="""
    .gradio-container {
        max-width: 800px;
        margin: 0 auto;
    }
    .chat-message {
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
    }
    """
) as demo:
    
    gr.HTML("""
    <div style="text-align: center; padding: 20px;">
        <h1 style="background: linear-gradient(135deg, #ff6b6b, #4ecdc4); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.5rem; font-weight: bold;">
            🚀 Teknova Nova AI
        </h1>
        <p style="font-size: 1.2rem; color: #666; margin: 10px 0;">
            <strong>Teknova</strong> tarafından geliştirilen <strong>özgün</strong> yapay zeka modeli
        </p>
        <div style="background: linear-gradient(135deg, #ff6b6b, #4ecdc4); color: white; padding: 8px 16px; border-radius: 20px; display: inline-block; font-size: 0.9rem;">
            ⚡ Özgün Nova AI Teknolojisi • 🧠 Teknova Innovation
        </div>
        <p style="font-size: 0.9rem; color: #888; margin-top: 10px;">
            🌟 Bu tamamen özgün bir Teknova Nova AI modelidir - Token gerektirmez
        </p>
    </div>
    """)
    
    chatbot = gr.Chatbot(
        height=500,
        show_label=False,
        show_share_button=False,
        show_copy_button=True,
        avatar_images=[
            None,  # User avatar
            "🤖"   # Bot avatar
        ]
    )
    
    with gr.Row():
        msg = gr.Textbox(
            placeholder="Nova AI'ya mesajınızı yazın...",
            show_label=False,
            scale=4
        )
        submit = gr.Button("🚀 Gönder", scale=1, variant="primary")
    
    with gr.Row():
        clear = gr.Button("🗑️ Temizle", scale=1)
        
    gr.HTML("""
    <div style="text-align: center; padding: 10px; color: #666;">
        <small>💡 Teknova Nova AI ilk yüklenirken biraz bekleyebilir. Özgün AI teknolojisi ile güçlendirilmiştir.</small>
        <br>
        <small style="color: #ff6b6b;">🚀 <strong>Teknova Nova AI</strong> - Tamamen özgün model teknolojisi</small>
        <br>
        <small style="color: #4ecdc4;">🌟 Hugging Face token gerektirmez - Kendi modeliniz!</small>
    </div>
    """)
    
    # Event handlers
    def user_message(message, history):
        return "", history + [[message, None]]
    
    def bot_message(history):
        user_message = history[-1][0]
        bot_response = chat_response(user_message, history[:-1])
        history[-1][1] = bot_response
        return history
    
    msg.submit(user_message, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot_message, chatbot, chatbot
    )
    submit.click(user_message, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot_message, chatbot, chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True
    ) 