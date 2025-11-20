import pytest
from pytest_httpx import HTTPXMock

from cloudpepper import Cloudpepper
from cloudpepper.models import Backup, BackupSchedule

@pytest.fixture
def client():
    return Cloudpepper(api_key="test-key")

@pytest.mark.asyncio
async def test_list_backups(client: Cloudpepper, httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        url="https://api.cloudpepper.com/v1/backups",
        method="GET",
        json=[
            {
                "id": "1",
                "status": "completed",
                "completed_at": "2023-01-01T00:00:00Z",
                "size": 100,
                "notes": "test backup",
            },
            {
                "id": "2",
                "status": "failed",
                "completed_at": "2023-01-02T00:00:00Z",
                "size": 0,
                "notes": "failed backup",
            },
        ],
    )

    backups = await client.backups.list()

    assert isinstance(backups, list)
    assert len(backups) == 2
    assert isinstance(backups[0], Backup)
    assert backups[0].id == "1"
    assert backups[0].status == "completed"

@pytest.mark.asyncio
async def test_add_backup_schedule(client: Cloudpepper, httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        url="https://api.cloudpepper.com/v1/instances/1/backup-schedules",
        method="POST",
        json={
            "id": "1",
            "instance_id": "1",
            "schedule": "0 0 * * *",
            "retention": 7,
        },
    )

    backup_schedule = await client.backup_schedules.add(
        instance_id="1",
        schedule="0 0 * * *",
        retention=7,
    )

    assert isinstance(backup_schedule, BackupSchedule)
    assert backup_schedule.id == "1"
    assert backup_schedule.schedule == "0 0 * * *"
