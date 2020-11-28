from __future__ import print_function

import json
import grpc
import nfs.nfs_pb2_grpc as nfs_pb2_grpc
import nfs.nfs_pb2 as nfs_pb2


def make_message(message):
    return nfs_pb2.Path(path=message)


def send_message(stub):
    message = make_message("C:/Users/ASUS/Desktop/projects/school/test_data")
    response = stub.list_dir(message)
    data = json.loads(response.string)
    for (dirpath, dirnames, filenames) in data:
        print("dirpath:", dirpath)
        print("dirnames:", dirnames)
        print("filenames:", filenames)
        print()


def run(host: str, port: int):
    with grpc.insecure_channel(f"{host}:{port}") as channel:
        stub = nfs_pb2_grpc.NFSStub(channel)
        send_message(stub)


if __name__ == "__main__":
    run(host="localhost", port=50051)
