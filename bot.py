from aiogram import Bot, Dispatcher, executor, types
import requests

API_TOKEN = "8510178079:AAFs7tCVWLONH-A29Y0KrPEW0zDaLT7VKo8"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await msg.answer("Bot aktif! Kirim link CapCut team kamu untuk auto-join.")

@dp.message_handler()
async def auto_join(msg: types.Message):
    link = msg.text
    email = requests.get("https://api.tempmail.lol/generate").json()["address"]
    await msg.answer(f"Membuat akun...\nEmail: {email}")
    await msg.answer("⚠️ Ini contoh bot ya, belum otomatis join CapCut team.")
    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
