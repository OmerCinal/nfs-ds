import json
import grpc
import nfs.nfs_pb2_grpc as nfs_pb2_grpc
import nfs.nfs_pb2 as nfs_pb2
from _functions import Functions
from pick import pick


class Client:
    REFRESH = "> Refresh Servers"
    EXIT = "> Exit"

    def __init__(self):
        self._servers = {}

    def _scan_servers(self):
        self._servers["Localhost"] = {
            "host": "localhost",
            "port": 50051
        }

    def _connect_to_server(self, server_name: str):
        host = self._servers[server_name]["host"]
        port = self._servers[server_name]["port"]
        channel = grpc.insecure_channel(f"{host}:{port}")
        return nfs_pb2_grpc.NFSStub(channel), channel

    def start(self):
        self._scan_servers()
        while True:
            options = (
                list(self._servers.keys())
                + [self.REFRESH, self.EXIT]
            )
            option, index = pick(options, f"{len(self._servers)} servers found.")
            if option == self.EXIT:
                break
            elif option == self.REFRESH:
                self._scan_servers()
            else:
                stub, channel = self._connect_to_server(option)
                PageNavigator(stub).loop_pages()
                channel.close()



if __name__ == "__main__":
    client = Client(host="localhost", port=50051)
    client.start()
    client.kill()
