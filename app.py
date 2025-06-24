"""
🚀 Teknova Nova AI - Hugging Face Spaces
Özgün yapay zeka teknolojisi - Hugging Face Spaces deployment
"""

import gradio as gr
import torch
import os
import logging
from typing import List, Tuple, Optional
import time

# Logging ayarları
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global değişkenler
model = None
tokenizer = None
device = "cuda" if torch.cuda.is_available() else "cpu"

def load_model():
    """
    Nova AI modelini yükle
    Hugging Face Spaces için optimize edilmiş
    """
    global model, tokenizer
    
    try:
        # Hugging Face Spaces'te model path'leri
        model_paths = [
            "/data/nova-ai-model",  # HF Spaces persistent storage
            "./nova-ai-model",      # Local path
            "/content/nova-ai-model"  # Colab fallback
        ]
        
        model_path = None
        for path in model_paths:
            if os.path.exists(path):
                model_path = path
                break
        
        if not model_path:
            logger.warning("⚠️ Model dosyaları bulunamadı")
            return "Model dosyaları yüklenmedi"
        
        logger.info(f"📂 Model yükleniyor: {model_path}")
        
        # HF Transformers ile model yükleme
        from transformers import AutoTokenizer, AutoModelForCausalLM
        
        tokenizer = AutoTokenizer.from_pretrained(
            model_path,
            trust_remote_code=True,
            use_fast=True
        )
        
        model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float16 if device == "cuda" else torch.float32,
            device_map="auto" if device == "cuda" else None,
            trust_remote_code=True,
            low_cpu_mem_usage=True
        )
        
        logger.info(f"✅ Nova AI model başarıyla yüklendi! ({device})")
        return f"Nova AI model hazır! 🚀 ({device})"
        
    except Exception as e:
        error_msg = f"❌ Model yükleme hatası: {str(e)}"
        logger.error(error_msg)
        return error_msg

def generate_response(prompt: str, max_length: int = 512, temperature: float = 0.7) -> str:
    """
    Nova AI ile yanıt oluştur
    """
    if not model or not tokenizer:
        return "⚠️ Model henüz yüklenmedi. Lütfen bekleyin..."
    
    try:
        # Input tokenize
        inputs = tokenizer.encode(prompt, return_tensors="pt")
        if device == "cuda":
            inputs = inputs.to(device)
        
        # Generate
        with torch.no_grad():
            outputs = model.generate(
                inputs,
                max_length=max_length,
                temperature=temperature,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id,
                no_repeat_ngram_size=3,
                top_p=0.9,
                top_k=50
            )
        
        # Decode
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Remove input from response
        if prompt in response:
            response = response.replace(prompt, "").strip()
        
        return response if response else "Nova AI şu anda yanıt üretemiyor."
        
    except Exception as e:
        logger.error(f"Generation error: {e}")
        return f"❌ Yanıt oluşturma hatası: {str(e)}"

def chat_response(message: str, history: List[List[str]], max_length: int, temperature: float) -> Tuple[str, List[List[str]]]:
    """
    Sohbet yanıtı oluştur
    """
    if not message.strip():
        return "", history
    
    # Nova AI yanıtı oluştur
    bot_response = generate_response(message, max_length, temperature)
    
    # History'e ekle
    history.append([message, bot_response])
    
    return "", history

def clear_chat():
    """
    Sohbet geçmişini temizle
    """
    return []

# Model yükleme (başlangıçta)
initial_status = load_model()

