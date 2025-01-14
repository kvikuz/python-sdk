# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/billing/v1/budget_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.billing.v1 import budget_pb2 as yandex_dot_cloud_dot_billing_dot_v1_dot_budget__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/billing/v1/budget_service.proto',
  package='yandex.cloud.billing.v1',
  syntax='proto3',
  serialized_options=b'\n\033yandex.cloud.api.billing.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/billing/v1;billing',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,yandex/cloud/billing/v1/budget_service.proto\x12\x17yandex.cloud.billing.v1\x1a\x1cgoogle/api/annotations.proto\x1a$yandex/cloud/billing/v1/budget.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\",\n\x10GetBudgetRequest\x12\x18\n\x02id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"|\n\x12ListBudgetsRequest\x12(\n\x12\x62illing_account_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"`\n\x13ListBudgetsResponse\x12\x30\n\x07\x62udgets\x18\x01 \x03(\x0b\x32\x1f.yandex.cloud.billing.v1.Budget\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xc3\x02\n\x13\x43reateBudgetRequest\x12(\n\x12\x62illing_account_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x12\n\x04name\x18\x02 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x43\n\x10\x63ost_budget_spec\x18\x03 \x01(\x0b\x32\'.yandex.cloud.billing.v1.CostBudgetSpecH\x00\x12I\n\x13\x65xpense_budget_spec\x18\x04 \x01(\x0b\x32*.yandex.cloud.billing.v1.ExpenseBudgetSpecH\x00\x12I\n\x13\x62\x61lance_budget_spec\x18\x05 \x01(\x0b\x32*.yandex.cloud.billing.v1.BalanceBudgetSpecH\x00\x42\x13\n\x0b\x62udget_spec\x12\x04\xc0\xc1\x31\x01\")\n\x14\x43reateBudgetMetadata\x12\x11\n\tbudget_id\x18\x01 \x01(\t2\xa2\x03\n\rBudgetService\x12s\n\x03Get\x12).yandex.cloud.billing.v1.GetBudgetRequest\x1a\x1f.yandex.cloud.billing.v1.Budget\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/billing/v1/budgets/{id}\x12~\n\x04List\x12+.yandex.cloud.billing.v1.ListBudgetsRequest\x1a,.yandex.cloud.billing.v1.ListBudgetsResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/billing/v1/budgets\x12\x9b\x01\n\x06\x43reate\x12,.yandex.cloud.billing.v1.CreateBudgetRequest\x1a!.yandex.cloud.operation.Operation\"@\x82\xd3\xe4\x93\x02\x18\"\x13/billing/v1/budgets:\x01*\xb2\xd2*\x1e\n\x14\x43reateBudgetMetadata\x12\x06\x42udgetBb\n\x1byandex.cloud.api.billing.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/billing/v1;billingb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_billing_dot_v1_dot_budget__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_GETBUDGETREQUEST = _descriptor.Descriptor(
  name='GetBudgetRequest',
  full_name='yandex.cloud.billing.v1.GetBudgetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.billing.v1.GetBudgetRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=246,
  serialized_end=290,
)


_LISTBUDGETSREQUEST = _descriptor.Descriptor(
  name='ListBudgetsRequest',
  full_name='yandex.cloud.billing.v1.ListBudgetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='billing_account_id', full_name='yandex.cloud.billing.v1.ListBudgetsRequest.billing_account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.billing.v1.ListBudgetsRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\006<=1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.billing.v1.ListBudgetsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=292,
  serialized_end=416,
)


_LISTBUDGETSRESPONSE = _descriptor.Descriptor(
  name='ListBudgetsResponse',
  full_name='yandex.cloud.billing.v1.ListBudgetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='budgets', full_name='yandex.cloud.billing.v1.ListBudgetsResponse.budgets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.billing.v1.ListBudgetsResponse.next_page_token', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=418,
  serialized_end=514,
)


_CREATEBUDGETREQUEST = _descriptor.Descriptor(
  name='CreateBudgetRequest',
  full_name='yandex.cloud.billing.v1.CreateBudgetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='billing_account_id', full_name='yandex.cloud.billing.v1.CreateBudgetRequest.billing_account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.billing.v1.CreateBudgetRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cost_budget_spec', full_name='yandex.cloud.billing.v1.CreateBudgetRequest.cost_budget_spec', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expense_budget_spec', full_name='yandex.cloud.billing.v1.CreateBudgetRequest.expense_budget_spec', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='balance_budget_spec', full_name='yandex.cloud.billing.v1.CreateBudgetRequest.balance_budget_spec', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
      name='budget_spec', full_name='yandex.cloud.billing.v1.CreateBudgetRequest.budget_spec',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\300\3011\001'),
  ],
  serialized_start=517,
  serialized_end=840,
)


_CREATEBUDGETMETADATA = _descriptor.Descriptor(
  name='CreateBudgetMetadata',
  full_name='yandex.cloud.billing.v1.CreateBudgetMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='budget_id', full_name='yandex.cloud.billing.v1.CreateBudgetMetadata.budget_id', index=0,
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
  serialized_start=842,
  serialized_end=883,
)

