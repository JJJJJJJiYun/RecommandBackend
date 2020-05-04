import sys
import traceback

from pb.common import common_pb2
from pb.item import item_pb2, item_pb2_grpc
from utils.common import *
from utils.db import MysqlPool
from utils.err_code import *


class ItemService(item_pb2_grpc.ItemServiceServicer):

    def GetItemList(self, request, context):
        try:
            pool = MysqlPool()
            item_type = item_pb2.ItemType.Name(request.item_type).lower()
            start, end = get_start_end_by_page_info(request.page, request.page_size)
            sql = 'select * from t_%s' % item_type
            res = pool.fetch_all(sql, ())
            items = []
            for item in res[start:end]:
                items.append(item_pb2.Item(id=str(item['id']), title=item['title'], content=item['content'],
                                           timestamp=str(item['created_at'])))
            return item_pb2.GetItemListReply(items=items, page_info=common_pb2.PageInfo(page=request.page,
                                                                                        page_size=request.page_size,
                                                                                        total=len(res),
                                                                                        total_page=get_total_page(
                                                                                            len(res),
                                                                                            request.page_size)))
        except:
            traceback.print_exc()
            context.set_code(ERR_CODE_GET_ITEM_LIST)
            context.set_details(sys.exc_info()[0])

    def GetItem(self, request, context):
        try:
            pool = MysqlPool()
            item_type = item_pb2.ItemType.Name(request.item_type).lower()
            table_name = 't_%s' % item_type
            sql = 'select * from ' + table_name + ' where id=%s'
            item = pool.fetch_one(sql, request.id)
            return item_pb2.Item(id=str(item['id']), title=item['title'], content=item['content'],
                                 timestamp=str(item['created_at']))
        except:
            traceback.print_exc()
            context.set_code(ERR_CODE_GET_ITEM_LIST)
            context.set_details(sys.exc_info()[0])
