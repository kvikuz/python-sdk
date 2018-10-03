# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/resourcemanager/v1/cloud_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.resourcemanager.v1 import cloud_pb2 as yandex_dot_cloud_dot_resourcemanager_dot_v1_dot_cloud__pb2
from yandex.api import operation_pb2 as yandex_dot_api_dot_operation__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/resourcemanager/v1/cloud_service.proto',
  package='yandex.cloud.resourcemanager.v1',
  syntax='proto3',
  serialized_pb=_b('\n3yandex/cloud/resourcemanager/v1/cloud_service.proto\x12\x1fyandex.cloud.resourcemanager.v1\x1a\x1cgoogle/api/annotations.proto\x1a+yandex/cloud/resourcemanager/v1/cloud.proto\x1a\x1ayandex/api/operation.proto\x1a yandex/cloud/access/access.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"1\n\x0fGetCloudRequest\x12\x1e\n\x08\x63loud_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"m\n\x11ListCloudsRequest\x12\x1d\n\tpage_size\x18\x01 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"e\n\x12ListCloudsResponse\x12\x36\n\x06\x63louds\x18\x01 \x03(\x0b\x32&.yandex.cloud.resourcemanager.v1.Cloud\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"z\n\x1aListCloudOperationsRequest\x12\x1e\n\x08\x63loud_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"m\n\x1bListCloudOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xa6\t\n\x0c\x43loudService\x12\x8f\x01\n\x03Get\x12\x30.yandex.cloud.resourcemanager.v1.GetCloudRequest\x1a&.yandex.cloud.resourcemanager.v1.Cloud\".\x82\xd3\xe4\x93\x02(\x12&/resource-manager/v1/clouds/{cloud_id}\x12\x94\x01\n\x04List\x12\x32.yandex.cloud.resourcemanager.v1.ListCloudsRequest\x1a\x33.yandex.cloud.resourcemanager.v1.ListCloudsResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/resource-manager/v1/clouds\x12\xc6\x01\n\x0eListOperations\x12;.yandex.cloud.resourcemanager.v1.ListCloudOperationsRequest\x1a<.yandex.cloud.resourcemanager.v1.ListCloudOperationsResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/resource-manager/v1/clouds/{cloud_id}/operations\x12\xbb\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"D\x82\xd3\xe4\x93\x02>\x12</resource-manager/v1/clouds/{resource_id}:listAccessBindings\x12\xeb\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x83\x01\x82\xd3\xe4\x93\x02@\";/resource-manager/v1/clouds/{resource_id}:setAccessBindings:\x01*\xb2\xd2*9\n access.SetAccessBindingsMetadata\x12\x15google.protobuf.Empty\x12\xf7\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x89\x01\x82\xd3\xe4\x93\x02\x43\">/resource-manager/v1/clouds/{resource_id}:updateAccessBindings:\x01*\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.EmptyBUZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/resourcemanager/v1;resourcemanagerb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_resourcemanager_dot_v1_dot_cloud__pb2.DESCRIPTOR,yandex_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_access_dot_access__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_GETCLOUDREQUEST = _descriptor.Descriptor(
  name='GetCloudRequest',
  full_name='yandex.cloud.resourcemanager.v1.GetCloudRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cloud_id', full_name='yandex.cloud.resourcemanager.v1.GetCloudRequest.cloud_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001\212\3101\004<=50')), file=DESCRIPTOR),
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
  serialized_start=296,
  serialized_end=345,
)


_LISTCLOUDSREQUEST = _descriptor.Descriptor(
  name='ListCloudsRequest',
  full_name='yandex.cloud.resourcemanager.v1.ListCloudsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.resourcemanager.v1.ListCloudsRequest.page_size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\372\3071\006<=1000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.resourcemanager.v1.ListCloudsRequest.page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3101\005<=100')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='yandex.cloud.resourcemanager.v1.ListCloudsRequest.filter', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3101\006<=1000')), file=DESCRIPTOR),
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
  serialized_start=347,
  serialized_end=456,
)


