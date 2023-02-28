# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.compute.v1 import gpu_cluster_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__pb2
from yandex.cloud.compute.v1 import gpu_cluster_service_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class GpuClusterServiceStub(object):
    """A set of methods for managing GPU clusters.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.compute.v1.GpuClusterService/Get',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.GetGpuClusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__pb2.GpuCluster.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.compute.v1.GpuClusterService/List',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.ListGpuClustersRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.ListGpuClustersResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.compute.v1.GpuClusterService/Create',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.CreateGpuClusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.compute.v1.GpuClusterService/Update',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.UpdateGpuClusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.compute.v1.GpuClusterService/Delete',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.DeleteGpuClusterRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.compute.v1.GpuClusterService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.ListGpuClusterOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.ListGpuClusterOperationsResponse.FromString,
                )
        self.ListInstances = channel.unary_unary(
                '/yandex.cloud.compute.v1.GpuClusterService/ListInstances',
                request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.ListGpuClusterInstancesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.ListGpuClusterInstancesResponse.FromString,
                )


class GpuClusterServiceServicer(object):
    """A set of methods for managing GPU clusters.
    """

    def Get(self, request, context):
        """Returns the specified GPU cluster.

        To get the list of available GPU clusters, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of GPU clusters in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a GPU cluster in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified GPU cluster.

        Currently only name, description and labels can be updated.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified GPU cluster.

        GPU cluster can be deleted only if it doesn't have any instances associated with it.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """Lists operations for the specified GPU cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListInstances(self, request, context):
        """List instances created in this GPU cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GpuClusterServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.GetGpuClusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__pb2.GpuCluster.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.ListGpuClustersRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.ListGpuClustersResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.CreateGpuClusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.UpdateGpuClusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.DeleteGpuClusterRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.ListGpuClusterOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.ListGpuClusterOperationsResponse.SerializeToString,
            ),
            'ListInstances': grpc.unary_unary_rpc_method_handler(
                    servicer.ListInstances,
                    request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.ListGpuClusterInstancesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.ListGpuClusterInstancesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.compute.v1.GpuClusterService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GpuClusterService(object):
    """A set of methods for managing GPU clusters.
    """

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.GpuClusterService/Get',
            yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.GetGpuClusterRequest.SerializeToString,
            yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__pb2.GpuCluster.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.GpuClusterService/List',
            yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.ListGpuClustersRequest.SerializeToString,
            yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.ListGpuClustersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.GpuClusterService/Create',
            yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.CreateGpuClusterRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.GpuClusterService/Update',
            yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.UpdateGpuClusterRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.GpuClusterService/Delete',
            yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.DeleteGpuClusterRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.GpuClusterService/ListOperations',
            yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.ListGpuClusterOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.ListGpuClusterOperationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListInstances(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.compute.v1.GpuClusterService/ListInstances',
            yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.ListGpuClusterInstancesRequest.SerializeToString,
            yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__service__pb2.ListGpuClusterInstancesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)