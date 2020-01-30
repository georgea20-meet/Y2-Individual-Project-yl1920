from model import Base, Participants

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///students.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_participant(name, psw, image, Nationality, Instrument, How_long, Type, email, ph_n):

	particiant = Participants(
		name=name,
		psw=psw,
		image = image,
		Instrument=Instrument,
		Nationality = Nationality,
		How_long=How_long,
		Type=Type,
		email=email,
		ph_n=ph_n)
	session.add(particiant)
	session.commit()

def query_by_instrument(Instrument):

	participant = session.query(Participants).filter_by(Instrument=Instrument).all()
	print(participant)
	return participant 


def delete():
	return session.query(Participants).delete()

def timeUpdate(email,time):
	person = session.query(Participants).filter_by(email=email).first()
	person.How_long = time

	session.commit()
