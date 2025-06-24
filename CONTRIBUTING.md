# 🤝 Nova AI'ya Katkıda Bulunma Rehberi

**Teknova Nova AI** projesine katkıda bulunmak istediğiniz için teşekkürler! Bu rehber, katkı sürecini kolaylaştırmak için hazırlanmıştır.

## 🎯 Katkı Türleri

### 🐛 **Bug Reports (Hata Bildirimi)**
- Detaylı hata açıklaması
- Tekrar edilebilir adımlar
- Sistem bilgileri (OS, Python version)
- Error logs ve screenshots

### ✨ **Feature Requests (Özellik İstekleri)**  
- Özelliğin amacını açıklayın
- Kullanım senaryolarını belirtin
- Mevcut alternatiflerle karşılaştırın

### 🔧 **Code Contributions (Kod Katkıları)**
- Bug fixes
- Performance improvements
- New features
- Documentation updates

### 📚 **Documentation**
- README improvements
- Code comments
- Tutorial yazıları
- API documentation

## 🚀 Başlangıç Adımları

### 1️⃣ **Repository'yi Fork Edin**
```bash
# GitHub'da Fork butonuna tıklayın
# Sonra local'e clone edin:
git clone https://github.com/YOUR-USERNAME/novaai.git
cd novaai
```

### 2️⃣ **Development Environment Kurun**
```bash
# Virtual environment oluşturun
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate    # Windows

# Dependencies yükleyin
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Dev dependencies
```

### 3️⃣ **Model Dosyalarını Hazırlayın**
```bash
# MODEL_SETUP.md rehberini takip edin
mkdir nova-ai-model
# Model dosyalarınızı bu klasöre yerleştirin
```

## 📋 Development Workflow

### 🌿 **Branch Oluşturma**
```bash
# Main branch'ten yeni branch oluşturun
git checkout main
git pull origin main
git checkout -b feature/amazing-feature

# Veya bug fix için:
git checkout -b fix/bug-description
```

### 💻 **Code Style**
```python
# Python kod standartları:
# - PEP 8 compliance
# - Type hints kullanın
# - Docstrings ekleyin

def nova_chat(message: str, history: List[Dict]) -> str:
    """
    Nova AI ile sohbet fonksiyonu.
    
    Args:
        message: Kullanıcı mesajı
        history: Sohbet geçmişi
        
    Returns:
        Nova AI yanıtı
    """
    # Implementation here
    pass
```

### 🧪 **Testing**
```bash
# Testleri çalıştırın
python -m pytest tests/

# Linting kontrolleri
flake8 .
black --check .
mypy .

# Security check
bandit -r .
```

### 📝 **Commit Messages**
```bash
# Anlamlı commit messages yazın:
git commit -m "✨ Add: Nova AI temperature control feature

- Add temperature parameter to chat function
- Update Gradio interface with slider
- Add tests for temperature validation
- Update documentation

Fixes #123"
```

## 🔍 Code Review Süreci

### 📋 **Pull Request Checklist**
- [ ] Code changes test edildi
- [ ] Yeni features için testler eklendi
- [ ] Documentation güncellendi
- [ ] Commit messages açıklayıcı
- [ ] Code style check'leri geçiyor
- [ ] No breaking changes (veya belirtildi)

### 🎯 **Pull Request Template**
```markdown
## 📝 Description
Brief description of changes

## 🔧 Type of Change
- [ ] Bug fix
- [ ] New feature  
- [ ] Breaking change
- [ ] Documentation update

## 🧪 Testing
- [ ] Tests pass locally
- [ ] Added tests for new features
- [ ] Manual testing completed

## 📋 Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No conflicts with main branch
```

## 🛠️ Development Guidelines

### 🎯 **Nova AI Specific Guidelines**

