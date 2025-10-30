import streamlit as st
import speech_recognition as sr
from streamlit_lottie import st_lottie
from gtts import gTTS
from io import BytesIO
import base64
import pathlib
import json

st.set_page_config(page_title="",layout="wide")

def css_file(file_path):
    with open(file_path)as f:
        st.html(f"<style>{f.read()}</style>")

filepath = pathlib.Path("assistant.css")
css_file(filepath)

st.markdown("""
<h1 style="color:white;font-size:50px;text-align:center;">🎙️Voice and Text Assistant App</h1>
""",unsafe_allow_html=True)
st.divider()
col = st.columns(3)
with col[0]:
    st.markdown("""
    <h4 style="color:white;font-size:40px;text-align:center;">📝Text To Speech Converter</h4>
    """,unsafe_allow_html=True)
    text_input = st.text_area("**Enter text:**",height=200)
    languages = {'Hindi': 'hi','English': 'en','Tamil': 'ta','French': 'fr','German': 'de',
    'Telugu': 'te','Spanish': 'es','Italian': 'it','Portuguese': 'pt','Russian': 'ru',
    'Chinese (Simplified)': 'zh-CN','Japanese': 'ja','Korean': 'ko','Arabic': 'ar','Turkish': 'tr',
    'Punjabi': 'pa','Urdu': 'ur','Greek': 'el','Dutch': 'nl','Polish': 'pl','Romanian': 'ro',
    'Swedish': 'sv','Thai': 'th','Vietnamese': 'vi'}
    selected_language = st.selectbox("**Select language:**", list(languages.keys()))
    if st.button("🔊Convert to speech",key="speech"):
        if text_input.strip() == "":
            st.error("❌ Please enter some text before converting.")
        else:
            lang_code = languages[selected_language]
            tts = gTTS(text=text_input, lang=lang_code)
            fp = BytesIO()
            tts.write_to_fp(fp)
            st.audio(fp, format='audio/mpeg', start_time=0)
with col[1]:
    def add_lottie_file(lottie_file: str):
        with open(lottie_file, "rb") as f:
            return json.load(f)
    data_lottie = add_lottie_file("Wave Loop.json")
    st_lottie(
        data_lottie,
        height=None,
        width=None
    )
with col[2]:
    st.markdown("""
    <h4 style="color:white;font-size:40px;text-align:center;">🗣️ Speech to Text Converter</h4>
    """,unsafe_allow_html=True)
    d = {"Hindi": "hi-IN","English": "en-IN", "Bengali": "bn-IN",
     "Tamil": "ta-IN", "Telugu": "te-IN", "Chinese": "zh-CN",
     "Japanese": "ja-JP", "Korean": "ko-KR", "French": "fr-FR",
     "German": "de-DE", "Russian": "ru-RU", "Arabic": "ar-SA",
     "Turkish": "tr-TR", "Portuguese": "pt-BR"}
    language = st.selectbox("**Select Language:**", options=list(d.keys()))
    lang_code = d[language]
    form = st.form("")
    timeout = st.slider("**Time Out:**", 1, 10, 5)
    phrase = st.slider("**Phrase Time:**", 1, 60, 10)
    duration = st.slider("**Duration:**", 0.0, 5.0, 1.3)

    if st.button("🎙️ Start Recording", key="voice"):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            st.info("Listening... Please speak clearly into your microphone.")
            r.adjust_for_ambient_noise(source, duration=duration)
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase)

        try:
            with st.spinner("Converting speech to text..."):
                text = r.recognize_google(audio, language=lang_code)
            st.text_area("Recognized Text:", value=text)
        except sr.UnknownValueError:
            st.error("Sorry, could not understand your speech.")
        except sr.RequestError:
            st.error("Could not connect to Google Speech Recognition service.I")
        except sr.WaitTimeoutError:
            st.error("No speech detected. Timed out.")