from kafka import KafkaProducer
import json
from .base_strategy import OutputStrategy

class KafkaStrategy(OutputStrategy):

    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def output(self, data):
        for item in data:
            self.producer.send('lab4_topic', item)

        self.producer.flush()

        print("✅ Дані відправлені в Kafka")