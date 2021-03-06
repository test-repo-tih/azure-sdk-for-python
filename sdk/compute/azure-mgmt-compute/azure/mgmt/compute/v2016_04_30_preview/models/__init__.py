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

try:
    from ._models_py3 import AccessUri
    from ._models_py3 import AdditionalUnattendContent
    from ._models_py3 import ApiEntityReference
    from ._models_py3 import ApiError
    from ._models_py3 import ApiErrorBase
    from ._models_py3 import AvailabilitySet
    from ._models_py3 import BootDiagnostics
    from ._models_py3 import BootDiagnosticsInstanceView
    from ._models_py3 import ComputeLongRunningOperationProperties
    from ._models_py3 import CreationData
    from ._models_py3 import DataDisk
    from ._models_py3 import DataDiskImage
    from ._models_py3 import DiagnosticsProfile
    from ._models_py3 import Disk
    from ._models_py3 import DiskEncryptionSettings
    from ._models_py3 import DiskInstanceView
    from ._models_py3 import DiskUpdate
    from ._models_py3 import EncryptionSettings
    from ._models_py3 import GrantAccessData
    from ._models_py3 import HardwareProfile
    from ._models_py3 import Image
    from ._models_py3 import ImageDataDisk
    from ._models_py3 import ImageDiskReference
    from ._models_py3 import ImageOSDisk
    from ._models_py3 import ImageReference
    from ._models_py3 import ImageStorageProfile
    from ._models_py3 import InnerError
    from ._models_py3 import InstanceViewStatus
    from ._models_py3 import KeyVaultAndKeyReference
    from ._models_py3 import KeyVaultAndSecretReference
    from ._models_py3 import KeyVaultKeyReference
    from ._models_py3 import KeyVaultSecretReference
    from ._models_py3 import LinuxConfiguration
    from ._models_py3 import ManagedDiskParameters
    from ._models_py3 import NetworkInterfaceReference
    from ._models_py3 import NetworkProfile
    from ._models_py3 import OperationStatusResponse
    from ._models_py3 import OSDisk
    from ._models_py3 import OSDiskImage
    from ._models_py3 import OSProfile
    from ._models_py3 import Plan
    from ._models_py3 import PurchasePlan
    from ._models_py3 import Resource
    from ._models_py3 import ResourceUpdate
    from ._models_py3 import Sku
    from ._models_py3 import Snapshot
    from ._models_py3 import SnapshotUpdate
    from ._models_py3 import SourceVault
    from ._models_py3 import SshConfiguration
    from ._models_py3 import SshPublicKey
    from ._models_py3 import StorageProfile
    from ._models_py3 import SubResource
    from ._models_py3 import SubResourceReadOnly
    from ._models_py3 import UpdateResource
    from ._models_py3 import UpgradePolicy
    from ._models_py3 import Usage
    from ._models_py3 import UsageName
    from ._models_py3 import VaultCertificate
    from ._models_py3 import VaultSecretGroup
    from ._models_py3 import VirtualHardDisk
    from ._models_py3 import VirtualMachine
    from ._models_py3 import VirtualMachineAgentInstanceView
    from ._models_py3 import VirtualMachineCaptureParameters
    from ._models_py3 import VirtualMachineCaptureResult
    from ._models_py3 import VirtualMachineExtension
    from ._models_py3 import VirtualMachineExtensionHandlerInstanceView
    from ._models_py3 import VirtualMachineExtensionImage
    from ._models_py3 import VirtualMachineExtensionInstanceView
    from ._models_py3 import VirtualMachineExtensionsListResult
    from ._models_py3 import VirtualMachineExtensionUpdate
    from ._models_py3 import VirtualMachineIdentity
    from ._models_py3 import VirtualMachineImage
    from ._models_py3 import VirtualMachineImageResource
    from ._models_py3 import VirtualMachineInstanceView
    from ._models_py3 import VirtualMachineScaleSet
    from ._models_py3 import VirtualMachineScaleSetDataDisk
    from ._models_py3 import VirtualMachineScaleSetExtension
    from ._models_py3 import VirtualMachineScaleSetExtensionProfile
    from ._models_py3 import VirtualMachineScaleSetIdentity
    from ._models_py3 import VirtualMachineScaleSetInstanceView
    from ._models_py3 import VirtualMachineScaleSetInstanceViewStatusesSummary
    from ._models_py3 import VirtualMachineScaleSetIPConfiguration
    from ._models_py3 import VirtualMachineScaleSetManagedDiskParameters
    from ._models_py3 import VirtualMachineScaleSetNetworkConfiguration
    from ._models_py3 import VirtualMachineScaleSetNetworkProfile
    from ._models_py3 import VirtualMachineScaleSetOSDisk
    from ._models_py3 import VirtualMachineScaleSetOSProfile
    from ._models_py3 import VirtualMachineScaleSetSku
    from ._models_py3 import VirtualMachineScaleSetSkuCapacity
    from ._models_py3 import VirtualMachineScaleSetStorageProfile
    from ._models_py3 import VirtualMachineScaleSetVM
    from ._models_py3 import VirtualMachineScaleSetVMExtensionsSummary
    from ._models_py3 import VirtualMachineScaleSetVMInstanceIDs
    from ._models_py3 import VirtualMachineScaleSetVMInstanceRequiredIDs
    from ._models_py3 import VirtualMachineScaleSetVMInstanceView
    from ._models_py3 import VirtualMachineScaleSetVMProfile
    from ._models_py3 import VirtualMachineSize
    from ._models_py3 import VirtualMachineStatusCodeCount
    from ._models_py3 import WindowsConfiguration
    from ._models_py3 import WinRMConfiguration
    from ._models_py3 import WinRMListener
