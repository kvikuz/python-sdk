# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/serverless/containers/v1/container.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/serverless/containers/v1/container.proto',
  package='yandex.cloud.serverless.containers.v1',
  syntax='proto3',
  serialized_options=b'\n)yandex.cloud.api.serverless.containers.v1ZTgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/containers/v1;containers',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n5yandex/cloud/serverless/containers/v1/container.proto\x12%yandex.cloud.serverless.containers.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xa5\x03\n\tContainer\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12L\n\x06labels\x18\x06 \x03(\x0b\x32<.yandex.cloud.serverless.containers.v1.Container.LabelsEntry\x12\x0b\n\x03url\x18\x08 \x01(\t\x12G\n\x06status\x18\t \x01(\x0e\x32\x37.yandex.cloud.serverless.containers.v1.Container.Status\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"S\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08\x44\x45LETING\x10\x03\x12\t\n\x05\x45RROR\x10\x04\"\xec\x03\n\x08Revision\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x63ontainer_id\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12;\n\x05image\x18\x05 \x01(\x0b\x32,.yandex.cloud.serverless.containers.v1.Image\x12\x43\n\tresources\x18\x06 \x01(\x0b\x32\x30.yandex.cloud.serverless.containers.v1.Resources\x12\x34\n\x11\x65xecution_timeout\x18\x07 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x13\n\x0b\x63oncurrency\x18\x08 \x01(\x03\x12\x1a\n\x12service_account_id\x18\t \x01(\t\x12\x46\n\x06status\x18\n \x01(\x0e\x32\x36.yandex.cloud.serverless.containers.v1.Revision.Status\"H\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08OBSOLETE\x10\x03\"\xf0\x02\n\x05Image\x12\x11\n\timage_url\x18\x01 \x01(\t\x12\x14\n\x0cimage_digest\x18\x02 \x01(\t\x12?\n\x07\x63ommand\x18\x03 \x01(\x0b\x32..yandex.cloud.serverless.containers.v1.Command\x12\x39\n\x04\x61rgs\x18\x04 \x01(\x0b\x32+.yandex.cloud.serverless.containers.v1.Args\x12y\n\x0b\x65nvironment\x18\x05 \x03(\x0b\x32=.yandex.cloud.serverless.containers.v1.Image.EnvironmentEntryB%\x8a\xc8\x31\x06<=4096\xb2\xc8\x31\x17\x12\x15[a-zA-Z][a-zA-Z0-9_]*\x12\x13\n\x0bworking_dir\x18\x06 \x01(\t\x1a\x32\n\x10\x45nvironmentEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1a\n\x07\x43ommand\x12\x0f\n\x07\x63ommand\x18\x01 \x03(\t\"\x14\n\x04\x41rgs\x12\x0c\n\x04\x61rgs\x18\x01 \x03(\t\"o\n\tResources\x12(\n\x06memory\x18\x01 \x01(\x03\x42\x18\xfa\xc7\x31\x14\x31\x33\x34\x32\x31\x37\x37\x32\x38-8589934592\x12\x16\n\x05\x63ores\x18\x02 \x01(\x03\x42\x07\xfa\xc7\x31\x03\x30-1\x12 \n\rcore_fraction\x18\x03 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100B\x81\x01\n)yandex.cloud.api.serverless.containers.v1ZTgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/containers/v1;containersb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])



_CONTAINER_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.serverless.containers.v1.Container.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETING', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=531,
  serialized_end=614,
)
_sym_db.RegisterEnumDescriptor(_CONTAINER_STATUS)

_REVISION_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.serverless.containers.v1.Revision.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OBSOLETE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1037,
  serialized_end=1109,
)
_sym_db.RegisterEnumDescriptor(_REVISION_STATUS)


_CONTAINER_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.serverless.containers.v1.Container.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.serverless.containers.v1.Container.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.serverless.containers.v1.Container.LabelsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=484,
  serialized_end=529,
)

_CONTAINER = _descriptor.Descriptor(
  name='Container',
  full_name='yandex.cloud.serverless.containers.v1.Container',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.serverless.containers.v1.Container.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.serverless.containers.v1.Container.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.serverless.containers.v1.Container.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.serverless.containers.v1.Container.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.serverless.containers.v1.Container.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.serverless.containers.v1.Container.labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='yandex.cloud.serverless.containers.v1.Container.url', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.serverless.containers.v1.Container.status', index=7,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CONTAINER_LABELSENTRY, ],
  enum_types=[
    _CONTAINER_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=614,
)


_REVISION = _descriptor.Descriptor(
  name='Revision',
  full_name='yandex.cloud.serverless.containers.v1.Revision',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.serverless.containers.v1.Revision.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='container_id', full_name='yandex.cloud.serverless.containers.v1.Revision.container_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.serverless.containers.v1.Revision.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.serverless.containers.v1.Revision.created_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='yandex.cloud.serverless.containers.v1.Revision.image', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resources', full_name='yandex.cloud.serverless.containers.v1.Revision.resources', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='execution_timeout', full_name='yandex.cloud.serverless.containers.v1.Revision.execution_timeout', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='concurrency', full_name='yandex.cloud.serverless.containers.v1.Revision.concurrency', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.serverless.containers.v1.Revision.service_account_id', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.serverless.containers.v1.Revision.status', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REVISION_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=617,
  serialized_end=1109,
)


_IMAGE_ENVIRONMENTENTRY = _descriptor.Descriptor(
  name='EnvironmentEntry',
  full_name='yandex.cloud.serverless.containers.v1.Image.EnvironmentEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.serverless.containers.v1.Image.EnvironmentEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.serverless.containers.v1.Image.EnvironmentEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1430,
  serialized_end=1480,
)

_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='yandex.cloud.serverless.containers.v1.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image_url', full_name='yandex.cloud.serverless.containers.v1.Image.image_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image_digest', full_name='yandex.cloud.serverless.containers.v1.Image.image_digest', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='command', full_name='yandex.cloud.serverless.containers.v1.Image.command', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='args', full_name='yandex.cloud.serverless.containers.v1.Image.args', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='environment', full_name='yandex.cloud.serverless.containers.v1.Image.environment', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\006<=4096\262\3101\027\022\025[a-zA-Z][a-zA-Z0-9_]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='working_dir', full_name='yandex.cloud.serverless.containers.v1.Image.working_dir', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_IMAGE_ENVIRONMENTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1112,
  serialized_end=1480,
)


