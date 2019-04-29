from . import Base

from sqlalchemy import Column, String, Boolean


class Token(Base):
    __tablename__ = 'tokenes'

    unique_token = Column(
        String(64),
        primary_key=True,
        unique=True
    )
    authorized = Column(
        Boolean,
        default=False
    )

    def __str__(self):
        return f'<Token({authorized}): {unique_token}>'