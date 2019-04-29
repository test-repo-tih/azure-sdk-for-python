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


class JobStream(Model):
    """Definition of the job stream.

    :param id: Gets or sets the id of the resource.
    :type id: str
    :param job_stream_id: Gets or sets the id of the job stream.
    :type job_stream_id: str
    :param time: Gets or sets the creation time of the job.
    :type time: datetime
    :param stream_type: Gets or sets the stream type. Possible values include:
     'Progress', 'Output', 'Warning', 'Error', 'Debug', 'Verbose', 'Any'
    :type stream_type: str or ~azure.mgmt.automation.models.JobStreamType
    :param stream_text: Gets or sets the stream text.
    :type stream_text: str
    :param summary: Gets or sets the summary.
    :type summary: str
    :param value: Gets or sets the values of the job stream.
    :type value: dict[str, object]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'job_stream_id': {'key': 'properties.jobStreamId', 'type': 'str'},
        'time': {'key': 'properties.time', 'type': 'iso-8601'},
        'stream_type': {'key': 'properties.streamType', 'type': 'str'},
        'stream_text': {'key': 'properties.streamText', 'type': 'str'},
        'summary': {'key': 'properties.summary', 'type': 'str'},
        'value': {'key': 'properties.value', 'type': '{object}'},
    }

    def __init__(self, **kwargs):
        super(JobStream, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.job_stream_id = kwargs.get('job_stream_id', None)
        self.time = kwargs.get('time', None)
        self.stream_type = kwargs.get('stream_type', None)
        self.stream_text = kwargs.get('stream_text', None)
        self.summary = kwargs.get('summary', None)
        self.value = kwargs.get('value', None)