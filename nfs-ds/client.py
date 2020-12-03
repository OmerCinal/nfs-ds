import json
from typing import Dict, List

import grpc
import nfs.nfs_pb2 as nfs_pb2
import nfs.nfs_pb2_grpc as nfs_pb2_grpc
from client._functions import Functions
from client._navigator import PageNavigator
from client._symbols import Symbols
from pick import pick


class Client:
    SEPARATOR = " := "
    BREAK = " "
    CANCEL = Symbols.make_option("Cancel")
    REFRESH = Symbols.make_option("Refresh Servers")
    MANUAL_CONNECT = Symbols.make_option("Add Server Manually")
    REMOVE_SERVER = Symbols.make_option("Remove Server")
    EXIT = Symbols.make_option("Exit")

    def __init__(self):
        self._servers = {}

    def _scan_servers(self):
        self._servers["Localhost"] = {"host": "localhost", "port": 50051}

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

    def _add_manual_server(self):
        server_name = input("Enter server name (alias).\n>")
        server_info = input("Enter the ip of the server. Example: [0.0.0.0:50051]\n>")
        host, port = server_info, "50051"
        if ":" in server_info:
            host, port = server_info.split(":")
        
        self._servers[server_name] = {
            "host": host,
            "port": port,
        }

    def _remove_server(self):
        while True:
            options = self._get_server_names() + [self.BREAK, self.CANCEL]
            option, index = pick(options, "Select a server to remove.")

            if option == self.BREAK:
                continue
            elif option == self.CANCEL:
                break
            else:
                server_name, _ = option.split(self.SEPARATOR)
                del self._servers[server_name]
                break


    def start(self):
        self._scan_servers()
        while True:
            options = self._get_server_names() + [self.BREAK, self.REFRESH, self.MANUAL_CONNECT, self.REMOVE_SERVER, self.EXIT]
            option, index = pick(options, f"{len(self._servers)} servers found.")
            if option == self.EXIT:
                break
            elif option == self.REFRESH:
                self._scan_servers()
            elif option == self.BREAK:
                continue
            elif option == self.MANUAL_CONNECT:
                self._add_manual_server()
            elif option == self.REMOVE_SERVER:
                self._remove_server()
            else:
                stub, channel = self._connect_to_server(option)
                PageNavigator(stub).loop_pages()
                channel.close()
                self._scan_servers()


if __name__ == "__main__":
    Client().start()
