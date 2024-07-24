from kafka import KafkaProducer

from .consumer import consumer

producer = KafkaProducer(bootstrap_servers=["localhost:9092"])
consumer.poll()


def send_message(msg):
    producer.send(topic="my-topic", value=msg.encode())
