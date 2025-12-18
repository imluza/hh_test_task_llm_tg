from app.nlp.date_parser import extract_date_range
from app.nlp.date_to_utc import to_utc

def get_utc_range(text: str, user_tz: str):
    local_from, local_to = extract_date_range(text)

    if not local_from:
        return None, None

    return (
        to_utc(local_from, user_tz),
        to_utc(local_to, user_tz),
    )
