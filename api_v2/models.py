from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class EventBought(Base):
    __tablename__ = 'indexer_eventbought'
    id = Column(Integer, primary_key=True)
    buyer_address = Column(String)
    amount = Column(String)
    tx = Column(String)
