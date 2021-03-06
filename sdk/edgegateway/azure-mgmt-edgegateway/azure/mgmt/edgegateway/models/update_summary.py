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

from .arm_base_model import ARMBaseModel


class UpdateSummary(ARMBaseModel):
    """Details about ongoing updates and availability of updates on the device.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The path ID that uniquely identifies the object.
    :vartype id: str
    :ivar name: The object name.
    :vartype name: str
    :ivar type: The hierarchical type of the object.
    :vartype type: str
    :param device_version_number: The current version of the device in format:
     1.2.17312.13.",
    :type device_version_number: str
    :param friendly_device_version_name: The current version of the device in
     text format.
    :type friendly_device_version_name: str
    :param device_last_scanned_date_time: The last time when a scan was done
     on the device.
    :type device_last_scanned_date_time: datetime
    :param last_completed_scan_job_date_time: The time when the last scan job
     was completed (success/cancelled/failed) on the appliance.
    :type last_completed_scan_job_date_time: datetime
    :ivar last_completed_download_job_date_time: The time when the last
     Download job was completed (success/cancelled/failed) on the appliance.
    :vartype last_completed_download_job_date_time: datetime
    :ivar last_completed_install_job_date_time: The time when the last Install
     job was completed (success/cancelled/failed) on the appliance.
    :vartype last_completed_install_job_date_time: datetime
    :ivar total_number_of_updates_available: The number of updates available
     for the current device version as per the last device scan.
    :vartype total_number_of_updates_available: int
    :ivar total_number_of_updates_pending_download: The total number of items
     pending download.
    :vartype total_number_of_updates_pending_download: int
    :ivar total_number_of_updates_pending_install: The total number of items
     pending install.
    :vartype total_number_of_updates_pending_install: int
    :ivar reboot_behavior: Indicates if updates are available and at least one
     of the updates needs a reboot. Possible values include: 'NeverReboots',
     'RequiresReboot', 'RequestReboot'
    :vartype reboot_behavior: str or
     ~azure.mgmt.edgegateway.models.InstallRebootBehavior
    :ivar ongoing_update_operation: The current update operation. Possible
     values include: 'None', 'Scan', 'Download', 'Install'
    :vartype ongoing_update_operation: str or
     ~azure.mgmt.edgegateway.models.UpdateOperation
    :ivar in_progress_download_job_id: The job ID of the download job in
     progress.
    :vartype in_progress_download_job_id: str
    :ivar in_progress_install_job_id: The job ID of the install job in
     progress.
    :vartype in_progress_install_job_id: str
    :ivar in_progress_download_job_started_date_time: The time when the
     currently running download (if any) started.
    :vartype in_progress_download_job_started_date_time: datetime
    :ivar in_progress_install_job_started_date_time: The time when the
     currently running install (if any) started.
    :vartype in_progress_install_job_started_date_time: datetime
    :ivar update_titles: The list of updates available for install.
    :vartype update_titles: list[str]
    :ivar total_update_size_in_bytes: The total size of updates available for
     download in bytes.
    :vartype total_update_size_in_bytes: float
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'last_completed_download_job_date_time': {'readonly': True},
        'last_completed_install_job_date_time': {'readonly': True},
        'total_number_of_updates_available': {'readonly': True},
        'total_number_of_updates_pending_download': {'readonly': True},
        'total_number_of_updates_pending_install': {'readonly': True},
        'reboot_behavior': {'readonly': True},
        'ongoing_update_operation': {'readonly': True},
        'in_progress_download_job_id': {'readonly': True},
        'in_progress_install_job_id': {'readonly': True},
        'in_progress_download_job_started_date_time': {'readonly': True},
        'in_progress_install_job_started_date_time': {'readonly': True},
        'update_titles': {'readonly': True},
        'total_update_size_in_bytes': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'device_version_number': {'key': 'properties.deviceVersionNumber', 'type': 'str'},
        'friendly_device_version_name': {'key': 'properties.friendlyDeviceVersionName', 'type': 'str'},
        'device_last_scanned_date_time': {'key': 'properties.deviceLastScannedDateTime', 'type': 'iso-8601'},
        'last_completed_scan_job_date_time': {'key': 'properties.lastCompletedScanJobDateTime', 'type': 'iso-8601'},
        'last_completed_download_job_date_time': {'key': 'properties.lastCompletedDownloadJobDateTime', 'type': 'iso-8601'},
        'last_completed_install_job_date_time': {'key': 'properties.lastCompletedInstallJobDateTime', 'type': 'iso-8601'},
        'total_number_of_updates_available': {'key': 'properties.totalNumberOfUpdatesAvailable', 'type': 'int'},
        'total_number_of_updates_pending_download': {'key': 'properties.totalNumberOfUpdatesPendingDownload', 'type': 'int'},
        'total_number_of_updates_pending_install': {'key': 'properties.totalNumberOfUpdatesPendingInstall', 'type': 'int'},
        'reboot_behavior': {'key': 'properties.rebootBehavior', 'type': 'str'},
        'ongoing_update_operation': {'key': 'properties.ongoingUpdateOperation', 'type': 'str'},
        'in_progress_download_job_id': {'key': 'properties.inProgressDownloadJobId', 'type': 'str'},
        'in_progress_install_job_id': {'key': 'properties.inProgressInstallJobId', 'type': 'str'},
        'in_progress_download_job_started_date_time': {'key': 'properties.inProgressDownloadJobStartedDateTime', 'type': 'iso-8601'},
        'in_progress_install_job_started_date_time': {'key': 'properties.inProgressInstallJobStartedDateTime', 'type': 'iso-8601'},
        'update_titles': {'key': 'properties.updateTitles', 'type': '[str]'},
        'total_update_size_in_bytes': {'key': 'properties.totalUpdateSizeInBytes', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(UpdateSummary, self).__init__(**kwargs)
        self.device_version_number = kwargs.get('device_version_number', None)
        self.friendly_device_version_name = kwargs.get('friendly_device_version_name', None)
        self.device_last_scanned_date_time = kwargs.get('device_last_scanned_date_time', None)
        self.last_completed_scan_job_date_time = kwargs.get('last_completed_scan_job_date_time', None)
        self.last_completed_download_job_date_time = None
        self.last_completed_install_job_date_time = None
        self.total_number_of_updates_available = None
        self.total_number_of_updates_pending_download = None
        self.total_number_of_updates_pending_install = None
        self.reboot_behavior = None
        self.ongoing_update_operation = None
        self.in_progress_download_job_id = None
        self.in_progress_install_job_id = None
        self.in_progress_download_job_started_date_time = None
        self.in_progress_install_job_started_date_time = None
        self.update_titles = None
        self.total_update_size_in_bytes = None
