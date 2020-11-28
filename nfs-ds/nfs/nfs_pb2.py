# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nfs.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="nfs.proto",
    package="nfs",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\tnfs.proto\x12\x03nfs"\x18\n\x06String\x12\x0e\n\x06string\x18\x01 \x01(\t"\x14\n\x04Path\x12\x0c\n\x04path\x18\x01 \x01(\t"*\n\nDoublePath\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0c\n\x04sink\x18\x02 \x01(\t">\n\nReadResult\x12\x11\n\tbytesread\x18\x01 \x01(\x05\x12\x0e\n\x06\x62uffer\x18\x02 \x01(\x0c\x12\r\n\x05\x65rror\x18\x03 \x01(\x05\x32\x82\x04\n\x03NFS\x12$\n\x08list_dir\x12\t.nfs.Path\x1a\x0b.nfs.String"\x00\x12&\n\ncreate_dir\x12\t.nfs.Path\x1a\x0b.nfs.String"\x00\x12&\n\ndelete_dir\x12\t.nfs.Path\x1a\x0b.nfs.String"\x00\x12,\n\nrename_dir\x12\x0f.nfs.DoublePath\x1a\x0b.nfs.String"\x00\x12*\n\x08\x63opy_dir\x12\x0f.nfs.DoublePath\x1a\x0b.nfs.String"\x00\x12*\n\x08move_dir\x12\x0f.nfs.DoublePath\x1a\x0b.nfs.String"\x00\x12$\n\x08get_file\x12\t.nfs.Path\x1a\x0b.nfs.String"\x00\x12\'\n\x0b\x63reate_file\x12\t.nfs.Path\x1a\x0b.nfs.String"\x00\x12\'\n\x0b\x64\x65lete_file\x12\t.nfs.Path\x1a\x0b.nfs.String"\x00\x12-\n\x0brename_file\x12\x0f.nfs.DoublePath\x1a\x0b.nfs.String"\x00\x12+\n\tcopy_file\x12\x0f.nfs.DoublePath\x1a\x0b.nfs.String"\x00\x12+\n\tmove_file\x12\x0f.nfs.DoublePath\x1a\x0b.nfs.String"\x00\x62\x06proto3',
)


_STRING = _descriptor.Descriptor(
    name="String",
    full_name="nfs.String",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="string",
            full_name="nfs.String.string",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=18,
    serialized_end=42,
)


_PATH = _descriptor.Descriptor(
    name="Path",
    full_name="nfs.Path",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="path",
            full_name="nfs.Path.path",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=44,
    serialized_end=64,
)


_DOUBLEPATH = _descriptor.Descriptor(
    name="DoublePath",
    full_name="nfs.DoublePath",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="source",
            full_name="nfs.DoublePath.source",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="sink",
            full_name="nfs.DoublePath.sink",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=66,
    serialized_end=108,
)


_READRESULT = _descriptor.Descriptor(
    name="ReadResult",
    full_name="nfs.ReadResult",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="bytesread",
            full_name="nfs.ReadResult.bytesread",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="buffer",
            full_name="nfs.ReadResult.buffer",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="error",
            full_name="nfs.ReadResult.error",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=110,
    serialized_end=172,
)

DESCRIPTOR.message_types_by_name["String"] = _STRING
DESCRIPTOR.message_types_by_name["Path"] = _PATH
DESCRIPTOR.message_types_by_name["DoublePath"] = _DOUBLEPATH
DESCRIPTOR.message_types_by_name["ReadResult"] = _READRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

String = _reflection.GeneratedProtocolMessageType(
    "String",
    (_message.Message,),
    {
        "DESCRIPTOR": _STRING,
        "__module__": "nfs_pb2"
        # @@protoc_insertion_point(class_scope:nfs.String)
    },
)
_sym_db.RegisterMessage(String)

Path = _reflection.GeneratedProtocolMessageType(
    "Path",
    (_message.Message,),
    {
        "DESCRIPTOR": _PATH,
        "__module__": "nfs_pb2"
        # @@protoc_insertion_point(class_scope:nfs.Path)
    },
)
_sym_db.RegisterMessage(Path)

DoublePath = _reflection.GeneratedProtocolMessageType(
    "DoublePath",
    (_message.Message,),
    {
        "DESCRIPTOR": _DOUBLEPATH,
        "__module__": "nfs_pb2"
        # @@protoc_insertion_point(class_scope:nfs.DoublePath)
    },
)
_sym_db.RegisterMessage(DoublePath)

ReadResult = _reflection.GeneratedProtocolMessageType(
    "ReadResult",
    (_message.Message,),
    {
        "DESCRIPTOR": _READRESULT,
        "__module__": "nfs_pb2"
        # @@protoc_insertion_point(class_scope:nfs.ReadResult)
    },
)
_sym_db.RegisterMessage(ReadResult)


_NFS = _descriptor.ServiceDescriptor(
    name="NFS",
    full_name="nfs.NFS",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=175,
    serialized_end=689,
    methods=[
        _descriptor.MethodDescriptor(
            name="list_dir",
            full_name="nfs.NFS.list_dir",
            index=0,
            containing_service=None,
            input_type=_PATH,
            output_type=_STRING,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="create_dir",
            full_name="nfs.NFS.create_dir",
            index=1,
            containing_service=None,
            input_type=_PATH,
            output_type=_STRING,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="delete_dir",
            full_name="nfs.NFS.delete_dir",
            index=2,
            containing_service=None,
            input_type=_PATH,
            output_type=_STRING,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="rename_dir",
            full_name="nfs.NFS.rename_dir",
            index=3,
            containing_service=None,
            input_type=_DOUBLEPATH,
            output_type=_STRING,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="copy_dir",
            full_name="nfs.NFS.copy_dir",
            index=4,
            containing_service=None,
            input_type=_DOUBLEPATH,
            output_type=_STRING,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="move_dir",
            full_name="nfs.NFS.move_dir",
            index=5,
            containing_service=None,
            input_type=_DOUBLEPATH,
            output_type=_STRING,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="get_file",
            full_name="nfs.NFS.get_file",
            index=6,
            containing_service=None,
            input_type=_PATH,
            output_type=_STRING,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="create_file",
            full_name="nfs.NFS.create_file",
            index=7,
            containing_service=None,
            input_type=_PATH,
            output_type=_STRING,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="delete_file",
            full_name="nfs.NFS.delete_file",
            index=8,
            containing_service=None,
            input_type=_PATH,
            output_type=_STRING,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="rename_file",
            full_name="nfs.NFS.rename_file",
            index=9,
            containing_service=None,
            input_type=_DOUBLEPATH,
            output_type=_STRING,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="copy_file",
            full_name="nfs.NFS.copy_file",
            index=10,
            containing_service=None,
            input_type=_DOUBLEPATH,
            output_type=_STRING,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="move_file",
            full_name="nfs.NFS.move_file",
            index=11,
            containing_service=None,
            input_type=_DOUBLEPATH,
            output_type=_STRING,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_NFS)

DESCRIPTOR.services_by_name["NFS"] = _NFS

# @@protoc_insertion_point(module_scope)