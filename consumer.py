import os

from kafka import KafkaConsumer

kafka_url = os.environ.get("KAFKA_URL")
consumer = KafkaConsumer("my-topic", bootstrap_servers=[kafka_url])


try:
    while True:
        messages = consumer.poll(timeout_ms=1000)  # ожидание сообщения
        if not messages:  # если сообщений нет
            continue

        else:

            for key, msg in messages.items():
                msg = msg[0]
                print(
                    msg,
                    "%s:%d:%d: key=%s value=%s"
                    % (
                        msg.topic,
                        msg.partition,
                        msg.offset,
                        msg.key,
                        msg.value.decode("utf-8"),
                    ),
                )

except KeyboardInterrupt:
    pass
finally:
    consumer.close()

{
    TopicPartition(topic="my-topic", partition=0): [
        ConsumerRecord(
            topic="my-topic",
            partition=0,
            offset=42,
            timestamp=1721844809509,
            timestamp_type=0,
            key=None,
            value=b"Hello",
            headers=[],
            checksum=None,
            serialized_key_size=-1,
            serialized_value_size=5,
            serialized_header_size=-1,
        )
    ]
}
