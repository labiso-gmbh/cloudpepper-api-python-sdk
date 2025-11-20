from typing import List
from ..client import Cloudpepper
from .base import APIResource
from ..models import Backup, BackupSchedule

class Backups(APIResource):
    def __init__(self, client: Cloudpepper):
        super().__init__(client.client)

    async def list(self) -> List[Backup]:
        data = await self._get("/backups")
        return [Backup(**item) for item in data]

    async def get(self, backup_id: str) -> Backup:
        return Backup(**await self._get(f"/backups/{backup_id}"))

    async def update(self, backup_id: str, **kwargs) -> Backup:
        return Backup(**await self._patch(f"/backups/{backup_id}", json=kwargs))

    async def delete(self, backup_id: str):
        return await self._delete(f"/backups/{backup_id}")

class BackupSchedules(APIResource):
    def __init__(self, client: Cloudpepper):
        super().__init__(client.client)

    async def add(self, instance_id: str, **kwargs) -> BackupSchedule:
        return BackupSchedule(**await self._post(f"/instances/{instance_id}/backup-schedules", json=kwargs))
    
    async def update(self, instance_id: str, schedule_id: str, **kwargs) -> BackupSchedule:
        return BackupSchedule(**await self._patch(f"/instances/{instance_id}/backup-schedules/{schedule_id}", json=kwargs))

    async def delete(self, instance_id: str, schedule_id: str):
        return await self._delete(f"/instances/{instance_id}/backup-schedules/{schedule_id}")

class BackupProviders(APIResource):
    def __init__(self, client: Cloudpepper):
        super().__init__(client.client)

    async def add(self, **kwargs):
        return await self._post("/backup-providers", json=kwargs)
    
    async def set_default(self, provider_id: str):
        return await self._post(f"/backup-providers/{provider_id}/set-default")

    async def delete(self, provider_id: str):
        return await self._delete(f"/backup-providers/{provider_id}")
