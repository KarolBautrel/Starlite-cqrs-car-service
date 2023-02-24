import redis
import json
from configs import REDIS_HOST, REDIS_PORT, RedisKeys


class RedisService:
    def __init__(self):
        self.service = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

    def set_cache_json(self, key, value):
        self.service.set(key, json.dumps(value))

    def set_cache_data(self, key, value):
        self.service.set(key, value)

    def get_cached_data(self, key):
        serialized_data = self.service.get(key)
        if not serialized_data:
            print("There is no key like this")
        deserialized_data = json.loads(serialized_data)
        return deserialized_data

    def lpush_to_list(self, key, value):

        self.service.lpush(key, value)

    def lrange_list(self, key):
        data = self.service.lrange(key, 0, -1)
        if len(data) <= 0:
            print("No data in redis")
            return []
        normalized_data = [json.loads(i) for i in data]
        return normalized_data

    def lrem_list(self,key,element):
        normalized_data = json.loads(element)
        serialized_data = json.dumps(normalized_data, separators=(',', ':'))

        self.service.lrem(key,0,serialized_data)
    def clear_list(self, key):

        return self.service.delete(key)
