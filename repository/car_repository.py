
from models.car import Car
from sqlalchemy.orm import sessionmaker
from db_config import engine
from events.car_events import car_events
from utils.car_utlis import CarUtils
class CarRepository:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.db_session = Session()
        self.car_utils = CarUtils()
    def save(self, car: Car):
        pass

    def get(self, id: int):
        car = Car(id)
        nested_event_list = [self.db_session.query(i).filter(i.car_id==id).all() for i in car_events ]
        flatten_event_list = self.car_utils.merge_events_to_one_list(nested_event_list)
        events = self.car_utils.sort_by_dates(flatten_event_list)
        if events is None:
            raise ValueError("User was not found!")
        for event in events:
            car.apply(event)
        return car


    def get_all(self):
        nested_events = [self.db_session.query(i).all() for i in car_events]
        prepared_car_list = self.car_utils.prepare_list_data(nested_events)
        car_list = []
        for id, events in prepared_car_list.items():
            car = Car(id)

            for event in events:
                car.apply(event)
            car_list.append(car)

        return car_list