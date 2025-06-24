"""
🚀 Nova AI - Hugging Face Spaces
Teknova tarafından geliştirilen özgün yapay zeka modeli
"""

import gradio as gr
import torch
import os
import logging
import time
from typing import List, Tuple

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global variables
model = None
tokenizer = None
device = "cuda" if torch.cuda.is_available() else "cpu"

def load_demo_responses():
    """
    Demo yanıtları - model yokken kullanılacak
    """
    demo_responses = {
        "merhaba": "Merhaba! Ben Nova AI, Teknova'nın özgün yapay zeka teknolojisi. Size nasıl yardımcı olabilirim?",
        "nasılsın": "Ben Nova AI'yım ve harika hissediyorum! Sizinle sohbet etmek için buradayım. Ne konuşmak istersiniz?",
        "nova ai nedir": "Nova AI, Teknova tarafından geliştirilen özgün bir yapay zeka modelidir. Türkçe konuşabilir ve çeşitli konularda yardımcı olabilirim.",
        "teknova": "Teknova, Türkiye'nin öncü yapay zeka teknoloji şirketidir. Özgün AI çözümleri geliştiriyoruz.",
        "yapay zeka": "Yapay zeka, bilgisayarların insan benzeri düşünme ve öğrenme yetenekleri göstermesidir. Ben de bir yapay zeka örneğiyim!",
        "projeler": "Size yenilikçi proje fikirleri önerebilirim: AI chatbot, veri analizi, web uygulaması, mobil uygulama gibi...",
        "gelecek": "Gelecekte yapay zeka, otonom araçlar, akıllı şehirler ve personalize eğitim gibi alanlarda devrim yaratacak!"
    }
    return demo_responses

def generate_demo_response(message: str) -> str:
    """
    Demo yanıt oluştur (model olmadığında)
    """
    message_lower = message.lower().strip()
    demo_responses = load_demo_responses()
    
    # Exact match
    if message_lower in demo_responses:
        return demo_responses[message_lower]
    
    # Partial match
    for key, response in demo_responses.items():
        if key in message_lower:
            return response
    
    # Default responses
    if "?" in message:
        return f"'{message}' hakkında çok ilginç bir soru sordunuz! Nova AI olarak elimden geldiğince yardımcı olmaya çalışırım. Bu konuda daha spesifik sorular sorabilirsiniz."
    
    return f"Nova AI burada! '{message}' konusunda konuşmak güzel. Size nasıl yardımcı olabilirim? Daha detaylı sorular sorabilirsiniz."

def chat_response(message: str, history: List[List[str]], max_length: int, temperature: float) -> Tuple[str, List[List[str]]]:
    """
    Chat response function
    """
    if not message.strip():
        return "", history
    
    # Simulate thinking time
    time.sleep(0.5)
    
    # Generate response
    if model and tokenizer:
        # Gerçek model ile yanıt (model yüklü ise)
        try:
            response = generate_real_response(message, max_length, temperature)
        except Exception as e:
            response = f"Model hatası: {str(e)} - Demo moduna geçiliyor..."
            response += "\n\n" + generate_demo_response(message)
    else:
        # Demo yanıt
        response = generate_demo_response(message)
        response += "\n\n💡 *Not: Bu demo modunda çalışıyor. Gerçek Nova AI modeli yüklendiğinde daha gelişmiş yanıtlar alacaksınız.*"
    
    # Add to history
    history.append([message, response])
    return "", history

def generate_real_response(message: str, max_length: int, temperature: float) -> str:
    """
    Gerçek model ile yanıt oluştur
    """
    if not model or not tokenizer:
        return generate_demo_response(message)
    
    try:
        inputs = tokenizer.encode(message, return_tensors="pt")
        if device == "cuda":
            inputs = inputs.to(device)
        
        with torch.no_grad():
            outputs = model.generate(
                inputs,
                max_length=max_length,
                temperature=temperature,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id,
                no_repeat_ngram_size=3,
                top_p=0.9
            )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        if message in response:
            response = response.replace(message, "").strip()
        
        return response if response else generate_demo_response(message)
        
    except Exception as e:
        logger.error(f"Model generation error: {e}")
        return generate_demo_response(message)

def load_model():
    """
    Model yükleme (opsiyonel)
    """
    global model, tokenizer
    
    try:
        # Model path'leri
        possible_paths = [
            "/data/nova-ai-model",
            "./nova-ai-model", 
            "/app/nova-ai-model"
        ]
        
        model_path = None
        for path in possible_paths:
            if os.path.exists(path):
                model_path = path
                logger.info(f"Model found at: {path}")
                break
        
        if not model_path:
            logger.warning("No model files found - running in demo mode")
            return "🎭 Demo Mode: Model dosyaları bulunamadı, demo yanıtlar kullanılıyor"
        
        from transformers import AutoTokenizer, AutoModelForCausalLM
        
        tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float16 if device == "cuda" else torch.float32,
            device_map="auto" if device == "cuda" else None,
            trust_remote_code=True
        )
        
        logger.info(f"✅ Nova AI model loaded successfully on {device}")
        return f"✅ Nova AI model hazır! ({device})"
        
    except Exception as e:
        logger.error(f"Model loading failed: {e}")
        return f"🎭 Demo Mode: Model yüklenemedi, demo yanıtlar kullanılıyor"

def clear_chat():
    """Clear chat history"""
    return []

# Model yükle (başlangıçta)
initial_status = load_model()

