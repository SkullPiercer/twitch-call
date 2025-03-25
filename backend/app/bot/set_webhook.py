import os

import requests
from dotenv import load_dotenv

load_dotenv()

TG_API_KEY = os.getenv("BOT_TOKEN")
webhook = os.getenv("WEBHOOK_URL")

if webhook is None:
    print(
        "------------------------------------------\n"
        "ВЫ ЗАБЫЛИ УКАЗАТЬ WEBHOOK_URL В env ФАЙЛЕ\n"
        "------------------------------------------"
    )
else:

    response = requests.get(
        (
            f"https://api.telegram.org"
            f"/bot{TG_API_KEY}/setWebhook?url={webhook}/api/v1/webhook"
        )
    )
    print(response.json())
