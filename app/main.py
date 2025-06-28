# app/main.py
import streamlit as st
import whisper
from llm_deepseek import call_llm
import tempfile
import os

st.set_page_config(page_title="AI 튜터 베타", layout="centered")
st.title("🧠🎙️ AI 튜터 실험실")

# Whisper 모델 로드 (base 권장)
stt_model = whisper.load_model("base")

# 음성 업로드
uploaded_file = st.file_uploader("🎤 음성 파일 업로드 (wav/mp3)", type=["wav", "mp3"])

if uploaded_file is not None:
    st.audio(uploaded_file)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    with st.spinner("⏳ 음성 → 텍스트 변환 중..."):
        result = stt_model.transcribe(tmp_path, fp16=False)
        user_text = result["text"]
        os.remove(tmp_path)

    st.success("✅ 변환 완료")
    st.markdown(f"**🗣️ 인식된 문장:** `{user_text}`")

    with st.spinner("🤖 AI 튜터 응답 생성 중..."):
        ai_response = call_llm(user_text)
    st.markdown("---")
    st.markdown(f"**🧠 튜터 응답:**")
    st.info(ai_response)
