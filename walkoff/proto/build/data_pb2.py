# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='data.proto',
  package='core',
  serialized_pb=_b('\n\ndata.proto\x12\x04\x63ore\"\x83\x03\n\x07Message\x12 \n\x04type\x18\x01 \x01(\x0e\x32\x12.core.Message.Type\x12\x12\n\nevent_name\x18\x02 \x01(\t\x12/\n\x0fworkflow_packet\x18\x03 \x01(\x0b\x32\x14.core.WorkflowPacketH\x00\x12+\n\raction_packet\x18\x04 \x01(\x0b\x32\x12.core.ActionPacketH\x00\x12-\n\x0egeneral_packet\x18\x05 \x01(\x0b\x32\x13.core.GeneralPacketH\x00\x12+\n\x0emessage_packet\x18\x06 \x01(\x0b\x32\x11.core.UserMessageH\x00\"~\n\x04Type\x12\x12\n\x0eWORKFLOWPACKET\x10\x01\x12\x16\n\x12WORKFLOWPACKETDATA\x10\x02\x12\x10\n\x0c\x41\x43TIONPACKET\x10\x03\x12\x14\n\x10\x41\x43TIONPACKETDATA\x10\x04\x12\x11\n\rGENERALPACKET\x10\x05\x12\x0f\n\x0bUSERMESSAGE\x10\x06\x42\x08\n\x06packet\"@\n\x0eWorkflowSender\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x14\n\x0c\x65xecution_id\x18\x03 \x01(\t\"O\n\x0eWorkflowPacket\x12$\n\x06sender\x18\x01 \x01(\x0b\x32\x14.core.WorkflowSender\x12\x17\n\x0f\x61\x64\x64itional_data\x18\x02 \x01(\t\"M\n\x08\x41rgument\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x11\n\treference\x18\x03 \x01(\t\x12\x11\n\tselection\x18\x04 \x01(\t\"\x9e\x02\n\x0c\x41\x63tionPacket\x12/\n\x06sender\x18\x01 \x01(\x0b\x32\x1f.core.ActionPacket.ActionSender\x12&\n\x08workflow\x18\x02 \x01(\x0b\x32\x14.core.WorkflowSender\x12\x17\n\x0f\x61\x64\x64itional_data\x18\x03 \x01(\t\x1a\x9b\x01\n\x0c\x41\x63tionSender\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x14\n\x0c\x65xecution_id\x18\x03 \x01(\t\x12\x10\n\x08\x61pp_name\x18\x04 \x01(\t\x12\x13\n\x0b\x61\x63tion_name\x18\x05 \x01(\t\x12!\n\targuments\x18\x06 \x03(\x0b\x32\x0e.core.Argument\x12\x11\n\tdevice_id\x18\t \x01(\x05\"\x99\x01\n\rGeneralPacket\x12\x31\n\x06sender\x18\x01 \x01(\x0b\x32!.core.GeneralPacket.GeneralSender\x12&\n\x08workflow\x18\x02 \x01(\x0b\x32\x14.core.WorkflowSender\x1a-\n\rGeneralSender\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x61pp_name\x18\x02 \x01(\t\"\xe5\x01\n\x13\x43ommunicationPacket\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x1e.core.CommunicationPacket.Type\x12\x39\n\x18workflow_control_message\x18\x02 \x01(\x0b\x32\x15.core.WorkflowControlH\x00\x12\x31\n\x14\x63\x61se_control_message\x18\x03 \x01(\x0b\x32\x11.core.CaseControlH\x00\"(\n\x04Type\x12\x0c\n\x08WORKFLOW\x10\x01\x12\x08\n\x04\x43\x41SE\x10\x02\x12\x08\n\x04\x45XIT\x10\x03\x42\x08\n\x06packet\"x\n\x0fWorkflowControl\x12(\n\x04type\x18\x01 \x01(\x0e\x32\x1a.core.WorkflowControl.Type\x12\x1d\n\x15workflow_execution_id\x18\x02 \x01(\t\"\x1c\n\x04Type\x12\t\n\x05PAUSE\x10\x01\x12\t\n\x05\x41\x42ORT\x10\x03\".\n\x10\x43\x61seSubscription\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x65vents\x18\x02 \x03(\t\"\x9a\x01\n\x0b\x43\x61seControl\x12$\n\x04type\x18\x01 \x01(\x0e\x32\x16.core.CaseControl.Type\x12\n\n\x02id\x18\x02 \x01(\x03\x12-\n\rsubscriptions\x18\x03 \x03(\x0b\x32\x16.core.CaseSubscription\"*\n\x04Type\x12\n\n\x06\x43REATE\x10\x01\x12\n\n\x06UPDATE\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\"\xbc\x01\n\x0bUserMessage\x12/\n\x06sender\x18\x01 \x01(\x0b\x32\x1f.core.ActionPacket.ActionSender\x12&\n\x08workflow\x18\x02 \x01(\x0b\x32\x14.core.WorkflowSender\x12\x0f\n\x07subject\x18\x03 \x01(\t\x12\x0c\n\x04\x62ody\x18\x04 \x01(\t\x12\x17\n\x0frequires_reauth\x18\x05 \x01(\x08\x12\r\n\x05users\x18\x06 \x03(\x05\x12\r\n\x05roles\x18\x07 \x03(\x05\"\x8e\x01\n\x16\x45xecuteWorkflowMessage\x12\x13\n\x0bworkflow_id\x18\x01 \x01(\t\x12\x1d\n\x15workflow_execution_id\x18\x02 \x01(\t\x12\r\n\x05start\x18\x03 \x01(\t\x12!\n\targuments\x18\x04 \x03(\x0b\x32\x0e.core.Argument\x12\x0e\n\x06resume\x18\x05 \x01(\x08')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_MESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='core.Message.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WORKFLOWPACKET', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORKFLOWPACKETDATA', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIONPACKET', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIONPACKETDATA', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GENERALPACKET', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USERMESSAGE', index=5, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=272,
  serialized_end=398,
)
_sym_db.RegisterEnumDescriptor(_MESSAGE_TYPE)

