### **Для начала работы:**

* Устновить пакетный менеджер pip и Python 3.12
* Запустить pip install grpcio grpcio-tools
* Запустить python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service.proto
* Запустить pip install confluent-kafka
* Установить docker на ПК
* Запускить docker-compose up
* Проверить, что контейнеры запустились без ошибок, в докер у контейнеров статус = Running
* Запустить сервер - python server.py


#### Далее в постман:
1. Выбрать gRPC
![Снимок экрана 2024-12-17 в 12.36.58.png](images%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-12-17%20%D0%B2%2012.36.58.png)
2. Выставить порт и выбрать прото файл из данного репозитория (service.proto)
![Снимок экрана 2024-12-17 в 12.37.59.png](images%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-12-17%20%D0%B2%2012.37.59.png)
3. Откроется список ручек
![Снимок экрана 2024-12-17 в 12.39.51.png](images%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-12-17%20%D0%B2%2012.39.51.png)

### Примеры запросов на ручки:

1. SayHelloWithAge:

`{
  "name": "Alice",
  "age": 30
}`

2. AddNumbers:

`{
  "num1": 10,
  "num2": 20
}`

3. GreetByTime:

`{
  "hour": 14
}`

### Как посмотреть это в Kafka:

1. Перейти на http://localhost:8081/ui/
2. После того, как вы сделаете запрос будут отображаться топики с сообщениями

### После завершения работ:

1. Остановить сервер во вкладке терминала - Сtrl + C
2. Остановить Docker - docker compose down
