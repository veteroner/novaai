from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import uvicorn
import os

# Teknova Nova AI - Özgün Model API
app = FastAPI(
    title="Teknova Nova AI API", 
    description="Teknova'nın özgün Nova AI modeli API servisi"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Access-Control-Allow-Origin"]
)

# Nova AI Model path - Özgün model
model_path = "./nova-ai-model"  # Yerel Nova AI model
colab_path = "/content/nova-ai-model"  # Colab için path

# Path kontrolü
actual_path = colab_path if os.path.exists(colab_path) else model_path

print("🚀 Teknova Nova AI API modeli yükleniyor...")
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
    print("✅ Teknova Nova AI API hazır!")
    print("🎉 Özgün Nova AI teknolojisi aktif!")
except Exception as e:
    print(f"❌ Nova AI model yükleme hatası: {e}")
    model = None
    tokenizer = None

@app.post("/chat")
async def chat(request: Request):
    if model is None or tokenizer is None:
        return JSONResponse({
            "error": "Teknova Nova AI modeli yüklenmedi",
            "solution": "Nova AI model dosyalarınızı doğru konuma yükleyin"
        })
    
    try:
        data = await request.json()
        prompt = data.get("prompt", "")
        
        # Nova AI konuşma formatı
        conversation = f"Kullanıcı: {prompt}\nNova AI:"
        
        inputs = tokenizer(conversation, return_tensors="pt").to(model.device)
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs, 
                max_new_tokens=128,
                temperature=0.7,
                do_sample=True
            )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        nova_response = response[len(conversation):].strip()
        
        return JSONResponse({
            "response": nova_response,
            "model": "Teknova Nova AI - Özgün Model"
        }, headers={"Access-Control-Allow-Origin": "*"})
        
    except Exception as e:
        return JSONResponse({
            "error": f"Nova AI API hatası: {str(e)}"
        }, headers={"Access-Control-Allow-Origin": "*"})

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8500, reload=True)
