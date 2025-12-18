from datetime import timedelta

def tz_to_offset(tz: str) -> timedelta:
    """
    tz: 'UTC', 'UTC+3', 'UTC-3'
    """
    if tz == "UTC":
        return timedelta(0)

    sign = 1 if "+" in tz else -1
    hours = int(tz.split(sign == 1 and "+" or "-")[1])
    return timedelta(hours=sign * hours)
