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
  name='nfs.proto',
  package='nfs',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tnfs.proto\x12\x03nfs\"\'\n\x06Status\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"\x18\n\x06String\x12\x0e\n\x06string\x18\x01 \x01(\t\":\n\nFolderView\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0f\n\x07\x66olders\x18\x02 \x01(\t\x12\r\n\x05\x66iles\x18\x03 \x01(\t\"\x14\n\x04Path\x12\x0c\n\x04path\x18\x01 \x01(\t\"*\n\nDoublePath\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0c\n\x04sink\x18\x02 \x01(\t\"+\n\nFileUpload\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\"\x1f\n\x0c\x46ileDownload\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\x32\x92\x04\n\x03NFS\x12(\n\x08list_dir\x12\t.nfs.Path\x1a\x0f.nfs.FolderView\"\x00\x12&\n\ncreate_dir\x12\t.nfs.Path\x1a\x0b.nfs.Status\"\x00\x12&\n\ndelete_dir\x12\t.nfs.Path\x1a\x0b.nfs.Status\"\x00\x12,\n\nrename_dir\x12\x0f.nfs.DoublePath\x1a\x0b.nfs.Status\"\x00\x12*\n\x08\x63opy_dir\x12\x0f.nfs.DoublePath\x1a\x0b.nfs.Status\"\x00\x12*\n\x08move_dir\x12\x0f.nfs.DoublePath\x1a\x0b.nfs.Status\"\x00\x12*\n\x08get_file\x12\t.nfs.Path\x1a\x11.nfs.FileDownload\"\x00\x12-\n\x0bupload_file\x12\x0f.nfs.FileUpload\x1a\x0b.nfs.Status\"\x00\x12\'\n\x0b\x64\x65lete_file\x12\t.nfs.Path\x1a\x0b.nfs.Status\"\x00\x12-\n\x0brename_file\x12\x0f.nfs.DoublePath\x1a\x0b.nfs.Status\"\x00\x12+\n\tcopy_file\x12\x0f.nfs.DoublePath\x1a\x0b.nfs.Status\"\x00\x12+\n\tmove_file\x12\x0f.nfs.DoublePath\x1a\x0b.nfs.Status\"\x00\x62\x06proto3'
)




_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='nfs.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='nfs.Status.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='nfs.Status.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=57,
)


_STRING = _descriptor.Descriptor(
  name='String',
  full_name='nfs.String',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='string', full_name='nfs.String.string', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=83,
)


_FOLDERVIEW = _descriptor.Descriptor(
  name='FolderView',
  full_name='nfs.FolderView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='nfs.FolderView.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folders', full_name='nfs.FolderView.folders', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='files', full_name='nfs.FolderView.files', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=143,
)


_PATH = _descriptor.Descriptor(
  name='Path',
  full_name='nfs.Path',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='nfs.Path.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=165,
)


_DOUBLEPATH = _descriptor.Descriptor(
  name='DoublePath',
  full_name='nfs.DoublePath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='nfs.DoublePath.source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sink', full_name='nfs.DoublePath.sink', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=209,
)


_FILEUPLOAD = _descriptor.Descriptor(
  name='FileUpload',
  full_name='nfs.FileUpload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='nfs.FileUpload.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='nfs.FileUpload.content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=254,
)


_FILEDOWNLOAD = _descriptor.Descriptor(
  name='FileDownload',
  full_name='nfs.FileDownload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='nfs.FileDownload.content', index=0,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=256,
  serialized_end=287,
)

DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['String'] = _STRING
DESCRIPTOR.message_types_by_name['FolderView'] = _FOLDERVIEW
DESCRIPTOR.message_types_by_name['Path'] = _PATH
DESCRIPTOR.message_types_by_name['DoublePath'] = _DOUBLEPATH
DESCRIPTOR.message_types_by_name['FileUpload'] = _FILEUPLOAD
DESCRIPTOR.message_types_by_name['FileDownload'] = _FILEDOWNLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'nfs_pb2'
  # @@protoc_insertion_point(class_scope:nfs.Status)
  })
_sym_db.RegisterMessage(Status)

