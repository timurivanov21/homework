from sqlalchemy.orm import DeclarativeBase

from homework_project.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
