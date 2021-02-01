# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/lockbox/v1/payload_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.lockbox.v1 import payload_pb2 as yandex_dot_cloud_dot_lockbox_dot_v1_dot_payload__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/lockbox/v1/payload_service.proto',
  package='yandex.cloud.lockbox.v1',
  syntax='proto3',
  serialized_options=b'\n\033yandex.cloud.api.lockbox.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/lockbox/v1;lockbox',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-yandex/cloud/lockbox/v1/payload_service.proto\x12\x17yandex.cloud.lockbox.v1\x1a\x1cgoogle/api/annotations.proto\x1a%yandex/cloud/lockbox/v1/payload.proto\x1a\x1dyandex/cloud/validation.proto\"R\n\x11GetPayloadRequest\x12\x1f\n\tsecret_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1c\n\nversion_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=502\x97\x01\n\x0ePayloadService\x12\x84\x01\n\x03Get\x12*.yandex.cloud.lockbox.v1.GetPayloadRequest\x1a .yandex.cloud.lockbox.v1.Payload\"/\x82\xd3\xe4\x93\x02)\x12\'/lockbox/v1/secrets/{secret_id}/payloadBb\n\x1byandex.cloud.api.lockbox.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/lockbox/v1;lockboxb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_lockbox_dot_v1_dot_payload__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_GETPAYLOADREQUEST = _descriptor.Descriptor(
  name='GetPayloadRequest',
  full_name='yandex.cloud.lockbox.v1.GetPayloadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='secret_id', full_name='yandex.cloud.lockbox.v1.GetPayloadRequest.secret_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version_id', full_name='yandex.cloud.lockbox.v1.GetPayloadRequest.version_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=174,
  serialized_end=256,
)

DESCRIPTOR.message_types_by_name['GetPayloadRequest'] = _GETPAYLOADREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetPayloadRequest = _reflection.GeneratedProtocolMessageType('GetPayloadRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPAYLOADREQUEST,
  '__module__' : 'yandex.cloud.lockbox.v1.payload_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.lockbox.v1.GetPayloadRequest)
  })
_sym_db.RegisterMessage(GetPayloadRequest)


DESCRIPTOR._options = None
_GETPAYLOADREQUEST.fields_by_name['secret_id']._options = None
_GETPAYLOADREQUEST.fields_by_name['version_id']._options = None

_PAYLOADSERVICE = _descriptor.ServiceDescriptor(
  name='PayloadService',
  full_name='yandex.cloud.lockbox.v1.PayloadService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=259,
  serialized_end=410,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.lockbox.v1.PayloadService.Get',
    index=0,
    containing_service=None,
    input_type=_GETPAYLOADREQUEST,
    output_type=yandex_dot_cloud_dot_lockbox_dot_v1_dot_payload__pb2._PAYLOAD,
    serialized_options=b'\202\323\344\223\002)\022\'/lockbox/v1/secrets/{secret_id}/payload',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PAYLOADSERVICE)

DESCRIPTOR.services_by_name['PayloadService'] = _PAYLOADSERVICE

# @@protoc_insertion_point(module_scope)