_COMMUNICATIONPACKET_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='core.CommunicationPacket.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WORKFLOW', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CASE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXIT', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1261,
  serialized_end=1301,
)
_sym_db.RegisterEnumDescriptor(_COMMUNICATIONPACKET_TYPE)

_WORKFLOWCONTROL_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='core.WorkflowControl.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PAUSE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ABORT', index=1, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1405,
  serialized_end=1433,
)
_sym_db.RegisterEnumDescriptor(_WORKFLOWCONTROL_TYPE)

_CASECONTROL_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='core.CaseControl.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CREATE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1596,
  serialized_end=1638,
)
_sym_db.RegisterEnumDescriptor(_CASECONTROL_TYPE)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='core.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='core.Message.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_name', full_name='core.Message.event_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='workflow_packet', full_name='core.Message.workflow_packet', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action_packet', full_name='core.Message.action_packet', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='general_packet', full_name='core.Message.general_packet', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_packet', full_name='core.Message.message_packet', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESSAGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='packet', full_name='core.Message.packet',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=21,
  serialized_end=408,
)


_WORKFLOWSENDER = _descriptor.Descriptor(
  name='WorkflowSender',
  full_name='core.WorkflowSender',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='core.WorkflowSender.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='core.WorkflowSender.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='execution_id', full_name='core.WorkflowSender.execution_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=410,
  serialized_end=474,
)


_WORKFLOWPACKET = _descriptor.Descriptor(
  name='WorkflowPacket',
  full_name='core.WorkflowPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='core.WorkflowPacket.sender', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='additional_data', full_name='core.WorkflowPacket.additional_data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=476,
  serialized_end=555,
)


_ARGUMENT = _descriptor.Descriptor(
  name='Argument',
  full_name='core.Argument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='core.Argument.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='core.Argument.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference', full_name='core.Argument.reference', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='selection', full_name='core.Argument.selection', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=557,
  serialized_end=634,
)


_ACTIONPACKET_ACTIONSENDER = _descriptor.Descriptor(
  name='ActionSender',
  full_name='core.ActionPacket.ActionSender',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='core.ActionPacket.ActionSender.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='core.ActionPacket.ActionSender.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='execution_id', full_name='core.ActionPacket.ActionSender.execution_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_name', full_name='core.ActionPacket.ActionSender.app_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action_name', full_name='core.ActionPacket.ActionSender.action_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arguments', full_name='core.ActionPacket.ActionSender.arguments', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_id', full_name='core.ActionPacket.ActionSender.device_id', index=6,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=768,
  serialized_end=923,
)

