import re
from datetime import datetime, timedelta
import dateparser


DATE_SETTINGS = {
    "LANGUAGE": "ru",
    "RETURN_AS_TIMEZONE_AWARE": False,
}


def parse_single_date(text: str) -> datetime | None:
    dt = dateparser.parse(text, settings=DATE_SETTINGS)
    if not dt:
        return None
    return dt.replace(hour=0, minute=0, second=0, microsecond=0)


def extract_date_range(text: str):
    text = text.lower()
    m = re.search(
        r"с\s+(\d{1,2}\s+\w+\s+\d{4})\s+по\s+(\d{1,2}\s+\w+\s+\d{4})",
        text,
    )
    if m:
        d1 = parse_single_date(m.group(1))
        d2 = parse_single_date(m.group(2))
        if d1 and d2:
            return d1, d2 + timedelta(days=1)

    d = parse_single_date(text)
    if d:
        return d, d + timedelta(days=1)

    return None, None
