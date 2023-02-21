from enum import Enum
import os
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")


class RedisKeys(Enum):
    EVENTS = "events_storage"


