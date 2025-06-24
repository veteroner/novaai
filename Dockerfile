# 🚀 Nova AI Docker Image
FROM python:3.9-slim

# 📋 Metadata
LABEL maintainer="Teknova <teknova@example.com>"
LABEL description="Teknova Nova AI - Özgün yapay zeka teknolojisi"
LABEL version="1.0.0"

# 🔧 Environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# 📂 Working directory
WORKDIR /app

# 🔧 System dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# 📦 Copy requirements first (for better caching)
COPY requirements.txt .

# 🐍 Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 📁 Copy application code
COPY . .

# 👤 Create non-root user
RUN useradd -m -u 1000 novaai && chown -R novaai:novaai /app
USER novaai

# 🌐 Expose port
EXPOSE 8000

# 🚀 Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/ || exit 1

# 🏃 Run application
CMD ["python", "app.py"] 