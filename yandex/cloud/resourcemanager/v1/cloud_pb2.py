# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/resourcemanager/v1/cloud.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/resourcemanager/v1/cloud.proto',
  package='yandex.cloud.resourcemanager.v1',
  syntax='proto3',
  serialized_pb=_b('\n+yandex/cloud/resourcemanager/v1/cloud.proto\x12\x1fyandex.cloud.resourcemanager.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"f\n\x05\x43loud\x12\n\n\x02id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\tBUZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/resourcemanager/v1;resourcemanagerb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_CLOUD = _descriptor.Descriptor(
  name='Cloud',
  full_name='yandex.cloud.resourcemanager.v1.Cloud',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.resourcemanager.v1.Cloud.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.resourcemanager.v1.Cloud.created_at', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.resourcemanager.v1.Cloud.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.resourcemanager.v1.Cloud.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=215,
)

_CLOUD.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Cloud'] = _CLOUD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Cloud = _reflection.GeneratedProtocolMessageType('Cloud', (_message.Message,), dict(
  DESCRIPTOR = _CLOUD,
  __module__ = 'yandex.cloud.resourcemanager.v1.cloud_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.resourcemanager.v1.Cloud)
  ))
_sym_db.RegisterMessage(Cloud)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/resourcemanager/v1;resourcemanager'))
# @@protoc_insertion_point(module_scope)
