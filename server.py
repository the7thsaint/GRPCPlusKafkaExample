import grpc
from concurrent import futures
import time
import json
from confluent_kafka import Producer

# Импорты сгенерированных файлов
import service_pb2
import service_pb2_grpc

# Конфигурация Kafka Producer
producer_conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(producer_conf)

# Callback для отправки сообщений
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Реализация gRPC сервиса
class ExampleServiceServicer(service_pb2_grpc.ExampleServiceServicer):
    def SayHello(self, request, context):
        response = f"Hello, {request.name}!"
        print(response)
        producer.produce('greetings', key="SayHello", value=json.dumps({"name": request.name, "response": response}), callback=delivery_report)
        producer.flush()
        return service_pb2.HelloResponse(message=response)

    def SayHelloWithAge(self, request, context):
        response = f"Hello, {request.name}! You are {request.age} years old."
        print(response)
        producer.produce('greetings', key="SayHelloWithAge", value=json.dumps({"name": request.name, "age": request.age, "response": response}), callback=delivery_report)
        producer.flush()
        return service_pb2.HelloResponse(message=response)

    def AddNumbers(self, request, context):
        result = request.num1 + request.num2
        print(f"Adding numbers: {request.num1} + {request.num2} = {result}")
        producer.produce('calculations', key="AddNumbers", value=json.dumps({"num1": request.num1, "num2": request.num2, "sum": result}), callback=delivery_report)
        producer.flush()
        return service_pb2.AddNumbersResponse(sum=result)

    def GreetByTime(self, request, context):
        if 0 <= request.hour < 12:
            response = "Good morning!"
        elif 12 <= request.hour < 18:
            response = "Good afternoon!"
        else:
            response = "Good evening!"

        print(f"Greeting based on time: Hour={request.hour}, Response={response}")
        producer.produce('greetings', key="GreetByTime", value=json.dumps({"hour": request.hour, "response": response}), callback=delivery_report)
        producer.flush()
        return service_pb2.HelloResponse(message=response)

# Запуск gRPC сервера
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_ExampleServiceServicer_to_server(ExampleServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Starting gRPC server on port 50051...")
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Stopping gRPC server...")
        server.stop(0)

if __name__ == '__main__':
    serve()
