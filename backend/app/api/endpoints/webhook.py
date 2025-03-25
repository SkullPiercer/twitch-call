from aiogram.types import Update
from fastapi import APIRouter, Request

from app.bot.main import bot, dp
from app.core.constants import BOT_COMMANDS

router = APIRouter()


@router.post("")
async def webhook(request: Request) -> None:
    try:
        update = Update.model_validate(
            await request.json(), context={"bot": bot}
        )

        if update.message is not None:
            message_text = (
                update.message.text
                if update.message
                else update.callback_query.data
            )

            if (
                message_text.lower().startswith("/start")
                and len(message_text) > 6
            ):
                ...

            elif message_text.lower() not in BOT_COMMANDS:
                await bot.send_message(
                    update.message.from_user.id,
                    "Привет! Напиши /start, чтобы зарегистрироваться.",
                )
    except Exception as err:
        print("error1", err)

    try:
        await dp.feed_update(bot, update)

    except Exception as err:
        print("error2", err)
