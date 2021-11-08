# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datatransfer/v1/endpoint/postgres.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.datatransfer.v1.endpoint import common_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/datatransfer/v1/endpoint/postgres.proto',
  package='yandex.cloud.datatransfer.v1.endpoint',
  syntax='proto3',
  serialized_options=b'\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n4yandex/cloud/datatransfer/v1/endpoint/postgres.proto\x12%yandex.cloud.datatransfer.v1.endpoint\x1a\x32yandex/cloud/datatransfer/v1/endpoint/common.proto\"\x81\n\n\x1ePostgresObjectTransferSettings\x12L\n\x08sequence\x18\x01 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12U\n\x11sequence_owned_by\x18\x02 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12I\n\x05table\x18\x03 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12O\n\x0bprimary_key\x18\x04 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12Q\n\rfk_constraint\x18\x05 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12R\n\x0e\x64\x65\x66\x61ult_values\x18\x06 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12N\n\nconstraint\x18\x07 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12I\n\x05index\x18\x08 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12H\n\x04view\x18\t \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12L\n\x08\x66unction\x18\n \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12K\n\x07trigger\x18\x0b \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12H\n\x04type\x18\x0c \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12H\n\x04rule\x18\r \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12M\n\tcollation\x18\x0e \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12J\n\x06policy\x18\x0f \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12H\n\x04\x63\x61st\x18\x10 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\"\x85\x01\n\x11OnPremisePostgres\x12\r\n\x05hosts\x18\x05 \x03(\t\x12\x0c\n\x04port\x18\x02 \x01(\x03\x12@\n\x08tls_mode\x18\x06 \x01(\x0b\x32..yandex.cloud.datatransfer.v1.endpoint.TLSMode\x12\x11\n\tsubnet_id\x18\x04 \x01(\t\"\x8c\x01\n\x12PostgresConnection\x12\x18\n\x0emdb_cluster_id\x18\x01 \x01(\tH\x00\x12N\n\non_premise\x18\x02 \x01(\x0b\x32\x38.yandex.cloud.datatransfer.v1.endpoint.OnPremisePostgresH\x00\x42\x0c\n\nconnection\"\x8e\x03\n\x0ePostgresSource\x12M\n\nconnection\x18\x01 \x01(\x0b\x32\x39.yandex.cloud.datatransfer.v1.endpoint.PostgresConnection\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\x12?\n\x08password\x18\x04 \x01(\x0b\x32-.yandex.cloud.datatransfer.v1.endpoint.Secret\x12\x16\n\x0einclude_tables\x18\x05 \x03(\t\x12\x16\n\x0e\x65xclude_tables\x18\x06 \x03(\t\x12\x1b\n\x13slot_byte_lag_limit\x18\x08 \x01(\x03\x12\x16\n\x0eservice_schema\x18\t \x01(\t\x12g\n\x18object_transfer_settings\x18\r \x01(\x0b\x32\x45.yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings\"\xc0\x01\n\x0ePostgresTarget\x12M\n\nconnection\x18\x01 \x01(\x0b\x32\x39.yandex.cloud.datatransfer.v1.endpoint.PostgresConnection\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\x12?\n\x08password\x18\x04 \x01(\x0b\x32-.yandex.cloud.datatransfer.v1.endpoint.SecretB\x7f\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpointb\x06proto3'
  ,
  dependencies=[yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2.DESCRIPTOR,])




_POSTGRESOBJECTTRANSFERSETTINGS = _descriptor.Descriptor(
  name='PostgresObjectTransferSettings',
  full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings.sequence', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_owned_by', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings.sequence_owned_by', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='table', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings.table', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='primary_key', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings.primary_key', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fk_constraint', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings.fk_constraint', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_values', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings.default_values', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='constraint', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings.constraint', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings.index', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='view', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings.view', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='function', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings.function', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trigger', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings.trigger', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings.type', index=11,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rule', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings.rule', index=12,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='collation', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings.collation', index=13,
      number=14, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='policy', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings.policy', index=14,
      number=15, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cast', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings.cast', index=15,
      number=16, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=148,
  serialized_end=1429,
)


