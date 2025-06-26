#!/bin/bash

# Ollama 설치
curl -fsSL https://ollama.com/install.sh | sh

# 쉘 환경 적용
source ~/.bashrc || source ~/.zshrc

# DeepSeek 모델 다운로드
ollama pull deepseek-chat:latest