except (SyntaxError, ImportError):
    from ._models import AccessUri
    from ._models import AdditionalUnattendContent
    from ._models import ApiEntityReference
    from ._models import ApiError
    from ._models import ApiErrorBase
    from ._models import AvailabilitySet
    from ._models import BootDiagnostics
    from ._models import BootDiagnosticsInstanceView
    from ._models import ComputeLongRunningOperationProperties
    from ._models import CreationData
    from ._models import DataDisk
    from ._models import DataDiskImage
    from ._models import DiagnosticsProfile
    from ._models import Disk
    from ._models import DiskEncryptionSettings
    from ._models import DiskInstanceView
    from ._models import DiskUpdate
    from ._models import EncryptionSettings
    from ._models import GrantAccessData
    from ._models import HardwareProfile
    from ._models import Image
    from ._models import ImageDataDisk
    from ._models import ImageDiskReference
    from ._models import ImageOSDisk
    from ._models import ImageReference
    from ._models import ImageStorageProfile
    from ._models import InnerError
    from ._models import InstanceViewStatus
    from ._models import KeyVaultAndKeyReference
    from ._models import KeyVaultAndSecretReference
    from ._models import KeyVaultKeyReference
    from ._models import KeyVaultSecretReference
    from ._models import LinuxConfiguration
    from ._models import ManagedDiskParameters
    from ._models import NetworkInterfaceReference
    from ._models import NetworkProfile
    from ._models import OperationStatusResponse
    from ._models import OSDisk
    from ._models import OSDiskImage
    from ._models import OSProfile
    from ._models import Plan
    from ._models import PurchasePlan
    from ._models import Resource
    from ._models import ResourceUpdate
    from ._models import Sku
    from ._models import Snapshot
    from ._models import SnapshotUpdate
    from ._models import SourceVault
    from ._models import SshConfiguration
    from ._models import SshPublicKey
    from ._models import StorageProfile
    from ._models import SubResource
    from ._models import SubResourceReadOnly
    from ._models import UpdateResource
    from ._models import UpgradePolicy
    from ._models import Usage
    from ._models import UsageName
    from ._models import VaultCertificate
    from ._models import VaultSecretGroup
    from ._models import VirtualHardDisk
    from ._models import VirtualMachine
    from ._models import VirtualMachineAgentInstanceView
    from ._models import VirtualMachineCaptureParameters
    from ._models import VirtualMachineCaptureResult
    from ._models import VirtualMachineExtension
    from ._models import VirtualMachineExtensionHandlerInstanceView
    from ._models import VirtualMachineExtensionImage
    from ._models import VirtualMachineExtensionInstanceView
    from ._models import VirtualMachineExtensionsListResult
    from ._models import VirtualMachineExtensionUpdate
    from ._models import VirtualMachineIdentity
    from ._models import VirtualMachineImage
    from ._models import VirtualMachineImageResource
    from ._models import VirtualMachineInstanceView
    from ._models import VirtualMachineScaleSet
    from ._models import VirtualMachineScaleSetDataDisk
    from ._models import VirtualMachineScaleSetExtension
    from ._models import VirtualMachineScaleSetExtensionProfile
    from ._models import VirtualMachineScaleSetIdentity
    from ._models import VirtualMachineScaleSetInstanceView
    from ._models import VirtualMachineScaleSetInstanceViewStatusesSummary
    from ._models import VirtualMachineScaleSetIPConfiguration
    from ._models import VirtualMachineScaleSetManagedDiskParameters
    from ._models import VirtualMachineScaleSetNetworkConfiguration
    from ._models import VirtualMachineScaleSetNetworkProfile
    from ._models import VirtualMachineScaleSetOSDisk
    from ._models import VirtualMachineScaleSetOSProfile
    from ._models import VirtualMachineScaleSetSku
    from ._models import VirtualMachineScaleSetSkuCapacity
    from ._models import VirtualMachineScaleSetStorageProfile
    from ._models import VirtualMachineScaleSetVM
    from ._models import VirtualMachineScaleSetVMExtensionsSummary
    from ._models import VirtualMachineScaleSetVMInstanceIDs
    from ._models import VirtualMachineScaleSetVMInstanceRequiredIDs
    from ._models import VirtualMachineScaleSetVMInstanceView
    from ._models import VirtualMachineScaleSetVMProfile
    from ._models import VirtualMachineSize
    from ._models import VirtualMachineStatusCodeCount
    from ._models import WindowsConfiguration
    from ._models import WinRMConfiguration
    from ._models import WinRMListener
