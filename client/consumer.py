#!/usr/bin/python

from kafka import KafkaConsumer
from json import loads
import json


class Consumer:
    def __init__(self):
        pass

    def run(self):
        print("Running")
        consumer = KafkaConsumer(
            "dbserver1.inventory.customers",
            bootstrap_servers=["localhost:9092"]
            # consumer_timeout_ms=1000,
        )
        print("Running 2")
        for message in consumer:
            try:
                message_value = json.loads(message.value)
                print(message_value['payload'])
            except Exception as e:
                print(message)
                print(e)


client = Consumer()
client.run()