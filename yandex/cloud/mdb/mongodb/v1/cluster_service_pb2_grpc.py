# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from yandex.cloud.mdb.mongodb.v1 import cluster_pb2 as yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__pb2
from yandex.cloud.mdb.mongodb.v1 import cluster_service_pb2 as yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class ClusterServiceStub(object):
  """A set of methods for managing MongoDB Cluster resources.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/Get',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.GetClusterRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__pb2.Cluster.FromString,
        )
    self.List = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/List',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClustersRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClustersResponse.FromString,
        )
    self.Create = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/Create',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.CreateClusterRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Update = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/Update',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.UpdateClusterRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Delete = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/Delete',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.DeleteClusterRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Start = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/Start',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.StartClusterRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Stop = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/Stop',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.StopClusterRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Move = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/Move',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.MoveClusterRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Backup = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/Backup',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.BackupClusterRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Restore = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/Restore',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.RestoreClusterRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.RescheduleMaintenance = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/RescheduleMaintenance',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.RescheduleMaintenanceRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.ListLogs = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/ListLogs',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClusterLogsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClusterLogsResponse.FromString,
        )
    self.StreamLogs = channel.unary_stream(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/StreamLogs',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.StreamClusterLogsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.StreamLogRecord.FromString,
        )
    self.ListOperations = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/ListOperations',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClusterOperationsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClusterOperationsResponse.FromString,
        )
    self.ListBackups = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/ListBackups',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClusterBackupsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClusterBackupsResponse.FromString,
        )
    self.ListHosts = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/ListHosts',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClusterHostsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClusterHostsResponse.FromString,
        )
    self.AddHosts = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/AddHosts',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.AddClusterHostsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.DeleteHosts = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/DeleteHosts',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.DeleteClusterHostsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.EnableSharding = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/EnableSharding',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.EnableClusterShardingRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.GetShard = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/GetShard',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.GetClusterShardRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__pb2.Shard.FromString,
        )
    self.ListShards = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/ListShards',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClusterShardsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClusterShardsResponse.FromString,
        )
    self.AddShard = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/AddShard',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.AddClusterShardRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.DeleteShard = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/DeleteShard',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.DeleteClusterShardRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.ResetupHosts = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/ResetupHosts',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ResetupHostsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.RestartHosts = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.ClusterService/RestartHosts',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.RestartHostsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )


class ClusterServiceServicer(object):
  """A set of methods for managing MongoDB Cluster resources.
  """

  def Get(self, request, context):
    """Returns the specified MongoDB Cluster resource.

    To get the list of available MongoDB Cluster resources, make a [List] request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """Retrieves the list of MongoDB Cluster resources that belong
    to the specified folder.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Create(self, request, context):
    """Creates a MongoDB cluster in the specified folder.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    """Updates the specified MongoDB cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Deletes the specified MongoDB cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Start(self, request, context):
    """Start the specified MongoDB cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Stop(self, request, context):
    """Stop the specified MongoDB cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Move(self, request, context):
    """Moves the specified MongoDB cluster to the specified folder.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Backup(self, request, context):
    """Creates a backup for the specified MongoDB cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Restore(self, request, context):
    """Creates a new MongoDB cluster using the specified backup.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RescheduleMaintenance(self, request, context):
    """Reschedule planned maintenance operation.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListLogs(self, request, context):
    """Retrieves logs for the specified MongoDB cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamLogs(self, request, context):
    """Same as ListLogs but using server-side streaming. Also allows for 'tail -f' semantics.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListOperations(self, request, context):
    """Retrieves the list of Operation resources for the specified cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListBackups(self, request, context):
    """Retrieves the list of available backups for the specified MongoDB cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListHosts(self, request, context):
    """Retrieves a list of hosts for the specified cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddHosts(self, request, context):
    """Creates new hosts for a cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteHosts(self, request, context):
    """Deletes the specified hosts for a cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EnableSharding(self, request, context):
    """Enables sharding for the cluster: creates 3 mongocfg and 2 mongos hosts
    that would support adding and using shards in the cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetShard(self, request, context):
    """Returns the specified shard.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListShards(self, request, context):
    """Retrieves a list of shards.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddShard(self, request, context):
    """Creates a new shard.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteShard(self, request, context):
    """Deletes the specified shard.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ResetupHosts(self, request, context):
    """Resetup hosts.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RestartHosts(self, request, context):
    """Restart hosts.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ClusterServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.GetClusterRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__pb2.Cluster.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClustersRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClustersResponse.SerializeToString,
      ),
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.CreateClusterRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.UpdateClusterRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.DeleteClusterRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Start': grpc.unary_unary_rpc_method_handler(
          servicer.Start,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.StartClusterRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Stop': grpc.unary_unary_rpc_method_handler(
          servicer.Stop,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.StopClusterRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Move': grpc.unary_unary_rpc_method_handler(
          servicer.Move,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.MoveClusterRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Backup': grpc.unary_unary_rpc_method_handler(
          servicer.Backup,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.BackupClusterRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Restore': grpc.unary_unary_rpc_method_handler(
          servicer.Restore,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.RestoreClusterRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'RescheduleMaintenance': grpc.unary_unary_rpc_method_handler(
          servicer.RescheduleMaintenance,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.RescheduleMaintenanceRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'ListLogs': grpc.unary_unary_rpc_method_handler(
          servicer.ListLogs,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClusterLogsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClusterLogsResponse.SerializeToString,
      ),
      'StreamLogs': grpc.unary_stream_rpc_method_handler(
          servicer.StreamLogs,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.StreamClusterLogsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.StreamLogRecord.SerializeToString,
      ),
      'ListOperations': grpc.unary_unary_rpc_method_handler(
          servicer.ListOperations,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClusterOperationsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClusterOperationsResponse.SerializeToString,
      ),
      'ListBackups': grpc.unary_unary_rpc_method_handler(
          servicer.ListBackups,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClusterBackupsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClusterBackupsResponse.SerializeToString,
      ),
      'ListHosts': grpc.unary_unary_rpc_method_handler(
          servicer.ListHosts,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClusterHostsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClusterHostsResponse.SerializeToString,
      ),
      'AddHosts': grpc.unary_unary_rpc_method_handler(
          servicer.AddHosts,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.AddClusterHostsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'DeleteHosts': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteHosts,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.DeleteClusterHostsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'EnableSharding': grpc.unary_unary_rpc_method_handler(
          servicer.EnableSharding,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.EnableClusterShardingRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'GetShard': grpc.unary_unary_rpc_method_handler(
          servicer.GetShard,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.GetClusterShardRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__pb2.Shard.SerializeToString,
      ),
      'ListShards': grpc.unary_unary_rpc_method_handler(
          servicer.ListShards,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClusterShardsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ListClusterShardsResponse.SerializeToString,
      ),
      'AddShard': grpc.unary_unary_rpc_method_handler(
          servicer.AddShard,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.AddClusterShardRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'DeleteShard': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteShard,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.DeleteClusterShardRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'ResetupHosts': grpc.unary_unary_rpc_method_handler(
          servicer.ResetupHosts,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.ResetupHostsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'RestartHosts': grpc.unary_unary_rpc_method_handler(
          servicer.RestartHosts,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_cluster__service__pb2.RestartHostsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'yandex.cloud.mdb.mongodb.v1.ClusterService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
