# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import helloworld_pb2 as helloworld__pb2

GRPC_GENERATED_VERSION = '1.66.2'
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
        + f' but the generated code in helloworld_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class HelloWorldStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHelloStream = channel.unary_stream(
                '/HelloWorld/SayHelloStream',
                request_serializer=helloworld__pb2.HelloRequest.SerializeToString,
                response_deserializer=helloworld__pb2.HelloReply.FromString,
                _registered_method=True)


class HelloWorldServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SayHelloStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HelloWorldServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHelloStream': grpc.unary_stream_rpc_method_handler(
                    servicer.SayHelloStream,
                    request_deserializer=helloworld__pb2.HelloRequest.FromString,
                    response_serializer=helloworld__pb2.HelloReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'HelloWorld', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('HelloWorld', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class HelloWorld(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SayHelloStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/HelloWorld/SayHelloStream',
            helloworld__pb2.HelloRequest.SerializeToString,
            helloworld__pb2.HelloReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
