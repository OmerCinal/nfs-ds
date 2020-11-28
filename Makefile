
run.server:
	python nfs-ds/server.py

run.client:
	python nfs-ds/client.py

build.protobuf:
	python -m grpc_tools.protoc --proto_path=nfs-ds/nfs/ nfs.proto --python_out=./nfs-ds/nfs --grpc_python_out=./nfs-ds/nfs