_ACTIONPACKET = _descriptor.Descriptor(
  name='ActionPacket',
  full_name='core.ActionPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='core.ActionPacket.sender', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='workflow', full_name='core.ActionPacket.workflow', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='additional_data', full_name='core.ActionPacket.additional_data', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ACTIONPACKET_ACTIONSENDER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=637,
  serialized_end=923,
)


_GENERALPACKET_GENERALSENDER = _descriptor.Descriptor(
  name='GeneralSender',
  full_name='core.GeneralPacket.GeneralSender',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='core.GeneralPacket.GeneralSender.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_name', full_name='core.GeneralPacket.GeneralSender.app_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1034,
  serialized_end=1079,
)

_GENERALPACKET = _descriptor.Descriptor(
  name='GeneralPacket',
  full_name='core.GeneralPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='core.GeneralPacket.sender', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='workflow', full_name='core.GeneralPacket.workflow', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GENERALPACKET_GENERALSENDER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=926,
  serialized_end=1079,
)


_COMMUNICATIONPACKET = _descriptor.Descriptor(
  name='CommunicationPacket',
  full_name='core.CommunicationPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='core.CommunicationPacket.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='workflow_control_message', full_name='core.CommunicationPacket.workflow_control_message', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='case_control_message', full_name='core.CommunicationPacket.case_control_message', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMMUNICATIONPACKET_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='packet', full_name='core.CommunicationPacket.packet',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1082,
  serialized_end=1311,
)


_WORKFLOWCONTROL = _descriptor.Descriptor(
  name='WorkflowControl',
  full_name='core.WorkflowControl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='core.WorkflowControl.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='workflow_execution_id', full_name='core.WorkflowControl.workflow_execution_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _WORKFLOWCONTROL_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1313,
  serialized_end=1433,
)


_CASESUBSCRIPTION = _descriptor.Descriptor(
  name='CaseSubscription',
  full_name='core.CaseSubscription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='core.CaseSubscription.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='events', full_name='core.CaseSubscription.events', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1435,
  serialized_end=1481,
)


_CASECONTROL = _descriptor.Descriptor(
  name='CaseControl',
  full_name='core.CaseControl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='core.CaseControl.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='core.CaseControl.id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subscriptions', full_name='core.CaseControl.subscriptions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CASECONTROL_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1484,
  serialized_end=1638,
)


_USERMESSAGE = _descriptor.Descriptor(
  name='UserMessage',
  full_name='core.UserMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='core.UserMessage.sender', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='workflow', full_name='core.UserMessage.workflow', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subject', full_name='core.UserMessage.subject', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='body', full_name='core.UserMessage.body', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requires_reauth', full_name='core.UserMessage.requires_reauth', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='users', full_name='core.UserMessage.users', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roles', full_name='core.UserMessage.roles', index=6,
      number=7, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1641,
  serialized_end=1829,
)


_EXECUTEWORKFLOWMESSAGE = _descriptor.Descriptor(
  name='ExecuteWorkflowMessage',
  full_name='core.ExecuteWorkflowMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workflow_id', full_name='core.ExecuteWorkflowMessage.workflow_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='workflow_execution_id', full_name='core.ExecuteWorkflowMessage.workflow_execution_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='core.ExecuteWorkflowMessage.start', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arguments', full_name='core.ExecuteWorkflowMessage.arguments', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resume', full_name='core.ExecuteWorkflowMessage.resume', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1832,
  serialized_end=1974,
)

_MESSAGE.fields_by_name['type'].enum_type = _MESSAGE_TYPE
_MESSAGE.fields_by_name['workflow_packet'].message_type = _WORKFLOWPACKET
_MESSAGE.fields_by_name['action_packet'].message_type = _ACTIONPACKET
_MESSAGE.fields_by_name['general_packet'].message_type = _GENERALPACKET
_MESSAGE.fields_by_name['message_packet'].message_type = _USERMESSAGE
_MESSAGE_TYPE.containing_type = _MESSAGE
_MESSAGE.oneofs_by_name['packet'].fields.append(
  _MESSAGE.fields_by_name['workflow_packet'])
