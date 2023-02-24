from services.redis_service.redis_service import RedisService
from configs import RedisKeys
import json


class RedisHandler:
    def __init__(self):
        self.redis_service = RedisService()

    def check_events(self, key):
        data = self.redis_service.lrange_list(key)
        if len(data)>0:

            return data
        return []
    def remove_event_from_list(self, element):

        self.redis_service.lrem_list(RedisKeys.EVENTS.value, json.dumps(element))
        print("Deleted")

    def publish_event(self, event):
        serialized_event = json.dumps(event, default=str)

        self.redis_service.lpush_to_list(key = RedisKeys.EVENTS.value,value= serialized_event )