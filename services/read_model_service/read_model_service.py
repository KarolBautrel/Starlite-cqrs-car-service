import json
import time

from services.redis_service.redis_handler import RedisHandler
from services.read_model_service.car_read_model_service import CarReadModelService
from services.read_model_service.order_read_model_service import OrderReadModelService
from configs import RedisKeys
class ReadModelChecker:

    def __init__(self):
        self.redis_handler = RedisHandler()
        self.car_read_model_service = CarReadModelService()
        self.order_read_model_service = OrderReadModelService()
        self.event_mapper = {
        "car": self.handle_car_event,
        "order": self.handle_order_event
        }
    def check_events(self):
        events = self.redis_handler.check_events(RedisKeys.EVENTS.value)
        if len(events)<=0:
            print("No new events_storage")
            return
        for event in events:
            routing_key = self.event_mapper[event.get("routing_key", None)]
            if routing_key:
                print(f"Event found with routing: {routing_key}")
                routing_key(event)
                self.redis_handler.remove_event_from_list(event)
    def handle_car_event(self, event):
        self.car_read_model_service.handle_event(event)

    def handle_order_event(self, event):
        print("UGA BUGA")

    def start_checking(self):
        print("Starting Checking events_storage")
        while True:
            time.sleep(1)
            self.check_events()