#### 🧠 **Model Integration**
```python
# Model loading best practices:
def load_nova_model(model_path: str) -> Tuple[Any, Any]:
    """Load Nova AI model with error handling."""
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float16,
            device_map="auto"
        )
        return model, tokenizer
    except Exception as e:
        logger.error(f"Model loading failed: {e}")
        raise
```

#### 🌐 **API Design**
```python
# FastAPI endpoint conventions:
@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest) -> ChatResponse:
    """Nova AI chat endpoint with proper error handling."""
    try:
        # Validate input
        if not request.message.strip():
            raise HTTPException(400, "Message cannot be empty")
        
        # Process with Nova AI
        response = await nova_chat(request.message, request.history)
        
        return ChatResponse(
            response=response,
            model="Teknova Nova AI",
            timestamp=datetime.utcnow()
        )
    except Exception as e:
        logger.error(f"Chat error: {e}")
        raise HTTPException(500, "Internal server error")
```

#### 🎨 **UI/UX Standards**
```python
# Gradio interface guidelines:
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.HTML("""
    <div style="text-align: center; padding: 20px;">
        <h1>🚀 Teknova Nova AI</h1>
        <p>Özgün yapay zeka teknolojisi</p>
    </div>
    """)
    
    # Always include:
    # - Clear labeling
    # - Error handling
    # - Loading states
    # - Responsive design
```

## 🏗️ Project Structure

```
novaai/
├── 📁 .github/
│   ├── workflows/          # GitHub Actions
│   ├── ISSUE_TEMPLATE/     # Issue templates
│   └── PULL_REQUEST_TEMPLATE.md
├── 📁 src/
│   ├── nova_ai/           # Main package
│   ├── api/               # API endpoints
│   ├── ui/                # User interfaces
│   └── utils/             # Utilities
├── 📁 tests/              # Test files
├── 📁 docs/               # Documentation
├── 📁 scripts/            # Build/deploy scripts
├── 🔧 requirements.txt
├── 🔧 requirements-dev.txt
├── 📋 pyproject.toml
└── 📖 README.md
```

## 🎯 Öncelikli Katkı Alanları

### 🔥 **High Priority**
- [ ] **Performance optimization** - Model inference speed
- [ ] **Memory management** - RAM kullanımı iyileştirmeleri
- [ ] **Error handling** - Robust error recovery
- [ ] **Testing coverage** - Unit ve integration testler

### 🌟 **Medium Priority**  
- [ ] **New UI features** - Advanced chat options
- [ ] **API extensions** - Batch processing
- [ ] **Documentation** - Tutorial videos
- [ ] **Localization** - Multi-language support

### 💡 **Nice to Have**
- [ ] **Mobile optimization** - Responsive design
- [ ] **Plugin system** - Extensible architecture
- [ ] **Analytics** - Usage metrics
- [ ] **Deployment tools** - Docker, K8s support

## 🤔 Sorularınız mı Var?

### 💬 **İletişim Kanalları**
- **GitHub Discussions**: Genel sorular için
- **GitHub Issues**: Bug reports ve feature requests
- **Email**: teknova@example.com (teknik destek)
- **Discord**: Nova AI Community Server

### 📚 **Yararlı Kaynaklar**
- [Python Style Guide](https://pep8.org/)
- [Transformers Documentation](https://huggingface.co/docs/transformers)
- [FastAPI Best Practices](https://fastapi.tiangolo.com/tutorial/)
- [Gradio Documentation](https://gradio.app/docs/)

## 🙏 Teşekkürler

Nova AI projesine katkıda bulunan herkese teşekkür ederiz! Sizin katkılarınız Nova AI'yi daha da güçlü kılıyor.

### 🏆 **Katkıda Bulunanlar**
- **Teknova Team** - Proje kurucu ekibi
- **Community Contributors** - Açık kaynak katkıları

---

🚀 **Teknova Nova AI** - Birlikte daha güçlüyüz!

*Bu rehber sürekli güncellenmektedir. Önerilerinizi GitHub Discussions'ta paylaşabilirsiniz.* 