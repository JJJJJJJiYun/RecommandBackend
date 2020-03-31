import sys

from pb.common import common_pb2
from pb.recommand import recommand_pb2_grpc, recommand_pb2
from service.recommand import recommand, set_default_recommand_items
from utils.err_code import *


class RecommandService(recommand_pb2_grpc.RecommandServiceServicer):

    def Recommand(self, request, context):
        try:
            recommand_items, total, total_page = recommand(request.user_id, request.page, request.page_size)
            return recommand_pb2.RecommandReply(item_ids=recommand_items,
                                                page_info=common_pb2.PageInfo(page=request.page,
                                                                              page_size=request.page_size,
                                                                              total=total,
                                                                              total_page=total_page))
        except:
            context.set_code(ERR_CODE_RECOMMAND)
            context.set_details(sys.exc_info()[0])

    def SetDefaultRecommandItems(self, request, context):
        try:
            set_default_recommand_items(request.item_ids)
        except:
            context.set_code(ERR_CODE_SET_DEFAULT_RECOMMAND_ITEMS)
            context.set_details(sys.exc_info()[0])
