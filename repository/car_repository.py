
from models.car import Car
from sqlalchemy.orm import sessionmaker
from db_config import engine
from events.car_events import car_events
from utils.car_utlis import CarUtils
from read_models.car import Car as ReadModelCar
class CarRepository:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.db_session = Session()
        self.car_utils = CarUtils()
    def save(self, car: Car):
        pass

    def get(self, id: int):
       possible_car = self.db_session.query(ReadModelCar).filter(ReadModelCar.id == id).first()

       if not possible_car:
            return None
       return possible_car

    def get_all(self):
        possible_car = self.db_session.query(ReadModelCar).all()
        return possible_car