_ONPREMISEPOSTGRES = _descriptor.Descriptor(
  name='OnPremisePostgres',
  full_name='yandex.cloud.datatransfer.v1.endpoint.OnPremisePostgres',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hosts', full_name='yandex.cloud.datatransfer.v1.endpoint.OnPremisePostgres.hosts', index=0,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='yandex.cloud.datatransfer.v1.endpoint.OnPremisePostgres.port', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tls_mode', full_name='yandex.cloud.datatransfer.v1.endpoint.OnPremisePostgres.tls_mode', index=2,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subnet_id', full_name='yandex.cloud.datatransfer.v1.endpoint.OnPremisePostgres.subnet_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=1432,
  serialized_end=1565,
)


_POSTGRESCONNECTION = _descriptor.Descriptor(
  name='PostgresConnection',
  full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresConnection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mdb_cluster_id', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresConnection.mdb_cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='on_premise', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresConnection.on_premise', index=1,
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
      name='connection', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresConnection.connection',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1568,
  serialized_end=1708,
)


_POSTGRESSOURCE = _descriptor.Descriptor(
  name='PostgresSource',
  full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresSource.connection', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='database', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresSource.database', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresSource.user', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresSource.password', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='include_tables', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresSource.include_tables', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exclude_tables', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresSource.exclude_tables', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='slot_byte_lag_limit', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresSource.slot_byte_lag_limit', index=6,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_schema', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresSource.service_schema', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='object_transfer_settings', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresSource.object_transfer_settings', index=8,
      number=13, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=1711,
  serialized_end=2109,
)


_POSTGRESTARGET = _descriptor.Descriptor(
  name='PostgresTarget',
  full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresTarget.connection', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='database', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresTarget.database', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresTarget.user', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='yandex.cloud.datatransfer.v1.endpoint.PostgresTarget.password', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=2112,
  serialized_end=2304,
)

