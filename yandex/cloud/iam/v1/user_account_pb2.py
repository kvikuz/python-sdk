# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iam/v1/user_account.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/iam/v1/user_account.proto',
  package='yandex.cloud.iam.v1',
  syntax='proto3',
  serialized_options=_b('\n\027yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iam'),
  serialized_pb=_b('\n&yandex/cloud/iam/v1/user_account.proto\x12\x13yandex.cloud.iam.v1\x1a\x1dyandex/cloud/validation.proto\"\xca\x01\n\x0bUserAccount\x12\n\n\x02id\x18\x01 \x01(\t\x12V\n\x1cyandex_passport_user_account\x18\x02 \x01(\x0b\x32..yandex.cloud.iam.v1.YandexPassportUserAccountH\x00\x12\x41\n\x11saml_user_account\x18\x03 \x01(\x0b\x32$.yandex.cloud.iam.v1.SamlUserAccountH\x00\x42\x14\n\x0cuser_account\x12\x04\xc0\xc1\x31\x01\"A\n\x19YandexPassportUserAccount\x12\r\n\x05login\x18\x01 \x01(\t\x12\x15\n\rdefault_email\x18\x02 \x01(\t\"V\n\x0fSamlUserAccount\x12#\n\rfederation_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1e\n\x07name_id\x18\x02 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05\x31-256BV\n\x17yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iamb\x06proto3')
  ,
  dependencies=[yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_USERACCOUNT = _descriptor.Descriptor(
  name='UserAccount',
  full_name='yandex.cloud.iam.v1.UserAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.iam.v1.UserAccount.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yandex_passport_user_account', full_name='yandex.cloud.iam.v1.UserAccount.yandex_passport_user_account', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='saml_user_account', full_name='yandex.cloud.iam.v1.UserAccount.saml_user_account', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
      name='user_account', full_name='yandex.cloud.iam.v1.UserAccount.user_account',
      index=0, containing_type=None, fields=[], serialized_options=_b('\300\3011\001')),
  ],
  serialized_start=95,
  serialized_end=297,
)


_YANDEXPASSPORTUSERACCOUNT = _descriptor.Descriptor(
  name='YandexPassportUserAccount',
  full_name='yandex.cloud.iam.v1.YandexPassportUserAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='login', full_name='yandex.cloud.iam.v1.YandexPassportUserAccount.login', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_email', full_name='yandex.cloud.iam.v1.YandexPassportUserAccount.default_email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  ],
  serialized_start=299,
  serialized_end=364,
)


_SAMLUSERACCOUNT = _descriptor.Descriptor(
  name='SamlUserAccount',
  full_name='yandex.cloud.iam.v1.SamlUserAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='federation_id', full_name='yandex.cloud.iam.v1.SamlUserAccount.federation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name_id', full_name='yandex.cloud.iam.v1.SamlUserAccount.name_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001\212\3101\0051-256'), file=DESCRIPTOR),
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
  serialized_start=366,
  serialized_end=452,
)

_USERACCOUNT.fields_by_name['yandex_passport_user_account'].message_type = _YANDEXPASSPORTUSERACCOUNT
_USERACCOUNT.fields_by_name['saml_user_account'].message_type = _SAMLUSERACCOUNT
_USERACCOUNT.oneofs_by_name['user_account'].fields.append(
  _USERACCOUNT.fields_by_name['yandex_passport_user_account'])
_USERACCOUNT.fields_by_name['yandex_passport_user_account'].containing_oneof = _USERACCOUNT.oneofs_by_name['user_account']
_USERACCOUNT.oneofs_by_name['user_account'].fields.append(
  _USERACCOUNT.fields_by_name['saml_user_account'])
_USERACCOUNT.fields_by_name['saml_user_account'].containing_oneof = _USERACCOUNT.oneofs_by_name['user_account']
DESCRIPTOR.message_types_by_name['UserAccount'] = _USERACCOUNT
DESCRIPTOR.message_types_by_name['YandexPassportUserAccount'] = _YANDEXPASSPORTUSERACCOUNT
DESCRIPTOR.message_types_by_name['SamlUserAccount'] = _SAMLUSERACCOUNT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserAccount = _reflection.GeneratedProtocolMessageType('UserAccount', (_message.Message,), {
  'DESCRIPTOR' : _USERACCOUNT,
  '__module__' : 'yandex.cloud.iam.v1.user_account_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.UserAccount)
  })
_sym_db.RegisterMessage(UserAccount)

YandexPassportUserAccount = _reflection.GeneratedProtocolMessageType('YandexPassportUserAccount', (_message.Message,), {
  'DESCRIPTOR' : _YANDEXPASSPORTUSERACCOUNT,
  '__module__' : 'yandex.cloud.iam.v1.user_account_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.YandexPassportUserAccount)
  })
_sym_db.RegisterMessage(YandexPassportUserAccount)

SamlUserAccount = _reflection.GeneratedProtocolMessageType('SamlUserAccount', (_message.Message,), {
  'DESCRIPTOR' : _SAMLUSERACCOUNT,
  '__module__' : 'yandex.cloud.iam.v1.user_account_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.SamlUserAccount)
  })
_sym_db.RegisterMessage(SamlUserAccount)


DESCRIPTOR._options = None
_USERACCOUNT.oneofs_by_name['user_account']._options = None
_SAMLUSERACCOUNT.fields_by_name['federation_id']._options = None
_SAMLUSERACCOUNT.fields_by_name['name_id']._options = None
# @@protoc_insertion_point(module_scope)
