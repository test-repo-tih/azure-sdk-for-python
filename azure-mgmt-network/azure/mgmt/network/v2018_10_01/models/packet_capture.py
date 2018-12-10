# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PacketCapture(Model):
    """Parameters that define the create packet capture operation.

    All required parameters must be populated in order to send to Azure.

    :param target: Required. The ID of the targeted resource, only VM is
     currently supported.
    :type target: str
    :param bytes_to_capture_per_packet: Number of bytes captured per packet,
     the remaining bytes are truncated. Default value: 0 .
    :type bytes_to_capture_per_packet: int
    :param total_bytes_per_session: Maximum size of the capture output.
     Default value: 1073741824 .
    :type total_bytes_per_session: int
    :param time_limit_in_seconds: Maximum duration of the capture session in
     seconds. Default value: 18000 .
    :type time_limit_in_seconds: int
    :param storage_location: Required.
    :type storage_location:
     ~azure.mgmt.network.v2018_10_01.models.PacketCaptureStorageLocation
    :param filters:
    :type filters:
     list[~azure.mgmt.network.v2018_10_01.models.PacketCaptureFilter]
    """

    _validation = {
        'target': {'required': True},
        'storage_location': {'required': True},
    }

    _attribute_map = {
        'target': {'key': 'properties.target', 'type': 'str'},
        'bytes_to_capture_per_packet': {'key': 'properties.bytesToCapturePerPacket', 'type': 'int'},
        'total_bytes_per_session': {'key': 'properties.totalBytesPerSession', 'type': 'int'},
        'time_limit_in_seconds': {'key': 'properties.timeLimitInSeconds', 'type': 'int'},
        'storage_location': {'key': 'properties.storageLocation', 'type': 'PacketCaptureStorageLocation'},
        'filters': {'key': 'properties.filters', 'type': '[PacketCaptureFilter]'},
    }

    def __init__(self, **kwargs):
        super(PacketCapture, self).__init__(**kwargs)
        self.target = kwargs.get('target', None)
        self.bytes_to_capture_per_packet = kwargs.get('bytes_to_capture_per_packet', 0)
        self.total_bytes_per_session = kwargs.get('total_bytes_per_session', 1073741824)
        self.time_limit_in_seconds = kwargs.get('time_limit_in_seconds', 18000)
        self.storage_location = kwargs.get('storage_location', None)
        self.filters = kwargs.get('filters', None)