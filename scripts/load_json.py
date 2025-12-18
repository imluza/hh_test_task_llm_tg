import json
import asyncio
from datetime import datetime
from app.db import SessionLocal
from app.models import Video, VideoSnapshot
from sqlalchemy.dialects.postgresql import insert


def parse_dt(v: str):
    return datetime.fromisoformat(v.replace("Z", "+00:00"))


async def main(path: str):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)["videos"]

    async with SessionLocal() as session:
        videos = []
        snapshots = []

        for v in data:
            videos.append(
                {
                    "id": v["id"],
                    "creator_id": v["creator_id"],
                    "video_created_at": parse_dt(v["video_created_at"]),
                    "views_count": v["views_count"],
                    "likes_count": v["likes_count"],
                    "comments_count": v["comments_count"],
                    "reports_count": v["reports_count"],
                    "created_at": parse_dt(v["created_at"]),
                    "updated_at": parse_dt(v["updated_at"]),
                }
            )

            for s in v["snapshots"]:
                snapshots.append(
                    {
                        "id": s["id"],
                        "video_id": s["video_id"],
                        "views_count": s["views_count"],
                        "likes_count": s["likes_count"],
                        "comments_count": s["comments_count"],
                        "reports_count": s["reports_count"],
                        "delta_views_count": s["delta_views_count"],
                        "delta_likes_count": s["delta_likes_count"],
                        "delta_comments_count": s["delta_comments_count"],
                        "delta_reports_count": s["delta_reports_count"],
                        "created_at": parse_dt(s["created_at"]),
                        "updated_at": parse_dt(s["updated_at"]),
                    }
                )

        await session.execute(insert(Video), videos)
        await session.execute(insert(VideoSnapshot), snapshots)
        await session.commit()


if __name__ == "__main__":
    import sys
    asyncio.run(main(sys.argv[1]))
