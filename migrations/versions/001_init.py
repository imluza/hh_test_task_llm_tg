from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("telegram_id", sa.String(), primary_key=True),
        sa.Column("timezone", sa.String(), nullable=False),
    )

    op.create_table(
        "videos",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("creator_id", sa.String(), nullable=False),
        sa.Column("video_created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("views_count", sa.Integer(), nullable=False),
        sa.Column("likes_count", sa.Integer(), nullable=False),
        sa.Column("comments_count", sa.Integer(), nullable=False),
        sa.Column("reports_count", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )

    op.create_index("ix_videos_creator", "videos", ["creator_id"])
    op.create_index("ix_videos_created", "videos", ["video_created_at"])
    op.create_index("ix_videos_views", "videos", ["views_count"])

    op.create_table(
        "video_snapshots",
        sa.Column("id", sa.Text(), primary_key=True),
        sa.Column("video_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("views_count", sa.Integer(), nullable=False),
        sa.Column("likes_count", sa.Integer(), nullable=False),
        sa.Column("comments_count", sa.Integer(), nullable=False),
        sa.Column("reports_count", sa.Integer(), nullable=False),
        sa.Column("delta_views_count", sa.Integer(), nullable=False),
        sa.Column("delta_likes_count", sa.Integer(), nullable=False),
        sa.Column("delta_comments_count", sa.Integer(), nullable=False),
        sa.Column("delta_reports_count", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["video_id"], ["videos.id"], ondelete="CASCADE"),
    )

    op.create_index(
        "ix_snapshots_video_created",
        "video_snapshots",
        ["video_id", "created_at"],
    )
    op.create_index(
        "ix_snapshots_created",
        "video_snapshots",
        ["created_at"],
    )


def downgrade():
    op.drop_table("video_snapshots")
    op.drop_table("videos")
    op.drop_table("users")
