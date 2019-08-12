from sqlalchemy import create_engine
from sqlalchemy import Column, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///mario_moves.db', echo=True)
Base = declarative_base()

class MarioPaths(Base):
    __tablename__ = "mario_moves"

    id = Column(DateTime, primary_key=True)
    grid = Column(String)
    moves = Column(String)
    time = Column(Float)

    def __repr__(self):
        return "{}".format(self.name)

# create tables
def create_table():
    Base.metadata.create_all(engine)