_MESSAGE.fields_by_name['workflow_packet'].containing_oneof = _MESSAGE.oneofs_by_name['packet']
_MESSAGE.oneofs_by_name['packet'].fields.append(
  _MESSAGE.fields_by_name['action_packet'])
_MESSAGE.fields_by_name['action_packet'].containing_oneof = _MESSAGE.oneofs_by_name['packet']
_MESSAGE.oneofs_by_name['packet'].fields.append(
  _MESSAGE.fields_by_name['general_packet'])
_MESSAGE.fields_by_name['general_packet'].containing_oneof = _MESSAGE.oneofs_by_name['packet']
_MESSAGE.oneofs_by_name['packet'].fields.append(
  _MESSAGE.fields_by_name['message_packet'])
_MESSAGE.fields_by_name['message_packet'].containing_oneof = _MESSAGE.oneofs_by_name['packet']
_WORKFLOWPACKET.fields_by_name['sender'].message_type = _WORKFLOWSENDER
_ACTIONPACKET_ACTIONSENDER.fields_by_name['arguments'].message_type = _ARGUMENT
_ACTIONPACKET_ACTIONSENDER.containing_type = _ACTIONPACKET
_ACTIONPACKET.fields_by_name['sender'].message_type = _ACTIONPACKET_ACTIONSENDER
_ACTIONPACKET.fields_by_name['workflow'].message_type = _WORKFLOWSENDER
_GENERALPACKET_GENERALSENDER.containing_type = _GENERALPACKET
_GENERALPACKET.fields_by_name['sender'].message_type = _GENERALPACKET_GENERALSENDER
_GENERALPACKET.fields_by_name['workflow'].message_type = _WORKFLOWSENDER
_COMMUNICATIONPACKET.fields_by_name['type'].enum_type = _COMMUNICATIONPACKET_TYPE
_COMMUNICATIONPACKET.fields_by_name['workflow_control_message'].message_type = _WORKFLOWCONTROL
_COMMUNICATIONPACKET.fields_by_name['case_control_message'].message_type = _CASECONTROL
_COMMUNICATIONPACKET_TYPE.containing_type = _COMMUNICATIONPACKET
_COMMUNICATIONPACKET.oneofs_by_name['packet'].fields.append(
  _COMMUNICATIONPACKET.fields_by_name['workflow_control_message'])
_COMMUNICATIONPACKET.fields_by_name['workflow_control_message'].containing_oneof = _COMMUNICATIONPACKET.oneofs_by_name['packet']
_COMMUNICATIONPACKET.oneofs_by_name['packet'].fields.append(
  _COMMUNICATIONPACKET.fields_by_name['case_control_message'])
_COMMUNICATIONPACKET.fields_by_name['case_control_message'].containing_oneof = _COMMUNICATIONPACKET.oneofs_by_name['packet']
_WORKFLOWCONTROL.fields_by_name['type'].enum_type = _WORKFLOWCONTROL_TYPE
_WORKFLOWCONTROL_TYPE.containing_type = _WORKFLOWCONTROL
_CASECONTROL.fields_by_name['type'].enum_type = _CASECONTROL_TYPE
_CASECONTROL.fields_by_name['subscriptions'].message_type = _CASESUBSCRIPTION
_CASECONTROL_TYPE.containing_type = _CASECONTROL
_USERMESSAGE.fields_by_name['sender'].message_type = _ACTIONPACKET_ACTIONSENDER
_USERMESSAGE.fields_by_name['workflow'].message_type = _WORKFLOWSENDER
_EXECUTEWORKFLOWMESSAGE.fields_by_name['arguments'].message_type = _ARGUMENT
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['WorkflowSender'] = _WORKFLOWSENDER
DESCRIPTOR.message_types_by_name['WorkflowPacket'] = _WORKFLOWPACKET
DESCRIPTOR.message_types_by_name['Argument'] = _ARGUMENT
DESCRIPTOR.message_types_by_name['ActionPacket'] = _ACTIONPACKET
DESCRIPTOR.message_types_by_name['GeneralPacket'] = _GENERALPACKET
DESCRIPTOR.message_types_by_name['CommunicationPacket'] = _COMMUNICATIONPACKET
DESCRIPTOR.message_types_by_name['WorkflowControl'] = _WORKFLOWCONTROL
DESCRIPTOR.message_types_by_name['CaseSubscription'] = _CASESUBSCRIPTION
DESCRIPTOR.message_types_by_name['CaseControl'] = _CASECONTROL
DESCRIPTOR.message_types_by_name['UserMessage'] = _USERMESSAGE
DESCRIPTOR.message_types_by_name['ExecuteWorkflowMessage'] = _EXECUTEWORKFLOWMESSAGE

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:core.Message)
  ))
