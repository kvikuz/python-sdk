# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from yandex.cloud.compute.v1.instancegroup import instance_group_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__pb2
from yandex.cloud.compute.v1.instancegroup import instance_group_service_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class InstanceGroupServiceStub(object):
  """A set of methods for managing InstanceGroup resources.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/yandex.cloud.compute.v1.instancegroup.InstanceGroupService/Get',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.GetInstanceGroupRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__pb2.InstanceGroup.FromString,
        )
    self.List = channel.unary_unary(
        '/yandex.cloud.compute.v1.instancegroup.InstanceGroupService/List',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.ListInstanceGroupsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.ListInstanceGroupsResponse.FromString,
        )
    self.Create = channel.unary_unary(
        '/yandex.cloud.compute.v1.instancegroup.InstanceGroupService/Create',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.CreateInstanceGroupRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.CreateFromYaml = channel.unary_unary(
        '/yandex.cloud.compute.v1.instancegroup.InstanceGroupService/CreateFromYaml',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.CreateInstanceGroupFromYamlRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Update = channel.unary_unary(
        '/yandex.cloud.compute.v1.instancegroup.InstanceGroupService/Update',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.UpdateInstanceGroupRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.UpdateFromYaml = channel.unary_unary(
        '/yandex.cloud.compute.v1.instancegroup.InstanceGroupService/UpdateFromYaml',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.UpdateInstanceGroupFromYamlRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Stop = channel.unary_unary(
        '/yandex.cloud.compute.v1.instancegroup.InstanceGroupService/Stop',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.StopInstanceGroupRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Start = channel.unary_unary(
        '/yandex.cloud.compute.v1.instancegroup.InstanceGroupService/Start',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.StartInstanceGroupRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Delete = channel.unary_unary(
        '/yandex.cloud.compute.v1.instancegroup.InstanceGroupService/Delete',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.DeleteInstanceGroupRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.ListInstances = channel.unary_unary(
        '/yandex.cloud.compute.v1.instancegroup.InstanceGroupService/ListInstances',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.ListInstanceGroupInstancesRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.ListInstanceGroupInstancesResponse.FromString,
        )
    self.ListOperations = channel.unary_unary(
        '/yandex.cloud.compute.v1.instancegroup.InstanceGroupService/ListOperations',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.ListInstanceGroupOperationsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.ListInstanceGroupOperationsResponse.FromString,
        )
    self.ListLogRecords = channel.unary_unary(
        '/yandex.cloud.compute.v1.instancegroup.InstanceGroupService/ListLogRecords',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.ListInstanceGroupLogRecordsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.ListInstanceGroupLogRecordsResponse.FromString,
        )


class InstanceGroupServiceServicer(object):
  """A set of methods for managing InstanceGroup resources.
  """

  def Get(self, request, context):
    """Returns the specified InstanceGroup resource.

    To get the list of available InstanceGroup resources, make a [List] request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """Retrieves the list of InstanceGroup resources in the specified folder.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Create(self, request, context):
    """Creates an instance group in the specified folder.
    This method starts an operation that can be cancelled by another operation.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateFromYaml(self, request, context):
    """Creates an instance group in the specified folder from a YAML file.
    This method starts an operation that can be cancelled by another operation.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    """Updates the specified instance group.
    This method starts an operation that can be cancelled by another operation.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateFromYaml(self, request, context):
    """Updates the specified instance group from a YAML file.
    This method starts an operation that can be cancelled by another operation.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Stop(self, request, context):
    """Stops the specified instance group.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Start(self, request, context):
    """Starts the specified instance group.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Deletes the specified instance group.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListInstances(self, request, context):
    """Lists instances for the specified instance group.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListOperations(self, request, context):
    """Lists operations for the specified instance group.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListLogRecords(self, request, context):
    """Lists logs for the specified instance group.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_InstanceGroupServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.GetInstanceGroupRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__pb2.InstanceGroup.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.ListInstanceGroupsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.ListInstanceGroupsResponse.SerializeToString,
      ),
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.CreateInstanceGroupRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'CreateFromYaml': grpc.unary_unary_rpc_method_handler(
          servicer.CreateFromYaml,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.CreateInstanceGroupFromYamlRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.UpdateInstanceGroupRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'UpdateFromYaml': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateFromYaml,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.UpdateInstanceGroupFromYamlRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Stop': grpc.unary_unary_rpc_method_handler(
          servicer.Stop,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.StopInstanceGroupRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Start': grpc.unary_unary_rpc_method_handler(
          servicer.Start,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.StartInstanceGroupRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.DeleteInstanceGroupRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'ListInstances': grpc.unary_unary_rpc_method_handler(
          servicer.ListInstances,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.ListInstanceGroupInstancesRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.ListInstanceGroupInstancesResponse.SerializeToString,
      ),
      'ListOperations': grpc.unary_unary_rpc_method_handler(
          servicer.ListOperations,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.ListInstanceGroupOperationsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.ListInstanceGroupOperationsResponse.SerializeToString,
      ),
      'ListLogRecords': grpc.unary_unary_rpc_method_handler(
          servicer.ListLogRecords,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.ListInstanceGroupLogRecordsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__service__pb2.ListInstanceGroupLogRecordsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'yandex.cloud.compute.v1.instancegroup.InstanceGroupService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))