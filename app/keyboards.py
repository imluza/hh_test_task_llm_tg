from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TZ_OPTIONS = [
    ("UTC-3", "UTC-3"),
    ("UTC", "UTC"),
    ("UTC+3", "UTC+3"),
    ("UTC+5", "UTC+5"),
    ("UTC+7", "UTC+7"),
]

def timezone_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=label, callback_data=f"tz:{value}")]
            for label, value in TZ_OPTIONS
        ]
    )
