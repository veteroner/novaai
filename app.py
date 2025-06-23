from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

# Teknova Nova AI - Özgün Model
app = FastAPI(
    title="Teknova Nova AI", 
    description="Teknova'nın özgün Nova AI modeli - Token gerektirmez",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Access-Control-Allow-Origin"]
)

# Nova AI Model yüklemesi - Özgün teknoloji
model_path = "./nova-ai-model"  # Kendi Nova AI modeliniz
colab_path = "/content/nova-ai-model"  # Colab için path

# Path kontrolü
actual_path = colab_path if os.path.exists(colab_path) else model_path

print("🚀 Teknova Nova AI modeli yükleniyor... (Web API)")
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
    print("✅ Teknova Nova AI Web API hazır!")
    print("🎉 Özgün Nova AI teknolojisi aktif!")
except Exception as e:
    print(f"❌ Nova AI model yükleme hatası: {e}")
    print("💡 Nova AI model dosyalarınızı doğru konuma yüklediğinizden emin olun.")

@app.get("/")
async def home():
    return HTMLResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Teknova Nova AI</title>
        <meta charset="utf-8">
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; 
                   background: linear-gradient(135deg, #ff6b6b, #4ecdc4); 
                   color: white; text-align: center; padding: 50px; }
            .container { background: rgba(255,255,255,0.1); padding: 40px; border-radius: 20px; 
                        backdrop-filter: blur(10px); max-width: 600px; margin: 0 auto; }
            h1 { font-size: 3rem; margin-bottom: 20px; }
            p { font-size: 1.2rem; margin-bottom: 15px; }
            .feature { background: rgba(255,255,255,0.2); padding: 15px; margin: 10px 0; 
                      border-radius: 10px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Teknova Nova AI</h1>
            <p><strong>Özgün yapay zeka teknolojisi</strong></p>
            <div class="feature">
                🌟 Tamamen özgün Teknova Nova AI modeli
            </div>
            <div class="feature">
                ⚡ Token gerektirmez - Kendi modeliniz
            </div>
            <div class="feature">
                🧠 Gelişmiş AI teknolojisi
            </div>
            <div class="feature">
                🚀 API Endpoint: <strong>/chat</strong>
            </div>
            <p style="margin-top: 30px; font-size: 0.9rem; opacity: 0.8;">
                API kullanımı: POST /chat {"prompt": "Mesajınız"}
            </p>
        </div>
    </body>
    </html>
    """)

@app.post("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "")
        
        if not prompt.strip():
            return JSONResponse({
                "error": "Lütfen Nova AI'ya mesajınızı yazın",
                "model": "Teknova Nova AI"
            })
        
        # Nova AI ile konuşma formatı
        conversation = f"Kullanıcı: {prompt}\nNova AI:"
        
        inputs = tokenizer(conversation, return_tensors="pt").to(model.device)
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs, 
                max_new_tokens=256,
                temperature=0.7,
                top_p=0.9,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        nova_response = response[len(conversation):].strip()
        
        return JSONResponse({
            "response": nova_response,
            "model": "Teknova Nova AI - Özgün Model",
            "status": "success"
        }, headers={"Access-Control-Allow-Origin": "*"})
        
    except Exception as e:
        return JSONResponse({
            "error": f"Nova AI hatası: {str(e)}",
            "model": "Teknova Nova AI",
            "status": "error"
        }, headers={"Access-Control-Allow-Origin": "*"})

if __name__ == "__main__":
    import uvicorn
    print("🌐 Teknova Nova AI Web sunucusu başlatılıyor...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
