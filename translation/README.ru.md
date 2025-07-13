# 💫 JinnyAI — твой AI vTuber-компаньон

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/Bit-Maximum/JinnyAI/blob/main/README.md)
[![ru](https://img.shields.io/badge/lang-ru-blue.svg)](https://github.com/Bit-Maximum/JinnyAI/blob/main/translation/README.ru.md)

> Личный AI vTuber-друг, с которым можно общаться, тренироваться в иностранных языках и просто весело проводить время.

---

## 📌 О проекте

**JinnyAI** — это экспериментальный проект, вдохновлённый такими феноменами, как [Neuro Sama](https://www.twitch.tv/vedal987) и платформами вроде Character.AI.

Основная цель — создать **AI-компаньона**, с которым можно было бы:
- 💬 вести непринуждённые диалоги (текстовые и голосовые),
- 🌍 тренировать иностранные языки,
- 🤖 взаимодействовать через Discord как с полноценным ботом,
- 🧠 сохранить **долгосрочную память** и контекст в разговоре.

---

## 🌟 Вдохновение и благодарности

- 🧠 **[Neuro Sama](https://www.twitch.tv/vedal987)** от [Vedal987](https://www.twitch.tv/vedal987) — невероятный AI vTuber и главный источник вдохновения. Обязательно загляните на её стримы!
- 📺 **[Limit Cant Code](https://www.youtube.com/@LimitCantCode)** — автор YouTube-серии по разработке собственного AI-компаньона. Его пайплайн помог понять множество технических нюансов. Спасибо!

---

## ✅ Статус проекта

**Активная разработка**.  
Функциональность будет расширяться с течением времени. Сейчас реализовано:

- [x] Discord-бот JinnyAI
- [x] Подключение к LLM (локально или через OpenAI API)
- [x] Ответы в текстовом чате
- [ ] Голосовой ввод и вывод (в процессе)
- [ ] Личностный профиль и постоянная память
- [ ] Интеграция с vtuber-аватаром (в планах)

---

## 🚀 Установка и запуск

### 📦 Зависимости

- Python 3.9+
- [FFMPEG](https://ffmpeg.org/download.html) (для работы с аудио):
    - Установите и добавьте в `PATH`

### 🧠 LLM-драйвер

У Jinny есть модуль подключения к LLM:  
`src/utils/service/openapi_driver.py`

По умолчанию используется **локальный LLM через LM Studio**:
```python
self.client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)
self.model = "qwen2.5-7b-instruct-1m"
```

Ты можешь заменить его на любой другой OpenAI-совместимый сервис.

## ⚙️ Установка и запуск

### 🔧 Требования

- Python 3.10+
- Установленный [FFMPEG](https://ffmpeg.org/download.html) (для записи и воспроизведения аудио)
- Аккаунт OpenAI **или** локально развернутая LLM (например, через [LM Studio](https://lmstudio.ai/))

### 📦 Установка зависимостей

```bash
git clone https://github.com/Bit-Maximum/JinnyAI.git
cd JinnyAI
pip install -r requirements.txt
# или
poetry install
```

## 🚀 Запуск Discord-бота
1. Создайте .env файл и укажите токен для вашего Discord-бота (если у вас нет токена, то вы можете получить его на [портале разработчиков Discord](https://discord.com/developers/docs/intro)):
```env
OPENAI_API_KEY=<OPENAI API KEY LIKE sk-...> # Если вы хотите подключится к OpenAPI
DISCORD_BOT_TOKEN=ваш_токен_бота
```
2. Запуск:
```bash
cd src
python main.py
```

## 🛣️ Дорожная карта (планы)
- [x] Подключение к LLM
- [x] Discord-интеграция (чтение и отправка сообщений)
- [ ] Генерация и воспроизведение речи
- [ ] Захват аудио от пользователя
- [ ] Персонификация Jinny (память, настроение, настройка)
- [ ] Веб-интерфейс или vTuber-обёртка (в духе Veadal / VTube Studio)
- [ ] Интеграция с OBS или стрим-софтом
- [ ] Упаковка в Docker / Windows .exe / WebUI

>Проект всё ещё очень ранний. Любые идеи, pull requests и обсуждения приветствуются!
>Если вы хотите поэкспериментировать с аватаром, голосами или интеллектом — милости прошу!

_🎙️ "Hi! I'm Jinny — your AI buddy. Let's chat, learn, and have fun!"_