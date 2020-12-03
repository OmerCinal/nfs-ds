import json
import os
import shutil
import string
from concurrent import futures

import grpc
import nfs.nfs_pb2 as nfs_pb2
import nfs.nfs_pb2_grpc as nfs_pb2_grpc
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
        print(f"list_dir: path='{path}'")
        if path:
            root, folders, files = next(os.walk(path))
        else:
            folders = [f'{d}:' for d in string.ascii_uppercase if os.path.exists(f'{d}:')]
            root, files = "", []

        return nfs_pb2.FolderView(
            path=root, folders=folders, files=files
        )

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


def serve(host: str, port: int, max_workers: int = 10):
    print(f"Starting the server with {max_workers} workers.")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    nfs_pb2_grpc.add_NFSServicer_to_server(NfsService(), server)
    server.add_insecure_port(f"{host}:{port}")
    server.start()
    print(f"Listening on port {port}.")
    try:
        server.wait_for_termination()
    except KeyboardInterrupt as exc:
        print("Stopped by user.")


if __name__ == "__main__":
    serve(host="0.0.0.0", port=50051)
