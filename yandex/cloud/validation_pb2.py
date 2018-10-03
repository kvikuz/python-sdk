# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/validation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/validation.proto',
  package='yandex.cloud',
  syntax='proto3',
  serialized_pb=_b('\n\x1dyandex/cloud/validation.proto\x12\x0cyandex.cloud\x1a google/protobuf/descriptor.proto\"<\n\nMapKeySpec\x12\r\n\x05value\x18\x01 \x01(\t\x12\x0f\n\x07pattern\x18\x02 \x01(\t\x12\x0e\n\x06length\x18\x03 \x01(\t:4\n\x0b\x65xactly_one\x12\x1d.google.protobuf.OneofOptions\x18\x98\x98\x06 \x01(\x08:1\n\x08required\x12\x1d.google.protobuf.FieldOptions\x18\xfd\x98\x06 \x01(\x08:0\n\x07pattern\x12\x1d.google.protobuf.FieldOptions\x18\xfe\x98\x06 \x01(\t:.\n\x05value\x12\x1d.google.protobuf.FieldOptions\x18\xff\x98\x06 \x01(\t:-\n\x04size\x12\x1d.google.protobuf.FieldOptions\x18\x80\x99\x06 \x01(\t:/\n\x06length\x12\x1d.google.protobuf.FieldOptions\x18\x81\x99\x06 \x01(\t:J\n\x07map_key\x12\x1d.google.protobuf.FieldOptions\x18\x86\x99\x06 \x01(\x0b\x32\x18.yandex.cloud.MapKeySpecBHZFgithub.com/yandex-cloud/go-genproto/yandex/cloud/validation;validationb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


EXACTLY_ONE_FIELD_NUMBER = 101400
exactly_one = _descriptor.FieldDescriptor(
  name='exactly_one', full_name='yandex.cloud.exactly_one', index=0,
  number=101400, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)
REQUIRED_FIELD_NUMBER = 101501
required = _descriptor.FieldDescriptor(
  name='required', full_name='yandex.cloud.required', index=1,
  number=101501, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)
PATTERN_FIELD_NUMBER = 101502
pattern = _descriptor.FieldDescriptor(
  name='pattern', full_name='yandex.cloud.pattern', index=2,
  number=101502, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)
VALUE_FIELD_NUMBER = 101503
value = _descriptor.FieldDescriptor(
  name='value', full_name='yandex.cloud.value', index=3,
  number=101503, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)
SIZE_FIELD_NUMBER = 101504
size = _descriptor.FieldDescriptor(
  name='size', full_name='yandex.cloud.size', index=4,
  number=101504, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)
LENGTH_FIELD_NUMBER = 101505
length = _descriptor.FieldDescriptor(
  name='length', full_name='yandex.cloud.length', index=5,
  number=101505, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)
MAP_KEY_FIELD_NUMBER = 101510
map_key = _descriptor.FieldDescriptor(
  name='map_key', full_name='yandex.cloud.map_key', index=6,
  number=101510, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)


_MAPKEYSPEC = _descriptor.Descriptor(
  name='MapKeySpec',
  full_name='yandex.cloud.MapKeySpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.MapKeySpec.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pattern', full_name='yandex.cloud.MapKeySpec.pattern', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='yandex.cloud.MapKeySpec.length', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=81,
  serialized_end=141,
)

DESCRIPTOR.message_types_by_name['MapKeySpec'] = _MAPKEYSPEC
DESCRIPTOR.extensions_by_name['exactly_one'] = exactly_one
DESCRIPTOR.extensions_by_name['required'] = required
DESCRIPTOR.extensions_by_name['pattern'] = pattern
DESCRIPTOR.extensions_by_name['value'] = value
DESCRIPTOR.extensions_by_name['size'] = size
DESCRIPTOR.extensions_by_name['length'] = length
DESCRIPTOR.extensions_by_name['map_key'] = map_key
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MapKeySpec = _reflection.GeneratedProtocolMessageType('MapKeySpec', (_message.Message,), dict(
  DESCRIPTOR = _MAPKEYSPEC,
  __module__ = 'yandex.cloud.validation_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.MapKeySpec)
  ))
_sym_db.RegisterMessage(MapKeySpec)

google_dot_protobuf_dot_descriptor__pb2.OneofOptions.RegisterExtension(exactly_one)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(required)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(pattern)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(value)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(size)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(length)
map_key.message_type = _MAPKEYSPEC
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(map_key)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('ZFgithub.com/yandex-cloud/go-genproto/yandex/cloud/validation;validation'))
# @@protoc_insertion_point(module_scope)
