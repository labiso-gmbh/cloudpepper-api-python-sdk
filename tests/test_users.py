import pytest
from pytest_httpx import HTTPXMock

from cloudpepper import Cloudpepper
from cloudpepper.models import User

@pytest.fixture
def client():
    return Cloudpepper(api_key="test-key")

@pytest.mark.asyncio
async def test_list_users(client: Cloudpepper, httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        url="https://api.cloudpepper.com/v1/users",
        method="GET",
        json=[
            {
                "uid": "1",
                "email": "user1@example.com",
                "email_verified": True,
                "metadata": {},
            },
            {
                "uid": "2",
                "email": "user2@example.com",
                "email_verified": False,
                "metadata": {},
            },
        ],
    )

    users = await client.users.list()

    assert isinstance(users, list)
    assert len(users) == 2
    assert isinstance(users[0], User)
    assert users[0].uid == "1"
    assert users[0].email == "user1@example.com"

@pytest.mark.asyncio
async def test_create_user(client: Cloudpepper, httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        url="https://api.cloudpepper.com/v1/users",
        method="POST",
        json={
            "uid": "1",
            "email": "new-user@example.com",
            "email_verified": False,
            "metadata": {},
        },
    )

    user = await client.users.create(
        email="new-user@example.com",
        password="password",
        role="USER",
    )

    assert isinstance(user, User)
    assert user.uid == "1"
    assert user.email == "new-user@example.com"
