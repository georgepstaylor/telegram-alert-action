import os
import json

class Env:
    try:
        TELEGRAM_BOT_TOKEN=os.environ.get("INPUT_TELEGRAM_BOT_TOKEN")
    except:
        raise Exception("TELEGRAM_BOT_TOKEN not found in environment variables")
    try:
        TELEGRAM_CHAT_ID=os.environ.get("INPUT_TELEGRAM_CHAT_ID")
    except:
        raise Exception("TELEGRAM_CHAT_ID not found in environment variables")

    TELEGRAM_MSG_TEXT=os.environ.get("INPUT_TELEGRAM_MSG_TEXT")
    try:
        TELEGRAM_MSG_INLINE_KEYBOARD=json.loads(os.environ.get("INPUT_TELEGRAM_MSG_INLINE_KEYBOARD", []))
    except:
        raise Exception("TELEGRAM_MSG_INLINE_KEYBOARD could not be parsed as JSON")
    TELEGRAM_MSG_PARSE_MODE=os.environ.get("INPUT_TELEGRAM_MSG_PARSE_MODE")
