from models import BookingRequest
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import BookingDB

Base = declarative_base()

# Set up the database connection
engine = create_engine('sqlite:///booking.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def save_booking(booking: BookingRequest):
    # Create a new session and add the booking to it
    session = Session()
    db_booking = BookingDB(**booking.dict())
    session.add(db_booking)

    session.commit()
    session.close()

    return db_booking
