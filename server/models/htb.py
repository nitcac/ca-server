from . import Base

import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql.functions import current_timestamp


class HTBResult(Base):
    __tablename__ = 'htb_results'
    
    result_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    player_name = Column(String(32))
    score = Column(Integer)
    created_at = Column(
        DateTime,
        nullable=False,
        server_default=current_timestamp()
    )

    def __repr__(self):
        return f'<Model: htb_result, {{id: {self.result_id}, score: {self.score}}}>'

    __str__ = __repr__

    def serialize(self):
        return {
            'result_id': self.result_id,
            'player_name': self.player_name,
            'score': self.score,
            'created_at': str(self.created_at)
        }
