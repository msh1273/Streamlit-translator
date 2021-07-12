import streamlit as st
from googletrans import Translator

st.title("구글 번역기")
from_text = st.text_input("번역할 글", "안녕 세상아!")
btn_translate = st.button("번역하기")

source = st.selectbox("나의 언어 (또는 자동)", ("auto", "engilsh", "korean", "japan"))
destination = st.selectbox("무슨 언어로 번역할지", ("english", "korean", "japan"))

translator = Translator()

if btn_translate: 
    if not source or source == "auto":  
        src = translator.detect(from_text).lang  
        source = src

    if not destination:  
        destination = "en" 

    result = translator.translate(
        from_text, dest=destination, src=source if source else src
    )
    st.success(result.text)
    st.write(f"Translated from {source if source else src} to {destination}")