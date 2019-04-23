from sqlalchemy import Column, Integer, String, Sequence

from . import Base


class GTBResult(Base):
    __tablename__ = 'gtb_results'
    
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    player_name = Column(String(32))
    pt = Column(Integer)

    def __repr__(self):
        return f'<Model: gtb_result, {{id: {self.id}, pt: {self.pt}}}>'
