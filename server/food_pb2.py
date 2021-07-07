# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: food.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='food.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nfood.proto\"(\n\x0b\x46oodRequest\x12\x0b\n\x03qty\x18\x01 \x01(\x05\x12\x0c\n\x04\x66ood\x18\x02 \x01(\t\"\x1f\n\x0c\x46oodResponse\x12\x0f\n\x07message\x18\x01 \x01(\t20\n\x04\x46ood\x12(\n\tOrderFood\x12\x0c.FoodRequest\x1a\r.FoodResponseb\x06proto3'
)




_FOODREQUEST = _descriptor.Descriptor(
  name='FoodRequest',
  full_name='FoodRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='qty', full_name='FoodRequest.qty', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='food', full_name='FoodRequest.food', index=1,
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
  serialized_start=14,
  serialized_end=54,
)


_FOODRESPONSE = _descriptor.Descriptor(
  name='FoodResponse',
  full_name='FoodResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='FoodResponse.message', index=0,
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
  serialized_start=56,
  serialized_end=87,
)

DESCRIPTOR.message_types_by_name['FoodRequest'] = _FOODREQUEST
DESCRIPTOR.message_types_by_name['FoodResponse'] = _FOODRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FoodRequest = _reflection.GeneratedProtocolMessageType('FoodRequest', (_message.Message,), {
  'DESCRIPTOR' : _FOODREQUEST,
  '__module__' : 'food_pb2'
  # @@protoc_insertion_point(class_scope:FoodRequest)
  })
_sym_db.RegisterMessage(FoodRequest)

FoodResponse = _reflection.GeneratedProtocolMessageType('FoodResponse', (_message.Message,), {
  'DESCRIPTOR' : _FOODRESPONSE,
  '__module__' : 'food_pb2'
  # @@protoc_insertion_point(class_scope:FoodResponse)
  })
_sym_db.RegisterMessage(FoodResponse)



_FOOD = _descriptor.ServiceDescriptor(
  name='Food',
  full_name='Food',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=89,
  serialized_end=137,
  methods=[
  _descriptor.MethodDescriptor(
    name='OrderFood',
    full_name='Food.OrderFood',
    index=0,
    containing_service=None,
    input_type=_FOODREQUEST,
    output_type=_FOODRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FOOD)

DESCRIPTOR.services_by_name['Food'] = _FOOD

# @@protoc_insertion_point(module_scope)
