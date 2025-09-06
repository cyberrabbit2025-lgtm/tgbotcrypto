import os
import sqlite3
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

# Читаем ключи из переменных окружения
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
TRON_API_KEY = os.getenv("TRON_API_KEY")

DB_PATH = os.getenv("DB_PATH", "bot.db")

# Настраиваем базу данных
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS persons (name TEXT PRIMARY KEY)")
cursor.execute("CREATE TABLE IF NOT EXISTS wallets (wallet TEXT PRIMARY KEY, name TEXT, chain TEXT)")
conn.commit()

# Настройка бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("👋 Привет! Я бот для учёта транзакций.\n\n"
                         "Команды:\n"
                         "/addperson <Имя>\n"
                         "/addwallet <Имя> <Кошелёк> <CHAIN: ETH/TRON>\n"
                         "/check <Имя1> <Имя2> <TOKEN> [days=30] [chain=ALL]")

@dp.message(Command("addperson"))
async def add_person(message: Message):
    try:
        _, name = message.text.split()
        cursor.execute("INSERT OR IGNORE INTO persons (name) VALUES (?)", (name,))
        conn.commit()
        await message.answer(f"✅ Добавлен пользователь: {name}")
    except:
        await message.answer("⚠️ Используй: /addperson Имя")

@dp.message(Command("addwallet"))
async def add_wallet(message: Message):
    try:
        _, name, wallet, chain = message.text.split()
        cursor.execute("INSERT OR REPLACE INTO wallets (wallet, name, chain) VALUES (?, ?, ?)", (wallet, name, chain.upper()))
        conn.commit()
        await message.answer(f"✅ Добавлен кошелёк {wallet} для {name} ({chain.upper()})")
    except:
        await message.answer("⚠️ Используй: /addwallet Имя Кошелёк ETH/TRON")

# Заглушка для проверки транзакций
@dp.message(Command("check"))
async def check(message: Message):
    await message.answer("🔍 Эта функция пока упрощена. Здесь будет проверка транзакций через Etherscan/TronGrid.")

async def main():
    print("🤖 Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