# 🎨 Gradio Arayüzü
def create_interface():
    """
    Hugging Face Spaces için Gradio arayüzü
    """
    
    with gr.Blocks(
        theme=gr.themes.Soft(),
        title="🚀 Teknova Nova AI",
        css="""
        .main-header {
            text-align: center;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        .chat-container {
            max-height: 500px;
            overflow-y: auto;
        }
        .control-panel {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        }
        """
    ) as demo:
        
        # Ana başlık
        gr.HTML("""
        <div class="main-header">
            <h1>🚀 Teknova Nova AI</h1>
            <p>Özgün Yapay Zeka Teknolojisi</p>
            <p><em>Powered by Teknova - Hugging Face Spaces'te!</em></p>
        </div>
        """)
        
        # Model durumu
        gr.Markdown(f"**Model Durumu:** {initial_status}")
        
        # Ana sohbet arayüzü
        with gr.Row():
            with gr.Column(scale=4):
                chatbot = gr.Chatbot(
                    label="Nova AI Sohbet",
                    height=400,
                    container=True,
                    elem_classes=["chat-container"]
                )
                
                with gr.Row():
                    msg = gr.Textbox(
                        label="Mesajınız",
                        placeholder="Nova AI'ye sorunuzu yazın...",
                        lines=2,
                        scale=4
                    )
                    send_btn = gr.Button("📤 Gönder", scale=1, variant="primary")
                
                clear_btn = gr.Button("🗑️ Temizle", variant="secondary")
                
            with gr.Column(scale=1):
                gr.Markdown("### ⚙️ Ayarlar")
                
                max_length = gr.Slider(
                    minimum=50,
                    maximum=1000,
                    value=512,
                    step=50,
                    label="Maksimum Uzunluk"
                )
                
                temperature = gr.Slider(
                    minimum=0.1,
                    maximum=1.5,
                    value=0.7,
                    step=0.1,
                    label="Yaratıcılık (Temperature)"
                )
                
                gr.Markdown("""
                ### 💡 İpuçları
                - **Düşük temperature**: Daha tutarlı
                - **Yüksek temperature**: Daha yaratıcı
                - **Uzun maksimum**: Detaylı yanıtlar
                """)
        
        # Örnek sorular
        with gr.Row():
            gr.Markdown("### 💬 Örnek Sorular")
            
        with gr.Row():
            example1 = gr.Button("🤖 Yapay zeka nedir?", size="sm")
            example2 = gr.Button("🚀 Teknova hakkında bilgi ver", size="sm")
            example3 = gr.Button("💡 Yenilikçi proje fikirleri", size="sm")
            example4 = gr.Button("🔬 Gelecekteki teknolojiler", size="sm")
        
        # Event handlers
        send_btn.click(
            chat_response,
            inputs=[msg, chatbot, max_length, temperature],
            outputs=[msg, chatbot]
        )
        
        msg.submit(
            chat_response,
            inputs=[msg, chatbot, max_length, temperature],
            outputs=[msg, chatbot]
        )
        
        clear_btn.click(
            clear_chat,
            outputs=chatbot
        )
        
        # Örnek soru click handlers
        example1.click(lambda: "Yapay zeka nedir?", outputs=msg)
        example2.click(lambda: "Teknova hakkında bilgi ver", outputs=msg)
        example3.click(lambda: "Bana yenilikçi proje fikirleri öner", outputs=msg)
        example4.click(lambda: "Gelecekteki teknolojiler hakkında konuşalım", outputs=msg)
        
        # Alt bilgi
        gr.HTML("""
        <div style="text-align: center; margin-top: 2rem; padding: 1rem; background: #f8f9fa; border-radius: 8px;">
            <p><strong>🚀 Teknova Nova AI</strong> - Özgün yapay zeka teknolojisi</p>
            <p>
                <a href="https://github.com/veteroner/novaai" target="_blank">GitHub</a> | 
                <a href="https://huggingface.co/spaces/YOUR-USERNAME/nova-ai" target="_blank">Hugging Face</a>
            </p>
            <p><em>Made with ❤️ by Teknova</em></p>
        </div>
        """)
    
    return demo

# Uygulamayı oluştur ve başlat
if __name__ == "__main__":
    demo = create_interface()
    demo.queue(max_size=10)  # HF Spaces için queue
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,  # HF Spaces default port
        share=False,
        debug=False
    )
