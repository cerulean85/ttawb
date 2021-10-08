# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/WorkProtocolService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/WorkProtocolService.proto',
  package='com.kkennib.grpc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fproto/WorkProtocolService.proto\x12\x10\x63om.kkennib.grpc\"\x80\x01\n\x04Work\x12\n\n\x02no\x18\x01 \x01(\x05\x12\x0f\n\x07groupNo\x18\x02 \x01(\x05\x12\x10\n\x08keywords\x18\x03 \x03(\t\x12\x10\n\x08\x63hannels\x18\x04 \x03(\t\x12\x17\n\x0f\x63ollectionDates\x18\x05 \x03(\t\x12\r\n\x05state\x18\x06 \x01(\t\x12\x0f\n\x07message\x18\x07 \x01(\t\"1\n\x05Works\x12(\n\x08workList\x18\x01 \x03(\x0b\x32\x16.com.kkennib.grpc.Work\".\n\x0cWorkResponse\x12\r\n\x05state\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t2\xfa\x02\n\x13WorkProtocolService\x12>\n\x04\x65\x63ho\x12\x16.com.kkennib.grpc.Work\x1a\x1e.com.kkennib.grpc.WorkResponse\x12\x46\n\x0b\x63ollectUrls\x12\x17.com.kkennib.grpc.Works\x1a\x1e.com.kkennib.grpc.WorkResponse\x12\x46\n\x0b\x63ollectDocs\x12\x17.com.kkennib.grpc.Works\x1a\x1e.com.kkennib.grpc.WorkResponse\x12G\n\x0c\x65xtractTexts\x12\x17.com.kkennib.grpc.Works\x1a\x1e.com.kkennib.grpc.WorkResponse\x12J\n\x0f\x65xtractContents\x12\x17.com.kkennib.grpc.Works\x1a\x1e.com.kkennib.grpc.WorkResponseb\x06proto3'
)




_WORK = _descriptor.Descriptor(
  name='Work',
  full_name='com.kkennib.grpc.Work',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='no', full_name='com.kkennib.grpc.Work.no', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='groupNo', full_name='com.kkennib.grpc.Work.groupNo', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keywords', full_name='com.kkennib.grpc.Work.keywords', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channels', full_name='com.kkennib.grpc.Work.channels', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='collectionDates', full_name='com.kkennib.grpc.Work.collectionDates', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='com.kkennib.grpc.Work.state', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='com.kkennib.grpc.Work.message', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=54,
  serialized_end=182,
)


_WORKS = _descriptor.Descriptor(
  name='Works',
  full_name='com.kkennib.grpc.Works',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='workList', full_name='com.kkennib.grpc.Works.workList', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=184,
  serialized_end=233,
)


_WORKRESPONSE = _descriptor.Descriptor(
  name='WorkResponse',
  full_name='com.kkennib.grpc.WorkResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='com.kkennib.grpc.WorkResponse.state', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='com.kkennib.grpc.WorkResponse.message', index=1,
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
  serialized_start=235,
  serialized_end=281,
)

_WORKS.fields_by_name['workList'].message_type = _WORK
DESCRIPTOR.message_types_by_name['Work'] = _WORK
DESCRIPTOR.message_types_by_name['Works'] = _WORKS
DESCRIPTOR.message_types_by_name['WorkResponse'] = _WORKRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Work = _reflection.GeneratedProtocolMessageType('Work', (_message.Message,), {
  'DESCRIPTOR' : _WORK,
  '__module__' : 'proto.WorkProtocolService_pb2'
  # @@protoc_insertion_point(class_scope:com.kkennib.grpc.Work)
  })
_sym_db.RegisterMessage(Work)

Works = _reflection.GeneratedProtocolMessageType('Works', (_message.Message,), {
  'DESCRIPTOR' : _WORKS,
  '__module__' : 'proto.WorkProtocolService_pb2'
  # @@protoc_insertion_point(class_scope:com.kkennib.grpc.Works)
  })
_sym_db.RegisterMessage(Works)

WorkResponse = _reflection.GeneratedProtocolMessageType('WorkResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKRESPONSE,
  '__module__' : 'proto.WorkProtocolService_pb2'
  # @@protoc_insertion_point(class_scope:com.kkennib.grpc.WorkResponse)
  })
_sym_db.RegisterMessage(WorkResponse)



_WORKPROTOCOLSERVICE = _descriptor.ServiceDescriptor(
  name='WorkProtocolService',
  full_name='com.kkennib.grpc.WorkProtocolService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=284,
  serialized_end=662,
  methods=[
  _descriptor.MethodDescriptor(
    name='echo',
    full_name='com.kkennib.grpc.WorkProtocolService.echo',
    index=0,
    containing_service=None,
    input_type=_WORK,
    output_type=_WORKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='collectUrls',
    full_name='com.kkennib.grpc.WorkProtocolService.collectUrls',
    index=1,
    containing_service=None,
    input_type=_WORKS,
    output_type=_WORKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='collectDocs',
    full_name='com.kkennib.grpc.WorkProtocolService.collectDocs',
    index=2,
    containing_service=None,
    input_type=_WORKS,
    output_type=_WORKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='extractTexts',
    full_name='com.kkennib.grpc.WorkProtocolService.extractTexts',
    index=3,
    containing_service=None,
    input_type=_WORKS,
    output_type=_WORKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='extractContents',
    full_name='com.kkennib.grpc.WorkProtocolService.extractContents',
    index=4,
    containing_service=None,
    input_type=_WORKS,
    output_type=_WORKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WORKPROTOCOLSERVICE)

DESCRIPTOR.services_by_name['WorkProtocolService'] = _WORKPROTOCOLSERVICE

# @@protoc_insertion_point(module_scope)
