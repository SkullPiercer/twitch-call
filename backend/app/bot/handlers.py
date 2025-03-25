from aiogram import Router
from aiogram.filters import Command
from aiogram.types import MenuButtonWebApp, Message, WebAppInfo

from app.core.config import settings

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    menu_button = MenuButtonWebApp(
        text="Войти в приложение",
        web_app=WebAppInfo(url=settings.webhook_url),
    )
    await message.bot.set_chat_menu_button(
        chat_id=message.chat.id, menu_button=menu_button
    )
