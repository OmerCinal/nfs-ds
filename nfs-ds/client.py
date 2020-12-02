import json
import grpc
import nfs.nfs_pb2_grpc as nfs_pb2_grpc
import nfs.nfs_pb2 as nfs_pb2
from client._functions import Functions
from pick import pick
from typing import List, Dict
from client._symbols import Symbols
from client._navigator import PageNavigator


class Client:
    SEPARATOR = " := "
    BREAK = " "
    REFRESH = Symbols.make_option("Refresh Servers")
    EXIT = Symbols.make_option("Exit")

    def __init__(self):
        self._servers = {}

    def _scan_servers(self):
        self._servers["Localhost"] = {
            "host": "localhost",
            "port": 50051
        }

    def _connect_to_server(self, server_name: str):
        server_name, _ = server_name.split(self.SEPARATOR)
        host = self._servers[server_name]["host"]
        port = self._servers[server_name]["port"]
        channel = grpc.insecure_channel(f"{host}:{port}")
        return nfs_pb2_grpc.NFSStub(channel), channel

    def _get_server_names(self) -> List:
        server_names = []
        for name, params in self._servers.items():
            host, port = params["host"], params["port"]
            server_names.append(f"{name}{self.SEPARATOR}({host}:{port})")
        return sorted(server_names)

    def start(self):
        self._scan_servers()
        while True:
            options = (
                self._get_server_names()
                + [self.BREAK, self.REFRESH, self.EXIT]
            )
            option, index = pick(options, f"{len(self._servers)} servers found.")
            if option == self.EXIT:
                break
            elif option == self.REFRESH:
                self._scan_servers()
            elif option == self.BREAK:
                continue
            else:
                stub, channel = self._connect_to_server(option)
                PageNavigator(stub).loop_pages()
                channel.close()
                self._scan_servers()



if __name__ == "__main__":
    client = Client()
    client.start()
