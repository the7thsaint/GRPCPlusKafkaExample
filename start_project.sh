#!/bin/bash

# Определение архитектуры машины
if grep -qi microsoft /proc/version 2>/dev/null; then
    echo "WSL (Windows Subsystem for Linux) обнаружен."
    ARCH="amd64"
else
    ARCH=$(uname -m)
fi

# Логи
echo "Определение архитектуры машины..."
echo "Архитектура: $ARCH"

# Генерация docker-compose.override.yml
echo "Создание docker-compose.override.yml с учетом архитектуры..."

if [ "$ARCH" == "arm64" ]; then
    cat > docker-compose.override.yml <<EOL
version: '3.8'

services:
  zookeeper:
    image: bitnami/zookeeper:latest
    platform: linux/arm64
    environment:
      ALLOW_ANONYMOUS_LOGIN: "yes"
    ports:
      - "2181:2181"

  kafka:
    image: bitnami/kafka:latest
    platform: linux/arm64
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_CFG_LISTENERS: PLAINTEXT://:9092,PLAINTEXT_INTERNAL://:29092
      KAFKA_CFG_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092,PLAINTEXT_INTERNAL://kafka:29092
      KAFKA_CFG_AUTO_CREATE_TOPICS_ENABLE: "true"
    depends_on:
      - zookeeper

  kafka-ui:
    image: provectuslabs/kafka-ui:latest
    platform: linux/amd64
    ports:
      - "8081:8080"
    environment:
      KAFKA_CLUSTERS_0_NAME: local
      KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS: kafka:29092
    depends_on:
      - kafka
EOL
else
    cat > docker-compose.override.yml <<EOL
version: '3.8'

services:
  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    platform: linux/amd64
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000
    ports:
      - "2181:2181"

  kafka:
    image: confluentinc/cp-kafka:latest
    platform: linux/amd64
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_INTERNAL:PLAINTEXT
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092,PLAINTEXT_INTERNAL://kafka:29092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
    depends_on:
      - zookeeper

  kafka-ui:
    image: provectuslabs/kafka-ui:latest
    platform: linux/amd64
    ports:
      - "8081:8080"
    environment:
      KAFKA_CLUSTERS_0_NAME: local
      KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS: kafka:29092
    depends_on:
      - kafka
EOL
fi

echo "docker-compose.override.yml создан!"

# Запуск Docker Compose
echo "Запуск Docker Compose..."
docker-compose up -d

# Проверка состояния контейнеров
echo "Состояние контейнеров:"
docker-compose ps
