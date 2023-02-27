from events.car_events import CarEvent
from services.redis_service.redis_handler import RedisHandler


class CarCommandService:

    def __init__(self):
        self.redis_handler = RedisHandler()
        self.car_events = CarEvent()

    def update_car_price(self, car_id: int, data: dict[str, int]):
        event = self.car_events.create_price_changed_car_event(car_id, data)
        self.redis_handler.publish_event(event)

    def buy_car(self, car_id: int):
        event = self.car_events.create_bought_car_event(car_id)
        self.redis_handler.publish_event(event)

    def cancel_car(self, car_id: int):
        event = self.car_events.create_car_cancelled_event(car_id)
        self.redis_handler.publish_event(event)
