from datetime import datetime

from starlite import HTTPException, status_codes

from repository.car_repository import CarRepository
from events_storage.car_events import CarBought, CarPriceChanged
from services.redis_service.redis_handler import RedisHandler
from sqlalchemy.orm import sessionmaker
from db_config import engine
from read_models.car import Car
class CarCommandService:

    def __init__(self):
        self.repository = CarRepository()
        self.redis_handler = RedisHandler()
        Session = sessionmaker(bind=engine)
        self.db_session = Session()
    def update_car_price(self, car_id: int, data: dict[str, int]):
        change = data.get("change", None)
        if change == None:
            raise HTTPException(status_code=status_codes.HTTP_404_NOT_FOUND)
        event = {
            "routing_key":"car",
            "event":"price_changed",
            "price": data.get("change"),
            "id":car_id
        }
        self.redis_handler.publish_event(event)
        self.db_session.add(CarPriceChanged(car_id=car_id, change = data.get("change"), created=datetime.utcnow()))
        self.db_session.commit()
    def buy_car(self, car_id:int):
        car = self.db_session.query(Car).filter(Car.id == car_id).first()

        event ={
            "routing_key":"order",
            "event": "create_order",
            "car":car.as_dict()
        }
        self.redis_handler.publish_event(event)
        self.db_session.add(CarBought(car_id=car_id, created=datetime.utcnow()))
        self.db_session.commit()
