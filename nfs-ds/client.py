import json
import grpc
import nfs.nfs_pb2_grpc as nfs_pb2_grpc
import nfs.nfs_pb2 as nfs_pb2
from _functions import Functions
from pick import pick


class Client:
    EXIT = "Exit"
    OPTION_COVER_LEFT = ">"
    OPTION_COVER_RIGHT = "<"

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = nfs_pb2_grpc.NFSStub(self.channel)
        self.functions = Functions(self.stub)

        self.actions = {
            "Test": self._test
        }

    def _test(self):
        print("Hello World")

    def start(self):
        while True:
            title = "Select an option"
            options = list(self.actions.keys()) + [self.EXIT]
            option, index = pick(options, title)
            if option == self.EXIT:
                print("Goodbye")
                break
            else:
                self.actions[option]()

    def kill(self):
        self.channel.close()


if __name__ == "__main__":
    client = Client(host="localhost", port=50051)
    client.start()
    client.kill()
