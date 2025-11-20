import pytest
from pytest_httpx import HTTPXMock

from cloudpepper import Cloudpepper
from cloudpepper.models import Instance, InstanceDetail, InstanceCreate

@pytest.fixture
def client():
    return Cloudpepper(api_key="test-key")

@pytest.mark.asyncio
async def test_list_instances(client: Cloudpepper, httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        url="https://api.cloudpepper.com/v1/instances",
        method="GET",
        json=[
            {
                "id": "1",
                "name": "instance-1",
                "status": "running",
                "domain": "instance-1.com",
                "alias_domains": [],
                "server_id": "1",
            },
            {
                "id": "2",
                "name": "instance-2",
                "status": "stopped",
                "domain": "instance-2.com",
                "alias_domains": [],
                "server_id": "1",
            },
        ],
    )

    instances = await client.instances.list()

    assert isinstance(instances, list)
    assert len(instances) == 2
    assert isinstance(instances[0], Instance)
    assert instances[0].id == "1"
    assert instances[0].name == "instance-1"

@pytest.mark.asyncio
async def test_create_instance(client: Cloudpepper, httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        url="https://api.cloudpepper.com/v1/instances",
        method="POST",
        json={
            "id": "1",
            "name": "new-instance",
            "status": "creating",
            "domain": "new-instance.com",
            "alias_domains": [],
            "server_id": "1",
            "features": {},
            "modules": [],
            "server": {
                "id": "1",
                "name": "server-1",
                "status": "running",
                "provider": "custom",
                "provider_id": "123",
                "features": {},
                "last_heartbeat": "",
                "odoo_version": "17.0",
                "os_id": "debian-12",
                "ip_v4": "127.0.0.1",
            }
        },
    )

    instance_create = InstanceCreate(
        server_id="1",
        config={"name": "new-instance", "domain": "new-instance.com"}
    )

    instance = await client.instances.create(instance_create)

    assert isinstance(instance, InstanceDetail)
    assert instance.id == "1"
    assert instance.name == "new-instance"
