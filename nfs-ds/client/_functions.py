import json
import os

import nfs.nfs_pb2 as nfs_pb2


class Functions:
    def __init__(self, stub):
        self.stub = stub

    def list_dir(self, path: str):
        message = nfs_pb2.Path(path=path)
        response = self.stub.list_dir(message)
        return {
            "root": response.path,
            "folders": json.loads(response.folders),
            "files": json.loads(response.files),
        }

    def copy_dir(self, source: str, sink: str):
        message = nfs_pb2.DoublePath(source=source, sink=sink)
        response = self.stub.copy_dir(message)
        return response.status

    def delete_dir(self, path: str):
        message = nfs_pb2.Path(path=path)
        response = self.stub.delete_dir(message)
        return response.status

    def get_file(self, source: str, sink: str):
        message = nfs_pb2.Path(path=source)
        flag = True
        try:
            response = self.stub.get_file(message)
            with open(sink, "wb") as fp:
                fp.write(response.content)
        except Exception as exc:
            print(exc)
            flag = False

        return flag

    def upload_file(self, source: str, sink: str):
        flag = True
        try:
            with open(source, "rb") as fp:
                content = fp.read()
            message = nfs_pb2.FileUpload(path=sink, content=content)
            response = self.stub.upload_file(message)
        except:
            flag = False
        return flag

    def create_dir(self, path: str):
        message = nfs_pb2.Path(path=path)
        response = self.stub.create_dir(message)
        return response.status

    def rename_dir(self, source: str, sink: str):
        message = nfs_pb2.DoublePath(source=source, sink=sink)
        response = self.stub.rename_dir(message)
        return response.status

    def move_dir(self, source: str, sink: str):
        message = nfs_pb2.DoublePath(source=source, sink=sink)
        response = self.stub.move_dir(message)
        return response.status

    def delete_file(self, path: str):
        message = nfs_pb2.Path(path=path)
        response = self.stub.delete_file(message)
        return response.status

    def rename_file(self, source: str, sink: str):
        message = nfs_pb2.DoublePath(source=source, sink=sink)
        response = self.stub.rename_file(message)
        return response.status

    def copy_file(self, source: str, sink: str):
        message = nfs_pb2.DoublePath(source=source, sink=sink)
        response = self.stub.copy_file(message)
        return response.status

    def move_file(self, source: str, sink: str):
        message = nfs_pb2.DoublePath(source=source, sink=sink)
        response = self.stub.move_file(message)
        return response.status

    def get_file_info(self, path: str) -> str:
        return "Not implemented yet"