from ._paged_models import AvailabilitySetPaged
from ._paged_models import DiskPaged
from ._paged_models import ImagePaged
from ._paged_models import SnapshotPaged
from ._paged_models import UsagePaged
from ._paged_models import VirtualMachinePaged
from ._paged_models import VirtualMachineScaleSetPaged
from ._paged_models import VirtualMachineScaleSetSkuPaged
from ._paged_models import VirtualMachineScaleSetVMPaged
from ._paged_models import VirtualMachineSizePaged
from ._compute_management_client_enums import (
    StatusLevelTypes,
    OperatingSystemTypes,
    VirtualMachineSizeTypes,
    CachingTypes,
    DiskCreateOptionTypes,
    StorageAccountTypes,
    PassNames,
    ComponentNames,
    SettingNames,
    ProtocolTypes,
    ResourceIdentityType,
    UpgradeMode,
    OperatingSystemStateTypes,
    VirtualMachineScaleSetSkuScaleType,
    DiskCreateOption,
    AccessLevel,
    InstanceViewTypes,
)

__all__ = [
    'AccessUri',
    'AdditionalUnattendContent',
    'ApiEntityReference',
    'ApiError',
    'ApiErrorBase',
    'AvailabilitySet',
    'BootDiagnostics',
    'BootDiagnosticsInstanceView',
    'ComputeLongRunningOperationProperties',
    'CreationData',
    'DataDisk',
    'DataDiskImage',
    'DiagnosticsProfile',
    'Disk',
    'DiskEncryptionSettings',
    'DiskInstanceView',
    'DiskUpdate',
    'EncryptionSettings',
    'GrantAccessData',
    'HardwareProfile',
    'Image',
    'ImageDataDisk',
    'ImageDiskReference',
    'ImageOSDisk',
    'ImageReference',
    'ImageStorageProfile',
    'InnerError',
    'InstanceViewStatus',
    'KeyVaultAndKeyReference',
    'KeyVaultAndSecretReference',
    'KeyVaultKeyReference',
    'KeyVaultSecretReference',
    'LinuxConfiguration',
    'ManagedDiskParameters',
    'NetworkInterfaceReference',
    'NetworkProfile',
    'OperationStatusResponse',
    'OSDisk',
    'OSDiskImage',
    'OSProfile',
    'Plan',
    'PurchasePlan',
    'Resource',
    'ResourceUpdate',
    'Sku',
    'Snapshot',
    'SnapshotUpdate',
    'SourceVault',
    'SshConfiguration',
    'SshPublicKey',
    'StorageProfile',
    'SubResource',
    'SubResourceReadOnly',
    'UpdateResource',
    'UpgradePolicy',
    'Usage',
    'UsageName',
    'VaultCertificate',
    'VaultSecretGroup',
    'VirtualHardDisk',
    'VirtualMachine',
    'VirtualMachineAgentInstanceView',
    'VirtualMachineCaptureParameters',
    'VirtualMachineCaptureResult',
    'VirtualMachineExtension',
    'VirtualMachineExtensionHandlerInstanceView',
    'VirtualMachineExtensionImage',
    'VirtualMachineExtensionInstanceView',
    'VirtualMachineExtensionsListResult',
    'VirtualMachineExtensionUpdate',
    'VirtualMachineIdentity',
    'VirtualMachineImage',
    'VirtualMachineImageResource',
    'VirtualMachineInstanceView',
    'VirtualMachineScaleSet',
    'VirtualMachineScaleSetDataDisk',
    'VirtualMachineScaleSetExtension',
    'VirtualMachineScaleSetExtensionProfile',
    'VirtualMachineScaleSetIdentity',
    'VirtualMachineScaleSetInstanceView',
    'VirtualMachineScaleSetInstanceViewStatusesSummary',
    'VirtualMachineScaleSetIPConfiguration',
    'VirtualMachineScaleSetManagedDiskParameters',
    'VirtualMachineScaleSetNetworkConfiguration',
    'VirtualMachineScaleSetNetworkProfile',
    'VirtualMachineScaleSetOSDisk',
    'VirtualMachineScaleSetOSProfile',
    'VirtualMachineScaleSetSku',
    'VirtualMachineScaleSetSkuCapacity',
    'VirtualMachineScaleSetStorageProfile',
    'VirtualMachineScaleSetVM',
    'VirtualMachineScaleSetVMExtensionsSummary',
    'VirtualMachineScaleSetVMInstanceIDs',
    'VirtualMachineScaleSetVMInstanceRequiredIDs',
    'VirtualMachineScaleSetVMInstanceView',
    'VirtualMachineScaleSetVMProfile',
    'VirtualMachineSize',
    'VirtualMachineStatusCodeCount',
    'WindowsConfiguration',
    'WinRMConfiguration',
    'WinRMListener',
    'AvailabilitySetPaged',
    'VirtualMachineSizePaged',
    'VirtualMachinePaged',
    'UsagePaged',
    'ImagePaged',
    'VirtualMachineScaleSetPaged',
    'VirtualMachineScaleSetSkuPaged',
    'VirtualMachineScaleSetVMPaged',
    'DiskPaged',
    'SnapshotPaged',
    'StatusLevelTypes',
    'OperatingSystemTypes',
    'VirtualMachineSizeTypes',
    'CachingTypes',
    'DiskCreateOptionTypes',
    'StorageAccountTypes',
    'PassNames',
    'ComponentNames',
    'SettingNames',
    'ProtocolTypes',
    'ResourceIdentityType',
    'UpgradeMode',
    'OperatingSystemStateTypes',
    'VirtualMachineScaleSetSkuScaleType',
    'DiskCreateOption',
    'AccessLevel',
    'InstanceViewTypes',
]