_LISTBUDGETSRESPONSE.fields_by_name['budgets'].message_type = yandex_dot_cloud_dot_billing_dot_v1_dot_budget__pb2._BUDGET
_CREATEBUDGETREQUEST.fields_by_name['cost_budget_spec'].message_type = yandex_dot_cloud_dot_billing_dot_v1_dot_budget__pb2._COSTBUDGETSPEC
_CREATEBUDGETREQUEST.fields_by_name['expense_budget_spec'].message_type = yandex_dot_cloud_dot_billing_dot_v1_dot_budget__pb2._EXPENSEBUDGETSPEC
_CREATEBUDGETREQUEST.fields_by_name['balance_budget_spec'].message_type = yandex_dot_cloud_dot_billing_dot_v1_dot_budget__pb2._BALANCEBUDGETSPEC
_CREATEBUDGETREQUEST.oneofs_by_name['budget_spec'].fields.append(
  _CREATEBUDGETREQUEST.fields_by_name['cost_budget_spec'])
_CREATEBUDGETREQUEST.fields_by_name['cost_budget_spec'].containing_oneof = _CREATEBUDGETREQUEST.oneofs_by_name['budget_spec']
_CREATEBUDGETREQUEST.oneofs_by_name['budget_spec'].fields.append(
  _CREATEBUDGETREQUEST.fields_by_name['expense_budget_spec'])
_CREATEBUDGETREQUEST.fields_by_name['expense_budget_spec'].containing_oneof = _CREATEBUDGETREQUEST.oneofs_by_name['budget_spec']
_CREATEBUDGETREQUEST.oneofs_by_name['budget_spec'].fields.append(
  _CREATEBUDGETREQUEST.fields_by_name['balance_budget_spec'])
_CREATEBUDGETREQUEST.fields_by_name['balance_budget_spec'].containing_oneof = _CREATEBUDGETREQUEST.oneofs_by_name['budget_spec']
DESCRIPTOR.message_types_by_name['GetBudgetRequest'] = _GETBUDGETREQUEST
DESCRIPTOR.message_types_by_name['ListBudgetsRequest'] = _LISTBUDGETSREQUEST
DESCRIPTOR.message_types_by_name['ListBudgetsResponse'] = _LISTBUDGETSRESPONSE
DESCRIPTOR.message_types_by_name['CreateBudgetRequest'] = _CREATEBUDGETREQUEST
DESCRIPTOR.message_types_by_name['CreateBudgetMetadata'] = _CREATEBUDGETMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetBudgetRequest = _reflection.GeneratedProtocolMessageType('GetBudgetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBUDGETREQUEST,
  '__module__' : 'yandex.cloud.billing.v1.budget_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.GetBudgetRequest)
  })
_sym_db.RegisterMessage(GetBudgetRequest)

ListBudgetsRequest = _reflection.GeneratedProtocolMessageType('ListBudgetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTBUDGETSREQUEST,
  '__module__' : 'yandex.cloud.billing.v1.budget_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.ListBudgetsRequest)
  })
_sym_db.RegisterMessage(ListBudgetsRequest)

ListBudgetsResponse = _reflection.GeneratedProtocolMessageType('ListBudgetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTBUDGETSRESPONSE,
  '__module__' : 'yandex.cloud.billing.v1.budget_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.ListBudgetsResponse)
  })
_sym_db.RegisterMessage(ListBudgetsResponse)

CreateBudgetRequest = _reflection.GeneratedProtocolMessageType('CreateBudgetRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBUDGETREQUEST,
  '__module__' : 'yandex.cloud.billing.v1.budget_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.CreateBudgetRequest)
  })
_sym_db.RegisterMessage(CreateBudgetRequest)

CreateBudgetMetadata = _reflection.GeneratedProtocolMessageType('CreateBudgetMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBUDGETMETADATA,
  '__module__' : 'yandex.cloud.billing.v1.budget_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.CreateBudgetMetadata)
  })
_sym_db.RegisterMessage(CreateBudgetMetadata)


DESCRIPTOR._options = None
_GETBUDGETREQUEST.fields_by_name['id']._options = None
_LISTBUDGETSREQUEST.fields_by_name['billing_account_id']._options = None
_LISTBUDGETSREQUEST.fields_by_name['page_size']._options = None
_LISTBUDGETSREQUEST.fields_by_name['page_token']._options = None
_CREATEBUDGETREQUEST.oneofs_by_name['budget_spec']._options = None
_CREATEBUDGETREQUEST.fields_by_name['billing_account_id']._options = None
_CREATEBUDGETREQUEST.fields_by_name['name']._options = None

_BUDGETSERVICE = _descriptor.ServiceDescriptor(
  name='BudgetService',
  full_name='yandex.cloud.billing.v1.BudgetService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=886,
  serialized_end=1304,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.billing.v1.BudgetService.Get',
    index=0,
    containing_service=None,
    input_type=_GETBUDGETREQUEST,
    output_type=yandex_dot_cloud_dot_billing_dot_v1_dot_budget__pb2._BUDGET,
    serialized_options=b'\202\323\344\223\002\032\022\030/billing/v1/budgets/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.billing.v1.BudgetService.List',
    index=1,
    containing_service=None,
    input_type=_LISTBUDGETSREQUEST,
    output_type=_LISTBUDGETSRESPONSE,
    serialized_options=b'\202\323\344\223\002\025\022\023/billing/v1/budgets',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='yandex.cloud.billing.v1.BudgetService.Create',
    index=2,
    containing_service=None,
    input_type=_CREATEBUDGETREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002\030\"\023/billing/v1/budgets:\001*\262\322*\036\n\024CreateBudgetMetadata\022\006Budget',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BUDGETSERVICE)

DESCRIPTOR.services_by_name['BudgetService'] = _BUDGETSERVICE

# @@protoc_insertion_point(module_scope)
