#!/usr/bin/python

from argparse import ArgumentParser
from kafka import KafkaConsumer
from json import loads
import logging
import json
import sys

sample_topic = "dbserver1.inventory.customers"
sample_kafka_host = "localhost:9092"
class Consumer:
    def __init__(self, kafka_host, kafka_topic):
        # logging.basicConfig(level=logging.DEBUG)
        logging.info('Initializing')

        self.kafka_host = kafka_host
        self.kafka_topic = kafka_topic

    def run(self):
        consumer = KafkaConsumer(
           self.kafka_topic,
            bootstrap_servers=[self.kafka_host]
        )
        logging.info(f"Listening topic {self.kafka_topic}")
        for message in consumer:
            self.print_payload(message)

    def print_payload(self, message):
        try:
            message_value = json.loads(message.value)
            pretty_payload = json.dumps(message_value['payload'], indent=4, sort_keys=True)
            print(pretty_payload)
        except Exception as e:
            logging.error(e)

try:
    parser = ArgumentParser(description='Rename songs')
    parser.add_argument('--h', '--host', help='kafka host', type=str)
    parser.add_argument('--t', '--topic', help='kafka topic', type=str)

    args = parser.parse_args()  # GET PARAMS
    client = Consumer(args.h, args.t)
    print(args)
    client.run()
except:
    logging.error("Parameters not found")
    logging.info(f"Use: python3 consumer.py --h {sample_kafka_host} --t {sample_topic}")