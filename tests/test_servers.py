import pytest
from pytest_httpx import HTTPXMock

from cloudpepper import Cloudpepper
from cloudpepper.models import Server, ServerDetail, ServerCreate

@pytest.fixture
def client():
    return Cloudpepper(api_key="test-key")

@pytest.mark.asyncio
async def test_list_servers(client: Cloudpepper, httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        url="https://api.cloudpepper.com/v1/servers",
        method="GET",
        json=[
            {
                "id": "1",
                "name": "server-1",
                "status": "running",
            },
            {
                "id": "2",
                "name": "server-2",
                "status": "stopped",
            },
        ],
    )

    servers = await client.servers.list()

    assert isinstance(servers, list)
    assert len(servers) == 2
    assert isinstance(servers[0], Server)
    assert servers[0].id == "1"
    assert servers[0].name == "server-1"

@pytest.mark.asyncio
async def test_create_server(client: Cloudpepper, httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        url="https://api.cloudpepper.com/v1/servers",
        method="POST",
        json={
            "id": "1",
            "name": "new-server",
            "status": "creating",
            "provider": "custom",
            "provider_id": "123",
            "features": {},
            "last_heartbeat": "",
            "odoo_version": "17.0",
            "os_id": "debian-12",
            "ip_v4": "127.0.0.1",
        },
    )

    server_create = ServerCreate(
        type="custom",
        region="",
        config={"odoo_version": "17.0"},
        ssh={}
    )

    server = await client.servers.create(server_create)

    assert isinstance(server, ServerDetail)
    assert server.id == "1"
    assert server.name == "new-server"
