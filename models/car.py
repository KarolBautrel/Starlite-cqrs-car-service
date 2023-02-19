from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from db_config import engine
from events.car_events import CarCreated, CarPriceChanged
from uuid import uuid4
from starlite import status_codes
from starlite import HTTPException
from datetime import datetime
from events.car_events import car_events
from utils.car_utlis import CarUtils
from read_models.car import Car as ReadModelCar
class Car:
    def __init__(self, id: int = None, car_id: int = None):
        self.car_utils = CarUtils()
        Session = sessionmaker(bind=engine)
        self.db_session = Session()
        self.id = id
        self.car_id: int = car_id
        self.model: str = None
        self.name: str = None
        self.year: int = None
        self.price: float = None
        self.created = None
        self.read_model = None
    def apply(self, event):
        if event.__class__.__name__ == "CarCreated":
            self.id = event.id

            self.car_id = event.car_id

            self.name = event.name

            self.price = event.price

            self.model = event.model

            self.year = event.year

            self.created = event.created

        if event.__class__.__name__ == "CarPriceChanged":
            if event.change <= 0:
                raise HTTPException(status_code=status_codes.HTTP_404_NOT_FOUND)
            self.price = event.change


    def check_if_car_exist(self, car_id):
        possible_car = self.db_session.query(Car).filter(Car.id == car_id).first()
        if possible_car:
            self.read_model = possible_car
            return None
        return True
    def create_car(
        self, id: int, car_id: int, model: str, name: str, year: int, price: float
    ):
        if not self.check_if_car_exist(car_id):
            return

        created_car = CarCreated(
            id=id,
            car_id=car_id,
            model=model,
            name=name,
            year=year,
            price=price,
            created=datetime.now(),
            sequence_number=1,
        )
        self.db_session.add(created_car)
        self.db_session.commit()
        self.apply(created_car)

    def change_car_price(self, change: int):
        nested_event_list = [self.db_session.query(i).filter(i.car_id == self.car_id).all() for i in car_events]
        sequence_number =len(self.car_utils.merge_events_to_one_list(nested_event_list))
        car_price_change = CarPriceChanged(
            id=str(uuid4()),
            car_id=self.car_id,
            change=change,
            created=datetime.now(),
            sequence_number=sequence_number,
        )
        self.db_session.add(car_price_change)
        self.db_session.commit()
        self.apply(car_price_change)
        if self.read_model:
            self.update_car_readmodel()


    def update_car_readmodel(self):
        self.read_model.model = self.model
        self.read_model.price = self.price
        self.read_model.year = self.year
        self.read_model.name = self.name
        self.db_session.commit(self.read_model)