_POSTGRESOBJECTTRANSFERSETTINGS.fields_by_name['sequence'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._OBJECTTRANSFERSTAGE
_POSTGRESOBJECTTRANSFERSETTINGS.fields_by_name['sequence_owned_by'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._OBJECTTRANSFERSTAGE
_POSTGRESOBJECTTRANSFERSETTINGS.fields_by_name['table'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._OBJECTTRANSFERSTAGE
_POSTGRESOBJECTTRANSFERSETTINGS.fields_by_name['primary_key'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._OBJECTTRANSFERSTAGE
_POSTGRESOBJECTTRANSFERSETTINGS.fields_by_name['fk_constraint'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._OBJECTTRANSFERSTAGE
_POSTGRESOBJECTTRANSFERSETTINGS.fields_by_name['default_values'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._OBJECTTRANSFERSTAGE
_POSTGRESOBJECTTRANSFERSETTINGS.fields_by_name['constraint'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._OBJECTTRANSFERSTAGE
_POSTGRESOBJECTTRANSFERSETTINGS.fields_by_name['index'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._OBJECTTRANSFERSTAGE
_POSTGRESOBJECTTRANSFERSETTINGS.fields_by_name['view'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._OBJECTTRANSFERSTAGE
_POSTGRESOBJECTTRANSFERSETTINGS.fields_by_name['function'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._OBJECTTRANSFERSTAGE
_POSTGRESOBJECTTRANSFERSETTINGS.fields_by_name['trigger'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._OBJECTTRANSFERSTAGE
_POSTGRESOBJECTTRANSFERSETTINGS.fields_by_name['type'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._OBJECTTRANSFERSTAGE
_POSTGRESOBJECTTRANSFERSETTINGS.fields_by_name['rule'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._OBJECTTRANSFERSTAGE
_POSTGRESOBJECTTRANSFERSETTINGS.fields_by_name['collation'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._OBJECTTRANSFERSTAGE
_POSTGRESOBJECTTRANSFERSETTINGS.fields_by_name['policy'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._OBJECTTRANSFERSTAGE
_POSTGRESOBJECTTRANSFERSETTINGS.fields_by_name['cast'].enum_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._OBJECTTRANSFERSTAGE
_ONPREMISEPOSTGRES.fields_by_name['tls_mode'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._TLSMODE
_POSTGRESCONNECTION.fields_by_name['on_premise'].message_type = _ONPREMISEPOSTGRES
_POSTGRESCONNECTION.oneofs_by_name['connection'].fields.append(
  _POSTGRESCONNECTION.fields_by_name['mdb_cluster_id'])
_POSTGRESCONNECTION.fields_by_name['mdb_cluster_id'].containing_oneof = _POSTGRESCONNECTION.oneofs_by_name['connection']
_POSTGRESCONNECTION.oneofs_by_name['connection'].fields.append(
  _POSTGRESCONNECTION.fields_by_name['on_premise'])
_POSTGRESCONNECTION.fields_by_name['on_premise'].containing_oneof = _POSTGRESCONNECTION.oneofs_by_name['connection']
_POSTGRESSOURCE.fields_by_name['connection'].message_type = _POSTGRESCONNECTION
_POSTGRESSOURCE.fields_by_name['password'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._SECRET
_POSTGRESSOURCE.fields_by_name['object_transfer_settings'].message_type = _POSTGRESOBJECTTRANSFERSETTINGS
_POSTGRESTARGET.fields_by_name['connection'].message_type = _POSTGRESCONNECTION
_POSTGRESTARGET.fields_by_name['password'].message_type = yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2._SECRET
DESCRIPTOR.message_types_by_name['PostgresObjectTransferSettings'] = _POSTGRESOBJECTTRANSFERSETTINGS
DESCRIPTOR.message_types_by_name['OnPremisePostgres'] = _ONPREMISEPOSTGRES
DESCRIPTOR.message_types_by_name['PostgresConnection'] = _POSTGRESCONNECTION
DESCRIPTOR.message_types_by_name['PostgresSource'] = _POSTGRESSOURCE
DESCRIPTOR.message_types_by_name['PostgresTarget'] = _POSTGRESTARGET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PostgresObjectTransferSettings = _reflection.GeneratedProtocolMessageType('PostgresObjectTransferSettings', (_message.Message,), {
  'DESCRIPTOR' : _POSTGRESOBJECTTRANSFERSETTINGS,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.postgres_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings)
  })
_sym_db.RegisterMessage(PostgresObjectTransferSettings)

OnPremisePostgres = _reflection.GeneratedProtocolMessageType('OnPremisePostgres', (_message.Message,), {
  'DESCRIPTOR' : _ONPREMISEPOSTGRES,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.postgres_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.OnPremisePostgres)
  })
_sym_db.RegisterMessage(OnPremisePostgres)

PostgresConnection = _reflection.GeneratedProtocolMessageType('PostgresConnection', (_message.Message,), {
  'DESCRIPTOR' : _POSTGRESCONNECTION,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.postgres_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.PostgresConnection)
  })
_sym_db.RegisterMessage(PostgresConnection)

PostgresSource = _reflection.GeneratedProtocolMessageType('PostgresSource', (_message.Message,), {
  'DESCRIPTOR' : _POSTGRESSOURCE,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.postgres_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.PostgresSource)
  })
_sym_db.RegisterMessage(PostgresSource)

PostgresTarget = _reflection.GeneratedProtocolMessageType('PostgresTarget', (_message.Message,), {
  'DESCRIPTOR' : _POSTGRESTARGET,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.postgres_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.PostgresTarget)
  })
_sym_db.RegisterMessage(PostgresTarget)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
