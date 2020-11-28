
run.server:
	python server.py

run.client:
	python client.py

build.protobuf:
	python -m grpc_tools.protoc --proto_path=nfs-ds/bidirectional/ bidirectional.proto --python_out=./nfs-ds/bidirectional --grpc_python_out=./nfs-ds/bidirectional

