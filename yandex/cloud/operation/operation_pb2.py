# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/operation/operation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/operation/operation.proto',
  package='yandex.cloud.operation',
  syntax='proto3',
  serialized_options=_b('\n\032yandex.cloud.api.operationZDgithub.com/yandex-cloud/go-genproto/yandex/cloud/operation;operation'),
  serialized_pb=_b('\n&yandex/cloud/operation/operation.proto\x12\x16yandex.cloud.operation\x1a\x19google/protobuf/any.proto\x1a\x17google/rpc/status.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb0\x02\n\tOperation\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\ncreated_by\x18\x04 \x01(\t\x12/\n\x0bmodified_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04\x64one\x18\x06 \x01(\x08\x12&\n\x08metadata\x18\x07 \x01(\x0b\x32\x14.google.protobuf.Any\x12#\n\x05\x65rror\x18\x08 \x01(\x0b\x32\x12.google.rpc.StatusH\x00\x12(\n\x08response\x18\t \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\x08\n\x06resultBb\n\x1ayandex.cloud.api.operationZDgithub.com/yandex-cloud/go-genproto/yandex/cloud/operation;operationb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='yandex.cloud.operation.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.operation.Operation.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.operation.Operation.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.operation.Operation.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_by', full_name='yandex.cloud.operation.Operation.created_by', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modified_at', full_name='yandex.cloud.operation.Operation.modified_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='done', full_name='yandex.cloud.operation.Operation.done', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='yandex.cloud.operation.Operation.metadata', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='yandex.cloud.operation.Operation.error', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='yandex.cloud.operation.Operation.response', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='result', full_name='yandex.cloud.operation.Operation.result',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=152,
  serialized_end=456,
)

_OPERATION.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_OPERATION.fields_by_name['modified_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_OPERATION.fields_by_name['metadata'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_OPERATION.fields_by_name['error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_OPERATION.fields_by_name['response'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_OPERATION.oneofs_by_name['result'].fields.append(
  _OPERATION.fields_by_name['error'])
_OPERATION.fields_by_name['error'].containing_oneof = _OPERATION.oneofs_by_name['result']
_OPERATION.oneofs_by_name['result'].fields.append(
  _OPERATION.fields_by_name['response'])
_OPERATION.fields_by_name['response'].containing_oneof = _OPERATION.oneofs_by_name['result']
DESCRIPTOR.message_types_by_name['Operation'] = _OPERATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), {
  'DESCRIPTOR' : _OPERATION,
  '__module__' : 'yandex.cloud.operation.operation_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.operation.Operation)
  })
_sym_db.RegisterMessage(Operation)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
