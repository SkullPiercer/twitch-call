from aiogram import Bot, Dispatcher

# from app.bot.handlers import router as handlers_router
from app.core.config import settings

bot = Bot(settings.bot_token)
dp = Dispatcher()
# dp.include_router(handlers_router)


async def start_bot():
    try:
        print("Бот запущен🥳.")
    except Exception as e:
        print(f"Ошибка при запуске бота: {e}")


async def stop_bot():
    try:
        print("Бот остановлен.😔")
    except Exception as e:
        print(f"Ошибка при остановке бота: {e}")
