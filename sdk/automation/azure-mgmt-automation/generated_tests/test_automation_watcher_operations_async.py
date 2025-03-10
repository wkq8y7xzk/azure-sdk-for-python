# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.automation.aio import AutomationClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestAutomationWatcherOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(AutomationClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_create_or_update(self, resource_group):
        response = await self.client.watcher.create_or_update(
            resource_group_name=resource_group.name,
            automation_account_name="str",
            watcher_name="str",
            parameters={
                "creationTime": "2020-02-20 00:00:00",
                "description": "str",
                "etag": "str",
                "executionFrequencyInSeconds": 0,
                "id": "str",
                "lastModifiedBy": "str",
                "lastModifiedTime": "2020-02-20 00:00:00",
                "location": "str",
                "name": "str",
                "scriptName": "str",
                "scriptParameters": {"str": "str"},
                "scriptRunOn": "str",
                "status": "str",
                "tags": {"str": "str"},
                "type": "str",
            },
            api_version="2020-01-13-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.watcher.get(
            resource_group_name=resource_group.name,
            automation_account_name="str",
            watcher_name="str",
            api_version="2020-01-13-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_update(self, resource_group):
        response = await self.client.watcher.update(
            resource_group_name=resource_group.name,
            automation_account_name="str",
            watcher_name="str",
            parameters={"executionFrequencyInSeconds": 0, "name": "str"},
            api_version="2020-01-13-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_delete(self, resource_group):
        response = await self.client.watcher.delete(
            resource_group_name=resource_group.name,
            automation_account_name="str",
            watcher_name="str",
            api_version="2020-01-13-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_start(self, resource_group):
        response = await self.client.watcher.start(
            resource_group_name=resource_group.name,
            automation_account_name="str",
            watcher_name="str",
            api_version="2020-01-13-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_stop(self, resource_group):
        response = await self.client.watcher.stop(
            resource_group_name=resource_group.name,
            automation_account_name="str",
            watcher_name="str",
            api_version="2020-01-13-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_automation_account(self, resource_group):
        response = self.client.watcher.list_by_automation_account(
            resource_group_name=resource_group.name,
            automation_account_name="str",
            api_version="2020-01-13-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