# 🎨 Gradio Interface
def create_interface():
    """
    Nova AI Gradio interface
    """
    
    with gr.Blocks(
        theme=gr.themes.Soft(),
        title="🚀 Teknova Nova AI",
        css="""
        .main-header {
            text-align: center;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }
        .main-header h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .chat-container {
            border-radius: 10px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        }
        .control-panel {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
        }
        .example-buttons {
            margin: 1rem 0;
        }
        .footer {
            text-align: center;
            padding: 2rem;
            background: #f8f9fa;
            border-radius: 10px;
            margin-top: 2rem;
            border: 1px solid #e9ecef;
        }
        """
    ) as demo:
        
        # Header
        gr.HTML("""
        <div class="main-header">
            <h1>🚀 Teknova Nova AI</h1>
            <p style="font-size: 1.2rem; margin-bottom: 0.5rem;">Özgün Yapay Zeka Teknolojisi</p>
            <p style="font-size: 1rem; opacity: 0.9;"><em>Powered by Teknova - Live on Hugging Face Spaces!</em></p>
        </div>
        """)
        
        # Status
        gr.Markdown(f"**🔧 Sistem Durumu:** {initial_status}")
        
        # Main interface
        with gr.Row():
            with gr.Column(scale=3):
                chatbot = gr.Chatbot(
                    label="💬 Nova AI Sohbet",
                    height=450,
                    show_label=True,
                    container=True,
                    elem_classes=["chat-container"],
                    avatar_images=("👤", "🤖")
                )
                
                with gr.Row():
                    msg = gr.Textbox(
                        label="✍️ Mesajınız",
                        placeholder="Nova AI'ye sorunuzu yazın... (Örn: 'Merhaba', 'Yapay zeka nedir?')",
                        lines=2,
                        scale=4,
                        show_label=False
                    )
                    send_btn = gr.Button("📤 Gönder", scale=1, variant="primary", size="lg")
                
                clear_btn = gr.Button("🗑️ Sohbeti Temizle", variant="secondary", size="sm")
                
            with gr.Column(scale=1):
                with gr.Group():
                    gr.Markdown("### ⚙️ Ayarlar")
                    
                    max_length = gr.Slider(
                        minimum=50,
                        maximum=500,
                        value=200,
                        step=25,
                        label="📏 Maksimum Uzunluk",
                        info="Yanıtın ne kadar uzun olacağını belirler"
                    )
                    
                    temperature = gr.Slider(
                        minimum=0.1,
                        maximum=1.2,
                        value=0.7,
                        step=0.1,
                        label="🎨 Yaratıcılık (Temperature)",
                        info="Düşük: tutarlı, Yüksek: yaratıcı"
                    )
                
                with gr.Group():
                    gr.Markdown("### 💡 Bilgi")
                    gr.Markdown("""
                    **Nova AI Özellikleri:**
                    - 🧠 Gelişmiş dil anlama
                    - 💬 Doğal konuşma
                    - 🌍 Türkçe optimizasyonu
                    - ⚡ Hızlı yanıt
                    """)
        
        # Example questions
        gr.Markdown("### 💬 Örnek Sorular")
        with gr.Row(elem_classes=["example-buttons"]):
            example_buttons = [
                gr.Button("👋 Merhaba Nova AI!", size="sm", variant="secondary"),
                gr.Button("🤖 Yapay zeka nedir?", size="sm", variant="secondary"), 
                gr.Button("🚀 Teknova hakkında bilgi", size="sm", variant="secondary"),
                gr.Button("💡 Proje fikirleri öner", size="sm", variant="secondary")
            ]
        
        # Event handlers
        send_btn.click(
            chat_response,
            inputs=[msg, chatbot, max_length, temperature],
            outputs=[msg, chatbot],
            show_progress=True
        )
        
        msg.submit(
            chat_response,
            inputs=[msg, chatbot, max_length, temperature],  
            outputs=[msg, chatbot],
            show_progress=True
        )
        
        clear_btn.click(clear_chat, outputs=chatbot)
        
        # Example button handlers
        example_buttons[0].click(lambda: "Merhaba Nova AI!", outputs=msg)
        example_buttons[1].click(lambda: "Yapay zeka nedir?", outputs=msg)
        example_buttons[2].click(lambda: "Teknova hakkında bilgi ver", outputs=msg)
        example_buttons[3].click(lambda: "Bana yenilikçi proje fikirleri öner", outputs=msg)
        
        # Footer
        gr.HTML("""
        <div class="footer">
            <h3>🚀 Teknova Nova AI</h3>
            <p><strong>Özgün yapay zeka teknolojisi</strong></p>
            <p>
                <a href="https://github.com/veteroner/novaai" target="_blank" style="margin: 0 10px;">📂 GitHub</a> |
                <a href="https://huggingface.co/spaces/veteroner/NovaAI" target="_blank" style="margin: 0 10px;">🤗 HF Spaces</a> |
                <a href="mailto:teknova@example.com" style="margin: 0 10px;">📧 İletişim</a>
            </p>
            <p style="margin-top: 1rem; font-size: 0.9rem; color: #666;">
                <em>Made with ❤️ by Teknova | Powered by Hugging Face Spaces</em>
            </p>
        </div>
        """)
    
    return demo

# Create and launch
if __name__ == "__main__":
    demo = create_interface()
    demo.queue(max_size=20, default_concurrency_limit=5)
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True,
        debug=False
    ) 