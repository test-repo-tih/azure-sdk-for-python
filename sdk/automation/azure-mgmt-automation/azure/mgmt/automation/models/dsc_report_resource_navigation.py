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


class DscReportResourceNavigation(Model):
    """Navigation for DSC Report Resource.

    :param resource_id: Gets or sets the ID of the resource to navigate to.
    :type resource_id: str
    """

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DscReportResourceNavigation, self).__init__(**kwargs)
        self.resource_id = kwargs.get('resource_id', None)
