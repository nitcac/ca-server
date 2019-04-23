from sqlalchemy import Column, Integer, String, Sequence

from . import Base


class HTBResult(Base):
    __tablename__ = 'htb_results'
    
    result_id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    player_name = Column(String(32))
    point = Column(Integer)

    def __repr__(self):
        return f'<Model: htb_result, {{id: {self.result_id}, pt: {self.point}}}>'