_sym_db.RegisterMessage(Message)

WorkflowSender = _reflection.GeneratedProtocolMessageType('WorkflowSender', (_message.Message,), dict(
  DESCRIPTOR = _WORKFLOWSENDER,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:core.WorkflowSender)
  ))
_sym_db.RegisterMessage(WorkflowSender)

WorkflowPacket = _reflection.GeneratedProtocolMessageType('WorkflowPacket', (_message.Message,), dict(
  DESCRIPTOR = _WORKFLOWPACKET,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:core.WorkflowPacket)
  ))
_sym_db.RegisterMessage(WorkflowPacket)

Argument = _reflection.GeneratedProtocolMessageType('Argument', (_message.Message,), dict(
  DESCRIPTOR = _ARGUMENT,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:core.Argument)
  ))
_sym_db.RegisterMessage(Argument)

ActionPacket = _reflection.GeneratedProtocolMessageType('ActionPacket', (_message.Message,), dict(

  ActionSender = _reflection.GeneratedProtocolMessageType('ActionSender', (_message.Message,), dict(
    DESCRIPTOR = _ACTIONPACKET_ACTIONSENDER,
    __module__ = 'data_pb2'
    # @@protoc_insertion_point(class_scope:core.ActionPacket.ActionSender)
    ))
  ,
  DESCRIPTOR = _ACTIONPACKET,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:core.ActionPacket)
  ))
_sym_db.RegisterMessage(ActionPacket)
_sym_db.RegisterMessage(ActionPacket.ActionSender)

GeneralPacket = _reflection.GeneratedProtocolMessageType('GeneralPacket', (_message.Message,), dict(

  GeneralSender = _reflection.GeneratedProtocolMessageType('GeneralSender', (_message.Message,), dict(
    DESCRIPTOR = _GENERALPACKET_GENERALSENDER,
    __module__ = 'data_pb2'
    # @@protoc_insertion_point(class_scope:core.GeneralPacket.GeneralSender)
    ))
  ,
  DESCRIPTOR = _GENERALPACKET,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:core.GeneralPacket)
  ))
_sym_db.RegisterMessage(GeneralPacket)
_sym_db.RegisterMessage(GeneralPacket.GeneralSender)

CommunicationPacket = _reflection.GeneratedProtocolMessageType('CommunicationPacket', (_message.Message,), dict(
  DESCRIPTOR = _COMMUNICATIONPACKET,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:core.CommunicationPacket)
  ))
_sym_db.RegisterMessage(CommunicationPacket)

WorkflowControl = _reflection.GeneratedProtocolMessageType('WorkflowControl', (_message.Message,), dict(
  DESCRIPTOR = _WORKFLOWCONTROL,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:core.WorkflowControl)
  ))
_sym_db.RegisterMessage(WorkflowControl)

CaseSubscription = _reflection.GeneratedProtocolMessageType('CaseSubscription', (_message.Message,), dict(
  DESCRIPTOR = _CASESUBSCRIPTION,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:core.CaseSubscription)
  ))
_sym_db.RegisterMessage(CaseSubscription)

CaseControl = _reflection.GeneratedProtocolMessageType('CaseControl', (_message.Message,), dict(
  DESCRIPTOR = _CASECONTROL,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:core.CaseControl)
  ))
_sym_db.RegisterMessage(CaseControl)

UserMessage = _reflection.GeneratedProtocolMessageType('UserMessage', (_message.Message,), dict(
  DESCRIPTOR = _USERMESSAGE,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:core.UserMessage)
  ))
_sym_db.RegisterMessage(UserMessage)

ExecuteWorkflowMessage = _reflection.GeneratedProtocolMessageType('ExecuteWorkflowMessage', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTEWORKFLOWMESSAGE,
  __module__ = 'data_pb2'
  # @@protoc_insertion_point(class_scope:core.ExecuteWorkflowMessage)
  ))
_sym_db.RegisterMessage(ExecuteWorkflowMessage)


# @@protoc_insertion_point(module_scope)
