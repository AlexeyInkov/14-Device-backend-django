import os

from dotenv.main import load_dotenv
from kafka import KafkaConsumer

load_dotenv()
kafka_url = os.environ.get("KAFKA_URL")


consumer = KafkaConsumer("my_topic", bootstrap_servers=kafka_url)


try:
    while True:
        messages = consumer.poll(timeout_ms=1000)  # ожидание сообщения
        if not messages:  # если сообщений нет
            continue

        else:

            for key, msg in messages.items():
                msg = msg[0]
                print(msg.topic, msg.value.decode("utf-8"))
                #     msg,
                #     "%s:%d:%d: key=%s value=%s"
                #     % (
                #         msg.topic,
                #         msg.partition,
                #         msg.offset,
                #         msg.key,
                #         msg.value.decode("utf-8"),
                #     ),
                # )

except KeyboardInterrupt:
    pass
finally:
    consumer.close()
