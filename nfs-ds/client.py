from __future__ import print_function

import json
import grpc
import nfs.nfs_pb2_grpc as nfs_pb2_grpc
import nfs.nfs_pb2 as nfs_pb2


def make_message(message):
    return nfs_pb2.Path(path=message)


def list_dir(stub):
    message = make_message("C:/Users/ASUS/Desktop/projects/school/test_data")
    response = stub.list_dir(message)
    data = json.loads(response.string)
    for (dirpath, dirnames, filenames) in data:
        print("dirpath:", dirpath)
        print("dirnames:", dirnames)
        print("filenames:", filenames)
        print()


def copy_dir(stub):
    message = nfs_pb2.DoublePath(
        source="C:/Users/ASUS/Desktop/projects/school/test_data",
        sink="C:/Users/ASUS/Desktop/projects/school/test_data2"
    )
    response = stub.copy_dir(message)
    print(response.status, response.error)


def delete_dir(stub):
    message = nfs_pb2.Path(
        path="C:/Users/ASUS/Desktop/projects/school/test_data2"
    )
    response = stub.copy_dir(message)
    print(response.status, response.error)


def run(host: str, port: int):
    with grpc.insecure_channel(f"{host}:{port}") as channel:
        stub = nfs_pb2_grpc.NFSStub(channel)
        # list_dir(stub)
        # copy_dir(stub)
        delete_dir(stub)


if __name__ == "__main__":
    run(host="localhost", port=50051)
