from __future__ import annotations
from typing import List, Dict, Any, TYPE_CHECKING
from .base import APIResource
from ..models import Backup, BackupSchedule

if TYPE_CHECKING:
    from ..client import Cloudpepper


class Backups(APIResource):
    def __init__(self, client: "Cloudpepper"):
        super().__init__(client.client)

    async def list(self) -> List[Backup]:
        data = await self._get("/backups")
        return [Backup(**item) for item in data]

    async def get(self, backup_id: str) -> Backup:
        return Backup(**await self._get(f"/backups/{backup_id}"))

    async def update(self, backup_id: str, **kwargs) -> Backup:
        data = await self._patch(f"/backups/{backup_id}", json=kwargs)
        return Backup(**data)

    async def delete(self, backup_id: str) -> Dict[str, Any]:
        return await self._delete(f"/backups/{backup_id}")


class BackupSchedules(APIResource):
    def __init__(self, client: "Cloudpepper"):
        super().__init__(client.client)

    async def add(
        self, instance_id: str, **kwargs
    ) -> BackupSchedule:
        path = f"/instances/{instance_id}/backup-schedules"
        data = await self._post(path, json=kwargs)
        return BackupSchedule(**data)

    async def update(
        self, instance_id: str, schedule_id: str, **kwargs
    ) -> BackupSchedule:
        path = f"/instances/{instance_id}/backup-schedules/{schedule_id}"
        data = await self._patch(path, json=kwargs)
        return BackupSchedule(**data)

    async def delete(
        self, instance_id: str, schedule_id: str
    ) -> Dict[str, Any]:
        path = f"/instances/{instance_id}/backup-schedules/{schedule_id}"
        return await self._delete(path)


class BackupProviders(APIResource):
    def __init__(self, client: "Cloudpepper"):
        super().__init__(client.client)

    async def add(self, **kwargs) -> Dict[str, Any]:
        return await self._post("/backup-providers", json=kwargs)

    async def set_default(self, provider_id: str) -> Dict[str, Any]:
        return await self._post(
            f"/backup-providers/{provider_id}/set-default"
        )

    async def delete(self, provider_id: str) -> Dict[str, Any]:
        return await self._delete(f"/backup-providers/{provider_id}")
