from concurrent import futures

import os
import shutil
import json

import grpc
import nfs.nfs_pb2_grpc as nfs_pb2_grpc
import nfs.nfs_pb2 as nfs_pb2

from server._utils import copy_tree


class NfsService(nfs_pb2_grpc.NFSServicer):
    def _run_command(self, func, *args):
        flag = True
        error = ""
        try:
            print(func, ", ".join(args))
            func(*args)
        except Exception as exc:
            flag = False
            error = str(exc)
        print(error)
        return nfs_pb2.Status(status=flag, error=error)

    def list_dir(self, request, context):
        path = request.path
        if not path:
            path = os.path.expanduser("~")
        print(f"list_dir: path={path}")
        root, folders, files = next(os.walk(path))
        return nfs_pb2.FolderView(path=root, folders=json.dumps(folders), files=json.dumps(files))

    def create_dir(self, request, context):
        return self._run_command(os.mkdir, request.path)
        
    def delete_dir(self, request, context):
        return self._run_command(shutil.rmtree, request.path)

    def rename_dir(self, request, context):
        return self._run_command(os.rename, request.source, request.sink)
        
    def copy_dir(self, request, context):
        return self._run_command(copy_tree, request.source, request.sink)

    def move_dir(self, request, context):
        return self._run_command(shutil.move, request.source, request.sink)
        
    def get_file(self, request, context):
        with open(request.path, "rb") as fp:
            content = fp.read()
        return nfs_pb2.FileDownload(content=content)

    def upload_file(self, request, context):
        flag, error = True, ""
        if os.path.isfile(request.path):
            flag, error = False, "File already exists."
        else:
            with open(request.path, "wb") as fp:
                fp.write(request.content)

        return nfs_pb2.Status(status=flag, error=error)

    def delete_file(self, request, context):
        return self._run_command(os.remove, request.path)

    def rename_file(self, request, context):
        return self._run_command(os.rename, request.source, request.sink)

    def copy_file(self, request, context):
        return self._run_command(shutil.copyfile, request.source, request.sink)

    def move_file(self, request, context):
        return self._run_command(shutil.move, request.source, request.sink)


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
