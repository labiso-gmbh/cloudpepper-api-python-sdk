from typing import List
from ..client import Cloudpepper
from .base import APIResource
from ..models import Instance, InstanceDetail, InstanceCreate

class Instances(APIResource):
    def __init__(self, client: Cloudpepper):
        super().__init__(client.client)

    async def list(self) -> List[Instance]:
        data = await self._get("/instances")
        return [Instance(**item) for item in data]

    async def create(self, instance: InstanceCreate) -> InstanceDetail:
        return InstanceDetail(**await self._post("/instances", json=instance.dict()))

    async def get(self, instance_id: str) -> InstanceDetail:
        return InstanceDetail(**await self._get(f"/instances/{instance_id}"))

    async def delete(self, instance_id: str):
        return await self._delete(f"/instances/{instance_id}")

    async def get_status(self, instance_id: str):
        return await self._get(f"/instances/{instance_id}/status")

    async def get_config(self, instance_id: str):
        return await self._get(f"/instances/{instance_id}/config")

    async def restart(self, instance_id: str):
        return await self._post(f"/instances/{instance_id}/restart")

    async def stop(self, instance_id: str):
        return await self._post(f"/instances/{instance_id}/stop")

    async def start(self, instance_id: str):
        return await self._post(f"/instances/{instance_id}/start")

    async def update(self, instance_id: str, **kwargs):
        return await self._post(f"/instances/{instance_id}/update", json=kwargs)

    async def get_logs(self, instance_id: str, **kwargs):
        return await self._get(f"/instances/{instance_id}/logs", params=kwargs)

    async def get_installed_modules(self, instance_id: str):
        return await self._get(f"/instances/{instance_id}/installed-modules")

    async def add_module(self, instance_id: str, **kwargs):
        return await self._post(f"/instances/{instance_id}/modules", json=kwargs)

    async def update_module(self, instance_id: str, module_id: str, **kwargs):
        return await self._post(f"/instances/{instance_id}/modules/{module_id}", json=kwargs)

    async def delete_module(self, instance_id: str, module_id: str):
        return await self._delete(f"/instances/{instance_id}/modules/{module_id}")
