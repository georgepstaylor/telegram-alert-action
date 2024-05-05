from env import Env
import requests
import json

telegram_base_url = "https://api.telegram.org/bot"

def telegram_check_token():
    try:
        user = requests.get(telegram_base_url + Env.TELEGRAM_BOT_TOKEN + "/getMe")
        if user.status_code == 200:
            if user.json()["ok"]:
                return True
            else:
                raise Exception("Authentication failed with Telegram API")
        else:
            raise Exception("Request did not return 200 status code")
    except Exception as e:
        raise Exception("Request failed to connect to Telegram API with error: " + str(e))

def telegram_send_message(message, parse_mode, inline_keyboard=[]):
    response = requests.post(
        f"{telegram_base_url}{Env.TELEGRAM_BOT_TOKEN}/sendMessage",
        json={
            "chat_id": Env.TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": parse_mode,
            "reply_markup": {
                "inline_keyboard": inline_keyboard
            }
        }
    )
    print(response.json())

def main():
    if telegram_check_token():
        print("Token is valid")
        telegram_send_message(
            message=Env.TELEGRAM_MSG_TEXT,
            inline_keyboard=Env.TELEGRAM_MSG_INLINE_KEYBOARD,
            parse_mode=Env.TELEGRAM_MSG_PARSE_MODE
        )
    else:
        exit(1)


if __name__ == "__main__":
    main()