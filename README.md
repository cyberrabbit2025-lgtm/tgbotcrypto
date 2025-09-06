# 🤖 tgBotCrypto

Телеграм-бот для учёта переводов между кошельками (ERC20 / TRC20).  
Позволяет добавлять кошельки с именами (например, "1234" = Ваня),  
и по запросу смотреть историю переводов через Etherscan / Tronscan API.  

---

## 🚀 Деплой на Railway

Нажми кнопку ниже, чтобы развернуть бота в один клик:

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/cyberrabbit2025-lgtm/tgbotcrypto)

---

## ⚙️ Переменные окружения

После деплоя нужно указать переменные в Railway → **Variables**:

- `TELEGRAM_BOT_TOKEN` — токен от [BotFather](https://t.me/BotFather)  
- `ETHERSCAN_API_KEY` — API ключ с [Etherscan](https://etherscan.io/myapikey)  
- `TRON_API_KEY` — API ключ с [TronGrid](https://www.trongrid.io/) (можно пустым)  
- `DB_PATH` — путь к базе (по умолчанию `bot.db`)  

---

## 📦 Файлы проекта

- `main.py` — код бота  
- `requirements.txt` — список зависимостей для Python  
- `Procfile` — указывает Railway, как запускать бота  
- `.env.example` — пример файла с переменными окружения  
- `README.md` — документация  

---

## 🛠 Локальный запуск (необязательно)

Если захочешь запускать у себя на компьютере:

```bash
git clone https://github.com/cyberrabbit2025-lgtm/tgbotcrypto.git
cd tgbotcrypto
pip install -r requirements.txt
python main.py
