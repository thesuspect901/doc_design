import redis
from .base_strategy import OutputStrategy

class RedisStrategy(OutputStrategy):

    def __init__(self):
        self.client = redis.Redis(host='localhost', port=6379, db=0)

    def output(self, data):
        for i, item in enumerate(data):
            key = f"data:{i}"
            self.client.set(key, str(item))

        print("✅ Дані записані в Redis")