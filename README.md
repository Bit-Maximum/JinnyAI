# 💫 JinnyAI — Your AI vTuber Companion

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/Bit-Maximum/JinnyAI/blob/main/README.md)
[![ru](https://img.shields.io/badge/lang-ru-blue.svg)](https://github.com/Bit-Maximum/JinnyAI/blob/main/translation/README.ru.md)

> A personal AI vTuber friend you can talk to, practice foreign languages with, and just have fun.

---

## 📌 About the Project

**JinnyAI** is an experimental project inspired by concepts like [Neuro Sama](https://www.twitch.tv/vedal987) and platforms such as Character.AI.

The main goal is to build an **AI companion** you can:
- 💬 Chat with naturally (text and voice)
- 🌍 Practice foreign languages
- 🤖 Interact with through Discord like a real bot
- 🧠 Maintain **long-term memory** and conversation context

---

## 🌟 Inspiration & Thanks

- 🧠 **[Neuro Sama](https://www.twitch.tv/vedal987)** by [Vedal987](https://www.twitch.tv/vedal987) — an incredible AI vTuber and the main source of inspiration. Definitely check out her streams!
- 📺 **[Limit Cant Code](https://www.youtube.com/@LimitCantCode)** — the author of a YouTube series on building an AI companion. His pipeline helped clarify many technical aspects. Huge thanks!

---

## ✅ Project Status

**Actively in development.**.  
Functionality will expand over time. Current features:

- [x] JinnyAI Discord bot
- [x] LLM integration (locally or via OpenAI API)
- [x] Text-based chat
- [ ] Voice input/output (in progress)
- [ ] Personality profile & persistent memory
- [ ] vTuber avatar integration (planned)

---

## 🚀 Installation & Launch

### 📦 Requirements

- Python 3.9+
- [FFMPEG](https://ffmpeg.org/download.html) (for audio processing):
    - Make sure it is installed and added to your system `PATH`

### 🧠 LLM Integration

Jinny uses a dedicated LLM driver module:
`src/utils/service/openapi_driver.py`

By default, it connects to a **local LLM via LM Studio**:
```python
self.client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)
self.model = "qwen2.5-7b-instruct-1m"
```

You can replace this with any OpenAI-compatible provider.

## ⚙️ Setup Instructions

### 🔧 Prerequisites

- Python 3.10+
- [FFMPEG](https://ffmpeg.org/download.html) installed (for recording and playing audio)
- An OpenAI account or a locally hosted LLM (e.g., via [LM Studio](https://lmstudio.ai/))

### 📦 Dependency Installation

```bash
git clone https://github.com/Bit-Maximum/JinnyAI.git
cd JinnyAI
pip install -r requirements.txt
# or
poetry install
```

## 🚀 Running the Discord Bot
1. Create a .env file and add your Discord bot token (if you don’t have one yet, generate it via the [Discord Developer Portal](https://discord.com/developers/docs/intro)):
```env
OPENAI_API_KEY=<OPENAI API KEY LIKE sk-...> # For OpenAI API (optional if using local model)
DISCORD_BOT_TOKEN=<your_discord_bot_token>
```
2. Start the bot:
```bash
cd src
python main.py
```

## 🛣️ Roadmap
- [x] LLM integration
- [x] Discord support (reading/sending messages)
- [ ] Voice generation and playback
- [ ] User audio input
- [ ] Jinny's personalization (memory, mood, tuning)
- [ ] Web interface or vTuber wrapper (like Vedal / VTube Studio)
- [ ] OBS or streaming software integration
- [ ] Packaging into Docker / Windows .exe / WebUI

>The project is still in early stages. Any ideas, pull requests, and discussions are welcome!
>If you’d like to experiment with avatars, voices, or intelligence — you're more than welcome!

_🎙️ “Hi! I’m Jinny — your AI buddy. Let’s chat, learn, and have fun!”_