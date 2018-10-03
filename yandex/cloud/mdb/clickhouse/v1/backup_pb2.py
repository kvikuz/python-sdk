# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/clickhouse/v1/backup.proto

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
  name='yandex/cloud/mdb/clickhouse/v1/backup.proto',
  package='yandex.cloud.mdb.clickhouse.v1',
  syntax='proto3',
  serialized_pb=_b('\n+yandex/cloud/mdb/clickhouse/v1/backup.proto\x12\x1eyandex.cloud.mdb.clickhouse.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa2\x01\n\x06\x42\x61\x63kup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x19\n\x11source_cluster_id\x18\x04 \x01(\t\x12.\n\nstarted_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampBOZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_BACKUP = _descriptor.Descriptor(
  name='Backup',
  full_name='yandex.cloud.mdb.clickhouse.v1.Backup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.mdb.clickhouse.v1.Backup.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.mdb.clickhouse.v1.Backup.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.mdb.clickhouse.v1.Backup.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_cluster_id', full_name='yandex.cloud.mdb.clickhouse.v1.Backup.source_cluster_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='started_at', full_name='yandex.cloud.mdb.clickhouse.v1.Backup.started_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_end=275,
)

_BACKUP.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BACKUP.fields_by_name['started_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Backup'] = _BACKUP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Backup = _reflection.GeneratedProtocolMessageType('Backup', (_message.Message,), dict(
  DESCRIPTOR = _BACKUP,
  __module__ = 'yandex.cloud.mdb.clickhouse.v1.backup_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.Backup)
  ))
_sym_db.RegisterMessage(Backup)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouse'))
# @@protoc_insertion_point(module_scope)