_LISTCLOUDSRESPONSE = _descriptor.Descriptor(
  name='ListCloudsResponse',
  full_name='yandex.cloud.resourcemanager.v1.ListCloudsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clouds', full_name='yandex.cloud.resourcemanager.v1.ListCloudsResponse.clouds', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.resourcemanager.v1.ListCloudsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=458,
  serialized_end=559,
)


_LISTCLOUDOPERATIONSREQUEST = _descriptor.Descriptor(
  name='ListCloudOperationsRequest',
  full_name='yandex.cloud.resourcemanager.v1.ListCloudOperationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cloud_id', full_name='yandex.cloud.resourcemanager.v1.ListCloudOperationsRequest.cloud_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001\212\3101\004<=50')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.resourcemanager.v1.ListCloudOperationsRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\372\3071\006<=1000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.resourcemanager.v1.ListCloudOperationsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3101\005<=100')), file=DESCRIPTOR),
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
  serialized_start=561,
  serialized_end=683,
)


_LISTCLOUDOPERATIONSRESPONSE = _descriptor.Descriptor(
  name='ListCloudOperationsResponse',
  full_name='yandex.cloud.resourcemanager.v1.ListCloudOperationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operations', full_name='yandex.cloud.resourcemanager.v1.ListCloudOperationsResponse.operations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.resourcemanager.v1.ListCloudOperationsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=685,
  serialized_end=794,
)

_LISTCLOUDSRESPONSE.fields_by_name['clouds'].message_type = yandex_dot_cloud_dot_resourcemanager_dot_v1_dot_cloud__pb2._CLOUD
_LISTCLOUDOPERATIONSRESPONSE.fields_by_name['operations'].message_type = yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION
DESCRIPTOR.message_types_by_name['GetCloudRequest'] = _GETCLOUDREQUEST
DESCRIPTOR.message_types_by_name['ListCloudsRequest'] = _LISTCLOUDSREQUEST
DESCRIPTOR.message_types_by_name['ListCloudsResponse'] = _LISTCLOUDSRESPONSE
DESCRIPTOR.message_types_by_name['ListCloudOperationsRequest'] = _LISTCLOUDOPERATIONSREQUEST
DESCRIPTOR.message_types_by_name['ListCloudOperationsResponse'] = _LISTCLOUDOPERATIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCloudRequest = _reflection.GeneratedProtocolMessageType('GetCloudRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCLOUDREQUEST,
  __module__ = 'yandex.cloud.resourcemanager.v1.cloud_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.resourcemanager.v1.GetCloudRequest)
  ))
_sym_db.RegisterMessage(GetCloudRequest)

ListCloudsRequest = _reflection.GeneratedProtocolMessageType('ListCloudsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTCLOUDSREQUEST,
  __module__ = 'yandex.cloud.resourcemanager.v1.cloud_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.resourcemanager.v1.ListCloudsRequest)
  ))
_sym_db.RegisterMessage(ListCloudsRequest)

ListCloudsResponse = _reflection.GeneratedProtocolMessageType('ListCloudsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTCLOUDSRESPONSE,
  __module__ = 'yandex.cloud.resourcemanager.v1.cloud_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.resourcemanager.v1.ListCloudsResponse)
  ))
_sym_db.RegisterMessage(ListCloudsResponse)

ListCloudOperationsRequest = _reflection.GeneratedProtocolMessageType('ListCloudOperationsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTCLOUDOPERATIONSREQUEST,
  __module__ = 'yandex.cloud.resourcemanager.v1.cloud_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.resourcemanager.v1.ListCloudOperationsRequest)
  ))
_sym_db.RegisterMessage(ListCloudOperationsRequest)

ListCloudOperationsResponse = _reflection.GeneratedProtocolMessageType('ListCloudOperationsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTCLOUDOPERATIONSRESPONSE,
  __module__ = 'yandex.cloud.resourcemanager.v1.cloud_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.resourcemanager.v1.ListCloudOperationsResponse)
  ))