_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='yandex.cloud.serverless.containers.v1.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='yandex.cloud.serverless.containers.v1.Command.command', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1482,
  serialized_end=1508,
)


_ARGS = _descriptor.Descriptor(
  name='Args',
  full_name='yandex.cloud.serverless.containers.v1.Args',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='args', full_name='yandex.cloud.serverless.containers.v1.Args.args', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1510,
  serialized_end=1530,
)


_RESOURCES = _descriptor.Descriptor(
  name='Resources',
  full_name='yandex.cloud.serverless.containers.v1.Resources',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='memory', full_name='yandex.cloud.serverless.containers.v1.Resources.memory', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\024134217728-8589934592', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cores', full_name='yandex.cloud.serverless.containers.v1.Resources.cores', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0030-1', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='core_fraction', full_name='yandex.cloud.serverless.containers.v1.Resources.core_fraction', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\0050-100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1532,
  serialized_end=1643,
)

_CONTAINER_LABELSENTRY.containing_type = _CONTAINER
_CONTAINER.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CONTAINER.fields_by_name['labels'].message_type = _CONTAINER_LABELSENTRY
_CONTAINER.fields_by_name['status'].enum_type = _CONTAINER_STATUS
_CONTAINER_STATUS.containing_type = _CONTAINER
_REVISION.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_REVISION.fields_by_name['image'].message_type = _IMAGE
_REVISION.fields_by_name['resources'].message_type = _RESOURCES
_REVISION.fields_by_name['execution_timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_REVISION.fields_by_name['status'].enum_type = _REVISION_STATUS
_REVISION_STATUS.containing_type = _REVISION
_IMAGE_ENVIRONMENTENTRY.containing_type = _IMAGE
_IMAGE.fields_by_name['command'].message_type = _COMMAND
_IMAGE.fields_by_name['args'].message_type = _ARGS
_IMAGE.fields_by_name['environment'].message_type = _IMAGE_ENVIRONMENTENTRY
DESCRIPTOR.message_types_by_name['Container'] = _CONTAINER
DESCRIPTOR.message_types_by_name['Revision'] = _REVISION
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['Args'] = _ARGS
DESCRIPTOR.message_types_by_name['Resources'] = _RESOURCES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Container = _reflection.GeneratedProtocolMessageType('Container', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONTAINER_LABELSENTRY,
    '__module__' : 'yandex.cloud.serverless.containers.v1.container_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.containers.v1.Container.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _CONTAINER,
  '__module__' : 'yandex.cloud.serverless.containers.v1.container_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.containers.v1.Container)
  })
_sym_db.RegisterMessage(Container)
_sym_db.RegisterMessage(Container.LabelsEntry)

Revision = _reflection.GeneratedProtocolMessageType('Revision', (_message.Message,), {
  'DESCRIPTOR' : _REVISION,
  '__module__' : 'yandex.cloud.serverless.containers.v1.container_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.containers.v1.Revision)
  })
_sym_db.RegisterMessage(Revision)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {

  'EnvironmentEntry' : _reflection.GeneratedProtocolMessageType('EnvironmentEntry', (_message.Message,), {
    'DESCRIPTOR' : _IMAGE_ENVIRONMENTENTRY,
    '__module__' : 'yandex.cloud.serverless.containers.v1.container_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.containers.v1.Image.EnvironmentEntry)
    })
  ,
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'yandex.cloud.serverless.containers.v1.container_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.containers.v1.Image)
  })
_sym_db.RegisterMessage(Image)
_sym_db.RegisterMessage(Image.EnvironmentEntry)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND,
  '__module__' : 'yandex.cloud.serverless.containers.v1.container_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.containers.v1.Command)
  })
_sym_db.RegisterMessage(Command)

Args = _reflection.GeneratedProtocolMessageType('Args', (_message.Message,), {
  'DESCRIPTOR' : _ARGS,
  '__module__' : 'yandex.cloud.serverless.containers.v1.container_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.containers.v1.Args)
  })
_sym_db.RegisterMessage(Args)

Resources = _reflection.GeneratedProtocolMessageType('Resources', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCES,
  '__module__' : 'yandex.cloud.serverless.containers.v1.container_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.containers.v1.Resources)
  })
_sym_db.RegisterMessage(Resources)


DESCRIPTOR._options = None
_CONTAINER_LABELSENTRY._options = None
_IMAGE_ENVIRONMENTENTRY._options = None
_IMAGE.fields_by_name['environment']._options = None
_RESOURCES.fields_by_name['memory']._options = None
_RESOURCES.fields_by_name['cores']._options = None
_RESOURCES.fields_by_name['core_fraction']._options = None
# @@protoc_insertion_point(module_scope)