String = _reflection.GeneratedProtocolMessageType('String', (_message.Message,), {
  'DESCRIPTOR' : _STRING,
  '__module__' : 'nfs_pb2'
  # @@protoc_insertion_point(class_scope:nfs.String)
  })
_sym_db.RegisterMessage(String)

FolderView = _reflection.GeneratedProtocolMessageType('FolderView', (_message.Message,), {
  'DESCRIPTOR' : _FOLDERVIEW,
  '__module__' : 'nfs_pb2'
  # @@protoc_insertion_point(class_scope:nfs.FolderView)
  })
_sym_db.RegisterMessage(FolderView)

Path = _reflection.GeneratedProtocolMessageType('Path', (_message.Message,), {
  'DESCRIPTOR' : _PATH,
  '__module__' : 'nfs_pb2'
  # @@protoc_insertion_point(class_scope:nfs.Path)
  })
_sym_db.RegisterMessage(Path)

DoublePath = _reflection.GeneratedProtocolMessageType('DoublePath', (_message.Message,), {
  'DESCRIPTOR' : _DOUBLEPATH,
  '__module__' : 'nfs_pb2'
  # @@protoc_insertion_point(class_scope:nfs.DoublePath)
  })
_sym_db.RegisterMessage(DoublePath)

FileUpload = _reflection.GeneratedProtocolMessageType('FileUpload', (_message.Message,), {
  'DESCRIPTOR' : _FILEUPLOAD,
  '__module__' : 'nfs_pb2'
  # @@protoc_insertion_point(class_scope:nfs.FileUpload)
  })
_sym_db.RegisterMessage(FileUpload)

FileDownload = _reflection.GeneratedProtocolMessageType('FileDownload', (_message.Message,), {
  'DESCRIPTOR' : _FILEDOWNLOAD,
  '__module__' : 'nfs_pb2'
  # @@protoc_insertion_point(class_scope:nfs.FileDownload)
  })
_sym_db.RegisterMessage(FileDownload)



_NFS = _descriptor.ServiceDescriptor(
  name='NFS',
  full_name='nfs.NFS',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=290,
  serialized_end=820,
  methods=[
  _descriptor.MethodDescriptor(
    name='list_dir',
    full_name='nfs.NFS.list_dir',
    index=0,
    containing_service=None,
    input_type=_PATH,
    output_type=_FOLDERVIEW,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='create_dir',
    full_name='nfs.NFS.create_dir',
    index=1,
    containing_service=None,
    input_type=_PATH,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='delete_dir',
    full_name='nfs.NFS.delete_dir',
    index=2,
    containing_service=None,
    input_type=_PATH,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='rename_dir',
    full_name='nfs.NFS.rename_dir',
    index=3,
    containing_service=None,
    input_type=_DOUBLEPATH,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='copy_dir',
    full_name='nfs.NFS.copy_dir',
    index=4,
    containing_service=None,
    input_type=_DOUBLEPATH,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='move_dir',
    full_name='nfs.NFS.move_dir',
    index=5,
    containing_service=None,
    input_type=_DOUBLEPATH,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_file',
    full_name='nfs.NFS.get_file',
    index=6,
    containing_service=None,
    input_type=_PATH,
    output_type=_FILEDOWNLOAD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='upload_file',
    full_name='nfs.NFS.upload_file',
    index=7,
    containing_service=None,
    input_type=_FILEUPLOAD,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='delete_file',
    full_name='nfs.NFS.delete_file',
    index=8,
    containing_service=None,
    input_type=_PATH,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='rename_file',
    full_name='nfs.NFS.rename_file',
    index=9,
    containing_service=None,
    input_type=_DOUBLEPATH,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='copy_file',
    full_name='nfs.NFS.copy_file',
    index=10,
    containing_service=None,
    input_type=_DOUBLEPATH,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='move_file',
    full_name='nfs.NFS.move_file',
    index=11,
    containing_service=None,
    input_type=_DOUBLEPATH,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_NFS)

DESCRIPTOR.services_by_name['NFS'] = _NFS

# @@protoc_insertion_point(module_scope)