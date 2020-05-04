import time
from concurrent import futures
from threading import Thread

import grpc

from pb.item import item_pb2_grpc
from pb.recommand import recommand_pb2_grpc
from pb_imp.item_imp import ItemService
from pb_imp.recommand_imp import RecommandService
from service.kafka_consumer import consume_user_action

if __name__ == '__main__':
    # 启动 rpc 服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recommand_pb2_grpc.add_RecommandServiceServicer_to_server(RecommandService(), server)
    item_pb2_grpc.add_ItemServiceServicer_to_server(ItemService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    # 启动 kafka 消费者
    thread_kafka = Thread(target=consume_user_action)
    thread_kafka.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)  # one day in seconds
    except KeyboardInterrupt:
        server.stop(0)
