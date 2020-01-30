from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Participants(Base):

	__tablename__ = "users"
	participant_id = Column(Integer , primary_key=True)
	name = Column(String)
	psw = Column(String)
	image = Column(String)
	Nationality = Column(String)
	Instrument = Column(String)
	How_long = Column(Integer)
	Type = Column(String)
	email = Column(String)
	ph_n = Column(Integer)