_sym_db.RegisterMessage(ListCloudOperationsResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/resourcemanager/v1;resourcemanager'))
_GETCLOUDREQUEST.fields_by_name['cloud_id'].has_options = True
_GETCLOUDREQUEST.fields_by_name['cloud_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001\212\3101\004<=50'))
_LISTCLOUDSREQUEST.fields_by_name['page_size'].has_options = True
_LISTCLOUDSREQUEST.fields_by_name['page_size']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\372\3071\006<=1000'))
_LISTCLOUDSREQUEST.fields_by_name['page_token'].has_options = True
_LISTCLOUDSREQUEST.fields_by_name['page_token']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3101\005<=100'))
_LISTCLOUDSREQUEST.fields_by_name['filter'].has_options = True
_LISTCLOUDSREQUEST.fields_by_name['filter']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3101\006<=1000'))
_LISTCLOUDOPERATIONSREQUEST.fields_by_name['cloud_id'].has_options = True
_LISTCLOUDOPERATIONSREQUEST.fields_by_name['cloud_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\350\3071\001\212\3101\004<=50'))
_LISTCLOUDOPERATIONSREQUEST.fields_by_name['page_size'].has_options = True
_LISTCLOUDOPERATIONSREQUEST.fields_by_name['page_size']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\372\3071\006<=1000'))
_LISTCLOUDOPERATIONSREQUEST.fields_by_name['page_token'].has_options = True
_LISTCLOUDOPERATIONSREQUEST.fields_by_name['page_token']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212\3101\005<=100'))

_CLOUDSERVICE = _descriptor.ServiceDescriptor(
  name='CloudService',
  full_name='yandex.cloud.resourcemanager.v1.CloudService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=797,
  serialized_end=1987,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.resourcemanager.v1.CloudService.Get',
    index=0,
    containing_service=None,
    input_type=_GETCLOUDREQUEST,
    output_type=yandex_dot_cloud_dot_resourcemanager_dot_v1_dot_cloud__pb2._CLOUD,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002(\022&/resource-manager/v1/clouds/{cloud_id}')),
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.resourcemanager.v1.CloudService.List',
    index=1,
    containing_service=None,
    input_type=_LISTCLOUDSREQUEST,
    output_type=_LISTCLOUDSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\035\022\033/resource-manager/v1/clouds')),
  ),
  _descriptor.MethodDescriptor(
    name='ListOperations',
    full_name='yandex.cloud.resourcemanager.v1.CloudService.ListOperations',
    index=2,
    containing_service=None,
    input_type=_LISTCLOUDOPERATIONSREQUEST,
    output_type=_LISTCLOUDOPERATIONSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0023\0221/resource-manager/v1/clouds/{cloud_id}/operations')),
  ),
  _descriptor.MethodDescriptor(
    name='ListAccessBindings',
    full_name='yandex.cloud.resourcemanager.v1.CloudService.ListAccessBindings',
    index=3,
    containing_service=None,
    input_type=yandex_dot_cloud_dot_access_dot_access__pb2._LISTACCESSBINDINGSREQUEST,
    output_type=yandex_dot_cloud_dot_access_dot_access__pb2._LISTACCESSBINDINGSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002>\022</resource-manager/v1/clouds/{resource_id}:listAccessBindings')),
  ),
  _descriptor.MethodDescriptor(
    name='SetAccessBindings',
    full_name='yandex.cloud.resourcemanager.v1.CloudService.SetAccessBindings',
    index=4,
    containing_service=None,
    input_type=yandex_dot_cloud_dot_access_dot_access__pb2._SETACCESSBINDINGSREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002@\";/resource-manager/v1/clouds/{resource_id}:setAccessBindings:\001*\262\322*9\n access.SetAccessBindingsMetadata\022\025google.protobuf.Empty')),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateAccessBindings',
    full_name='yandex.cloud.resourcemanager.v1.CloudService.UpdateAccessBindings',
    index=5,
    containing_service=None,
    input_type=yandex_dot_cloud_dot_access_dot_access__pb2._UPDATEACCESSBINDINGSREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002C\">/resource-manager/v1/clouds/{resource_id}:updateAccessBindings:\001*\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty')),
  ),
])
_sym_db.RegisterServiceDescriptor(_CLOUDSERVICE)

DESCRIPTOR.services_by_name['CloudService'] = _CLOUDSERVICE

# @@protoc_insertion_point(module_scope)
