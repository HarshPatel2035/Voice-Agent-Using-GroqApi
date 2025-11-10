# 🎙️ Voice Agent using Groq API

An interactive **AI-powered voice assistant** built with **Streamlit** and **Groq API**, capable of listening to user input through voice, understanding the query, and responding both **visually** and **through speech**.

🌐 **Live Demo:** [Voice Agent App](https://voice-agent-using-groapppi-aexaalavybgs43g2uwvzra.streamlit.app/)

---

## 🚀 Features

- 🎤 **Voice Input:** Speak directly to the AI using the Streamlit microphone widget.
- 💬 **Smart AI Responses:** Uses **Groq API** to generate intelligent and conversational answers.
- 🔊 **Speech Output:** Converts AI responses to speech using **gTTS** for a smooth audio experience.
- 🧠 **Conversational Flow:** Designed to simulate an AI Engineer being interviewed.
- 🌍 **Web-Based:** Runs completely in the browser — no local setup required.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **AI Model:** Groq API
- **Speech-to-Text:** Streamlit’s built-in microphone
- **Text-to-Speech:** Google Text-to-Speech (gTTS)
- **Deployment:** Streamlit Cloud

---

## 🧩 Project Structure

```
├── app.py                # Main Streamlit application
├── config.py             # Contains API key and configuration settings
├── requirements.txt      # Required Python packages
└── README.md             # Project documentation
```

---

## ⚙️ Setup Instructions

1. **Clone this repository:**
   ```bash
   git clone https://github.com/<your-username>/voice-agent.git
   cd voice-agent
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your Groq API key:**
   - Create a `config.py` file in the project root.
   - Add the following line inside it:
     ```python
     GROQ_API_KEY = "your_api_key_here"
     ```

4. **Run the app locally:**
   ```bash
   streamlit run app.py
   ```

---

## 💡 Example Questions

You can ask questions like:
- “What should we know about your life story in a few sentences?”
- “What’s your #1 superpower?”
- “What are the top 3 areas you’d like to grow in?”
- “How do you push your boundaries and limits?”

---

## 📫 Contact

**Harsh Patel**  
📧 harshpatel20.official@gmail.com  
🔗 [GitHub Profile](https://github.com/HarshPatel2035)
