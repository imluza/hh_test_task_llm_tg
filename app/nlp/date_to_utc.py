from datetime import datetime
from app.nlp.timezone import tz_to_offset

def to_utc(local_dt: datetime, user_tz: str) -> datetime:
    offset = tz_to_offset(user_tz)
    return local_dt - offset
