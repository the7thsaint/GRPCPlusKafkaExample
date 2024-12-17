# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import service_pb2 as service__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ExampleServiceStub(object):
    """Сервис с несколькими методами
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/example.ExampleService/SayHello',
                request_serializer=service__pb2.HelloRequest.SerializeToString,
                response_deserializer=service__pb2.HelloResponse.FromString,
                _registered_method=True)
        self.SayHelloWithAge = channel.unary_unary(
                '/example.ExampleService/SayHelloWithAge',
                request_serializer=service__pb2.HelloWithAgeRequest.SerializeToString,
                response_deserializer=service__pb2.HelloResponse.FromString,
                _registered_method=True)
        self.AddNumbers = channel.unary_unary(
                '/example.ExampleService/AddNumbers',
                request_serializer=service__pb2.AddNumbersRequest.SerializeToString,
                response_deserializer=service__pb2.AddNumbersResponse.FromString,
                _registered_method=True)
        self.GreetByTime = channel.unary_unary(
                '/example.ExampleService/GreetByTime',
                request_serializer=service__pb2.TimeOfDayRequest.SerializeToString,
                response_deserializer=service__pb2.HelloResponse.FromString,
                _registered_method=True)


class ExampleServiceServicer(object):
    """Сервис с несколькими методами
    """

    def SayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHelloWithAge(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddNumbers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GreetByTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExampleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=service__pb2.HelloRequest.FromString,
                    response_serializer=service__pb2.HelloResponse.SerializeToString,
            ),
            'SayHelloWithAge': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHelloWithAge,
                    request_deserializer=service__pb2.HelloWithAgeRequest.FromString,
                    response_serializer=service__pb2.HelloResponse.SerializeToString,
            ),
            'AddNumbers': grpc.unary_unary_rpc_method_handler(
                    servicer.AddNumbers,
                    request_deserializer=service__pb2.AddNumbersRequest.FromString,
                    response_serializer=service__pb2.AddNumbersResponse.SerializeToString,
            ),
            'GreetByTime': grpc.unary_unary_rpc_method_handler(
                    servicer.GreetByTime,
                    request_deserializer=service__pb2.TimeOfDayRequest.FromString,
                    response_serializer=service__pb2.HelloResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'example.ExampleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('example.ExampleService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ExampleService(object):
    """Сервис с несколькими методами
    """

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/example.ExampleService/SayHello',
            service__pb2.HelloRequest.SerializeToString,
            service__pb2.HelloResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SayHelloWithAge(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/example.ExampleService/SayHelloWithAge',
            service__pb2.HelloWithAgeRequest.SerializeToString,
            service__pb2.HelloResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddNumbers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/example.ExampleService/AddNumbers',
            service__pb2.AddNumbersRequest.SerializeToString,
            service__pb2.AddNumbersResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GreetByTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/example.ExampleService/GreetByTime',
            service__pb2.TimeOfDayRequest.SerializeToString,
            service__pb2.HelloResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)