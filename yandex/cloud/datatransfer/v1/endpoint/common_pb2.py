# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datatransfer/v1/endpoint/common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/datatransfer/v1/endpoint/common.proto',
  package='yandex.cloud.datatransfer.v1.endpoint',
  syntax='proto3',
  serialized_options=b'\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2yandex/cloud/datatransfer/v1/endpoint/common.proto\x12%yandex.cloud.datatransfer.v1.endpoint\x1a\x1bgoogle/protobuf/empty.proto\" \n\x06Secret\x12\r\n\x03raw\x18\x01 \x01(\tH\x00\x42\x07\n\x05value\"\x86\x01\n\x07TLSMode\x12*\n\x08\x64isabled\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12\x43\n\x07\x65nabled\x18\x02 \x01(\x0b\x32\x30.yandex.cloud.datatransfer.v1.endpoint.TLSConfigH\x00\x42\n\n\x08tls_mode\"#\n\tTLSConfig\x12\x16\n\x0e\x63\x61_certificate\x18\x01 \x01(\t*h\n\x13ObjectTransferStage\x12%\n!OBJECT_TRANSFER_STAGE_UNSPECIFIED\x10\x00\x12\x0f\n\x0b\x42\x45\x46ORE_DATA\x10\x01\x12\x0e\n\nAFTER_DATA\x10\x02\x12\t\n\x05NEVER\x10\x03\x42\x7f\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpointb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_OBJECTTRANSFERSTAGE = _descriptor.EnumDescriptor(
  name='ObjectTransferStage',
  full_name='yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OBJECT_TRANSFER_STAGE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BEFORE_DATA', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AFTER_DATA', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NEVER', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=330,
  serialized_end=434,
)
_sym_db.RegisterEnumDescriptor(_OBJECTTRANSFERSTAGE)

ObjectTransferStage = enum_type_wrapper.EnumTypeWrapper(_OBJECTTRANSFERSTAGE)
OBJECT_TRANSFER_STAGE_UNSPECIFIED = 0
BEFORE_DATA = 1
AFTER_DATA = 2
NEVER = 3



_SECRET = _descriptor.Descriptor(
  name='Secret',
  full_name='yandex.cloud.datatransfer.v1.endpoint.Secret',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='raw', full_name='yandex.cloud.datatransfer.v1.endpoint.Secret.raw', index=0,
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
    _descriptor.OneofDescriptor(
      name='value', full_name='yandex.cloud.datatransfer.v1.endpoint.Secret.value',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=122,
  serialized_end=154,
)


_TLSMODE = _descriptor.Descriptor(
  name='TLSMode',
  full_name='yandex.cloud.datatransfer.v1.endpoint.TLSMode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='disabled', full_name='yandex.cloud.datatransfer.v1.endpoint.TLSMode.disabled', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='yandex.cloud.datatransfer.v1.endpoint.TLSMode.enabled', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='tls_mode', full_name='yandex.cloud.datatransfer.v1.endpoint.TLSMode.tls_mode',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=157,
  serialized_end=291,
)


_TLSCONFIG = _descriptor.Descriptor(
  name='TLSConfig',
  full_name='yandex.cloud.datatransfer.v1.endpoint.TLSConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ca_certificate', full_name='yandex.cloud.datatransfer.v1.endpoint.TLSConfig.ca_certificate', index=0,
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
  serialized_start=293,
  serialized_end=328,
)

_SECRET.oneofs_by_name['value'].fields.append(
  _SECRET.fields_by_name['raw'])
_SECRET.fields_by_name['raw'].containing_oneof = _SECRET.oneofs_by_name['value']
_TLSMODE.fields_by_name['disabled'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
_TLSMODE.fields_by_name['enabled'].message_type = _TLSCONFIG
_TLSMODE.oneofs_by_name['tls_mode'].fields.append(
  _TLSMODE.fields_by_name['disabled'])
_TLSMODE.fields_by_name['disabled'].containing_oneof = _TLSMODE.oneofs_by_name['tls_mode']
_TLSMODE.oneofs_by_name['tls_mode'].fields.append(
  _TLSMODE.fields_by_name['enabled'])
_TLSMODE.fields_by_name['enabled'].containing_oneof = _TLSMODE.oneofs_by_name['tls_mode']
DESCRIPTOR.message_types_by_name['Secret'] = _SECRET
DESCRIPTOR.message_types_by_name['TLSMode'] = _TLSMODE
DESCRIPTOR.message_types_by_name['TLSConfig'] = _TLSCONFIG
DESCRIPTOR.enum_types_by_name['ObjectTransferStage'] = _OBJECTTRANSFERSTAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Secret = _reflection.GeneratedProtocolMessageType('Secret', (_message.Message,), {
  'DESCRIPTOR' : _SECRET,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.common_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.Secret)
  })
_sym_db.RegisterMessage(Secret)

TLSMode = _reflection.GeneratedProtocolMessageType('TLSMode', (_message.Message,), {
  'DESCRIPTOR' : _TLSMODE,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.common_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.TLSMode)
  })
_sym_db.RegisterMessage(TLSMode)

TLSConfig = _reflection.GeneratedProtocolMessageType('TLSConfig', (_message.Message,), {
  'DESCRIPTOR' : _TLSCONFIG,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.common_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.TLSConfig)
  })
_sym_db.RegisterMessage(TLSConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
