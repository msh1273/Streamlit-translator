import streamlit as st
from googletrans import Translator

st.title("구글 번역기")
from_text = st.text_input("번역할 글", "안녕 세상아!")
btn_translate = st.button("번역하기")

source = st.selectbox("나의 언어 (또는 자동)", ("auto", "engilsh", "korean", "japan"))
destination = st.selectbox("무슨 언어로 번역할지", ("english", "korean", "japan"))

translator = Translator()

if btn_translate:  # 버튼 누르면
    if not source or source == "auto":  # 나의 언어 선택을 안했거나, "auto"이면
        src = translator.detect(from_text).lang  # 언어 감지하기
        source = src

    if not destination:  # 무슨 언어로 번역할지 선택을 안했으면
        destination = "en"  # 기본은 영어로 한다.

    result = translator.translate(
        from_text, dest=destination, src=source if source else src
    )
    st.success(result.text)
    st.write(f"Translated from {source if source else src} to {destination}")