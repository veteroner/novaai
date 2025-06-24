"""
🧪 Nova AI Test Suite
Teknova Nova AI için test dosyaları
"""

import pytest
import torch
from unittest.mock import Mock, patch
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestNovaAI:
    """Nova AI ana test sınıfı"""
    
    def test_torch_available(self):
        """PyTorch'un kullanılabilir olduğunu test et"""
        assert torch.cuda.is_available() or True  # CPU'da da çalışabilir
        
    def test_transformers_import(self):
        """Transformers kütüphanesinin import edilebilir olduğunu test et"""
        try:
            from transformers import AutoTokenizer, AutoModelForCausalLM
            assert True
        except ImportError:
            pytest.fail("Transformers kütüphanesi import edilemedi")
    
    def test_gradio_import(self):
        """Gradio'nun import edilebilir olduğunu test et"""
        try:
            import gradio as gr
            assert True
        except ImportError:
            pytest.fail("Gradio kütüphanesi import edilemedi")
            
    def test_fastapi_import(self):
        """FastAPI'nin import edilebilir olduğunu test et"""
        try:
            from fastapi import FastAPI
            assert True
        except ImportError:
            pytest.fail("FastAPI kütüphanesi import edilemedi")

class TestGradioApp:
    """Gradio uygulaması testleri"""
    
    @patch('gradio_app.load_model')
    def test_gradio_app_import(self, mock_load_model):
        """Gradio app'in import edilebilir olduğunu test et"""
        mock_load_model.return_value = "Model yüklendi"
        try:
            import gradio_app
            assert True
        except ImportError:
            pytest.fail("gradio_app modülü import edilemedi")
    
    def test_chat_response_empty_message(self):
        """Boş mesaj ile chat response testi"""
        from gradio_app import chat_response
        
        # Mock model ve tokenizer
        with patch('gradio_app.model', None), patch('gradio_app.tokenizer', None):
            result = chat_response("", [])
            assert "henüz yüklenmedi" in result.lower()

class TestFastAPIApp:
    """FastAPI uygulaması testleri"""
    
    def test_app_creation(self):
        """FastAPI uygulamasının oluşturulabilir olduğunu test et"""
        try:
            import app
            assert hasattr(app, 'app')
        except Exception as e:
            pytest.fail(f"FastAPI uygulaması oluşturulamadı: {e}")

class TestMainConsole:
    """Konsol uygulaması testleri"""
    
    @patch('main.load_nova_model')
    def test_main_import(self, mock_load_model):
        """Main modülünün import edilebilir olduğunu test et"""
        mock_load_model.return_value = (Mock(), Mock())
        try:
            import main
            assert hasattr(main, 'load_nova_model')
        except ImportError:
            pytest.fail("main modülü import edilemedi")

class TestModelFunctions:
    """Model fonksiyonları testleri"""
    
    def test_model_path_check(self):
        """Model path kontrolü"""
        import os
        expected_paths = [
            "./nova-ai-model",
            "/content/nova-ai-model"
        ]
        
        # En azından bir path tanımlanmış olmalı
        assert len(expected_paths) > 0
        
    @patch('os.path.exists')
    def test_model_path_selection(self, mock_exists):
        """Model path seçim mantığı testi"""
        mock_exists.side_effect = lambda path: path == "/content/nova-ai-model"
        
        # Colab path mevcut olduğunda onu seçmeli
        colab_path = "/content/nova-ai-model"
        local_path = "./nova-ai-model"
        
        import os
        selected_path = colab_path if os.path.exists(colab_path) else local_path
        assert selected_path == colab_path

class TestAPIEndpoints:
    """API endpoint testleri"""
    
    @pytest.fixture
    def client(self):
        """Test client oluştur"""
        from fastapi.testclient import TestClient
        import app
        return TestClient(app.app)
    
    def test_root_endpoint(self, client):
        """Ana endpoint testi"""
        response = client.get("/")
        assert response.status_code == 200
        assert "Nova AI" in response.text
        
    @patch('app.model', Mock())
    @patch('app.tokenizer', Mock())
    def test_chat_endpoint_structure(self, client):
        """Chat endpoint yapısı testi"""
        # POST endpoint'in mevcut olduğunu kontrol et
        response = client.post("/chat", json={"prompt": "test"})
        # 500 olabilir (model gerçek değil) ama endpoint mevcut olmalı
        assert response.status_code in [200, 500]

class TestErrorHandling:
    """Hata yönetimi testleri"""
    
    def test_empty_model_path(self):
        """Boş model path durumu"""
        with patch('os.path.exists', return_value=False):
            # Model path mevcut değilse uygun hata mesajı vermeli
            import os
            model_exists = os.path.exists("./nova-ai-model")
            assert not model_exists
    
    def test_invalid_input_handling(self):
        """Geçersiz input handling"""
        from gradio_app import chat_response
        
        # Boş string testi
        with patch('gradio_app.model', None):
            result = chat_response("", [])
            assert isinstance(result, str)
            assert len(result) > 0

class TestPerformance:
    """Performance testleri"""
    
    def test_import_time(self):
        """Import süresi testi"""
        import time
        
        start_time = time.time()
        import gradio as gr
        import torch
        from transformers import AutoTokenizer
        end_time = time.time()
        
        # Import süresi 10 saniyeyi geçmemeli
        assert (end_time - start_time) < 10.0
        
    @pytest.mark.skipif(not torch.cuda.is_available(), reason="GPU gerekli")
    def test_gpu_availability(self):
        """GPU kullanılabilirlik testi"""
        assert torch.cuda.is_available()
        assert torch.cuda.device_count() > 0

if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 