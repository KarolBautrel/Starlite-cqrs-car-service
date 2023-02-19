
from repository.car_repository import CarRepository
from models.car import Car
from services.redis_service.redis_handler import RedisHandler

class CarCommandService:

    def __init__(self):
        self.repository = CarRepository()
        self.redis_handler = RedisHandler()
    def update_car_price(self, car_id: int, data: dict[str, int]):
        event = {
            "routing_key":"car",
            "event":"price_changed",
            "price": data.get("change"),
            "id":car_id
        }
        self.redis_handler.publish_event(event)

    # def delete_car(self, car_id: int):
    #     car = self.check_car_exists(car_id)
    #     self.db_session.delete(car)
    #     self.db_session.commit()
    #     return True