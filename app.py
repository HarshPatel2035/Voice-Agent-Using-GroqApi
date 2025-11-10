import streamlit as st
import tempfile
import os
import pyttsx3
import speech_recognition as sr
from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

st.set_page_config(page_title="AI Engineer VoiceBot 🎙️", page_icon="🤖", layout="centered")

st.title("🤖 AI Engineer Voice Interview Bot")
st.markdown("Speak your question — this bot will respond as an **AI Engineer candidate** being interviewed.")

def speak_text(text):
    """Convert text to speech using pyttsx3"""
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 170)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        st.warning("Speech playback not supported on this platform.")

def get_audio():
    """Record voice input using Streamlit's built-in mic"""
    audio_data = st.audio_input("🎤 Ask your interview question:")
    if audio_data:
        temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        temp_audio.write(audio_data.getvalue())
        temp_audio.close()
        return temp_audio.name
    return None

def transcribe_audio(file_path):
    """Transcribe the recorded audio using Google SpeechRecognition"""
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except Exception as e:
        st.error(f"Transcription failed: {e}")
        return None

def generate_response(prompt):
    """Generate AI response using Groq"""
    try:
        completion = client.chat.completions.create(

            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_completion_tokens=160,
            top_p=1,
            stream=False,
            messages=[
                {"role": "system", "content": "You are an AI Engineer being interviewed. Give confident, concise, and technically sound answers in 2-3 sentences."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        st.error(f"Groq API Error: {e}")
        return None

st.markdown("---")
st.markdown("🎙 Click below and start speaking your interview question.")

audio_file = get_audio()

if audio_file:
    st.success("✅ Audio recorded successfully! Processing your question...")
    user_question = transcribe_audio(audio_file)

    if user_question:
        st.info(f"**You asked:** {user_question}")
        answer = generate_response(user_question)

        if answer:
            st.success(f"**AI Engineer Answer:** {answer}")
            speak_text(answer)
        else:
            st.error("Failed to generate an answer.")
    else:
        st.warning("Could not recognize your speech. Please try again.")
