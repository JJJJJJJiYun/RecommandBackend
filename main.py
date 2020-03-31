import time
from concurrent import futures

import grpc

from pb.recommand import recommand_pb2_grpc
from pb_imp.recommand_imp import RecommandService

if __name__ == '__main__':
    # 启动 rpc 服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recommand_pb2_grpc.add_RecommandServiceServicer_to_server(RecommandService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)  # one day in seconds
    except KeyboardInterrupt:
        server.stop(0)
