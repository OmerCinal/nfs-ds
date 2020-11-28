from concurrent import futures

import os
import json

import grpc
import nfs.nfs_pb2_grpc as nfs_pb2_grpc
import nfs.nfs_pb2 as nfs_pb2


class NfsService(nfs_pb2_grpc.NFSServicer):
    def list_dir(self, request, context):
        path = request.path
        print(f"list_dir: path={path}")
        data = list(os.walk(path))
        return nfs_pb2.String(string=json.dumps(data))

    # def create_dir(self, request, context):
    #     return "Succesful"

    # def delete_dir(self, request, context):
    #     return "Succesful"

    # def rename_dir(self, request, context):
    #     return "Succesful"

    # def copy_dir(self, request, context):
    #     return "Succesful"

    # def move_dir(self, request, context):
    #     return "Succesful"

    # def get_file(self, request, context):
    #     return "Succesful"

    # def create_file(self, request, context):
    #     return "Succesful"

    # def delete_file(self, request, context):
    #     return "Succesful"

    # def rename_file(self, request, context):
    #     return "Succesful"

    # def copy_file(self, request, context):
    #     return "Succesful"

    # def move_file(self, request, context):
    #     return "Succesful"


def serve(port: int, max_workers: int = 10):
    print(f"Starting the server with {max_workers} workers.")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    nfs_pb2_grpc.add_NFSServicer_to_server(NfsService(), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(f"Listening on port {port}.")
    try:
        server.wait_for_termination()
    except KeyboardInterrupt as exc:
        print("Stopped by user.")


if __name__ == "__main__":
    serve(port=50051)
