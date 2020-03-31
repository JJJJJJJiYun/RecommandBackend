# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from pb.recommand import recommand_pb2 as pb_dot_recommand_dot_recommand__pb2


class RecommandServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Recommand = channel.unary_unary(
        '/recommand.RecommandService/Recommand',
        request_serializer=pb_dot_recommand_dot_recommand__pb2.RecommandRequest.SerializeToString,
        response_deserializer=pb_dot_recommand_dot_recommand__pb2.RecommandReply.FromString,
        )
    self.SetDefaultRecommandItems = channel.unary_unary(
        '/recommand.RecommandService/SetDefaultRecommandItems',
        request_serializer=pb_dot_recommand_dot_recommand__pb2.SetDefaultRecommandItemsRequest.SerializeToString,
        response_deserializer=pb_dot_recommand_dot_recommand__pb2.EmptyMessage.FromString,
        )


class RecommandServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Recommand(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetDefaultRecommandItems(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RecommandServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Recommand': grpc.unary_unary_rpc_method_handler(
          servicer.Recommand,
          request_deserializer=pb_dot_recommand_dot_recommand__pb2.RecommandRequest.FromString,
          response_serializer=pb_dot_recommand_dot_recommand__pb2.RecommandReply.SerializeToString,
      ),
      'SetDefaultRecommandItems': grpc.unary_unary_rpc_method_handler(
          servicer.SetDefaultRecommandItems,
          request_deserializer=pb_dot_recommand_dot_recommand__pb2.SetDefaultRecommandItemsRequest.FromString,
          response_serializer=pb_dot_recommand_dot_recommand__pb2.EmptyMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'recommand.RecommandService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))