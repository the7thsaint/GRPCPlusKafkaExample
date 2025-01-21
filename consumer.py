from confluent_kafka import Consumer, KafkaError

# Конфигурация Kafka Consumer
consumer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_conf)

# Подписка на топики
consumer.subscribe(['greetings', 'calculations'])

def consume_messages():
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # Достигнут конец раздела
                    print(f"End of partition reached {msg.partition()}")
                else:
                    print(f"Error: {msg.error()}")
            else:
                # Вывод полученного сообщения
                print(f"Received message: {msg.value().decode('utf-8')}")
    except KeyboardInterrupt:
        print("Stopping consumer...")
    finally:
        consumer.close()

if __name__ == '__main__':
    print("Starting Kafka Consumer...")
    consume_messages()