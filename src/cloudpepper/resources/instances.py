from ..client import Cloudpepper
from .base import APIResource

class Instances(APIResource):
    def __init__(self, client: Cloudpepper):
        super().__init__(client.client)

    async def list(self):
        return await self._get("/instances")

    async def create(self, **kwargs):
        return await self._post("/instances", json=kwargs)

    async def get(self, instance_id: str):
        return await self._get(f"/instances/{instance_id}")

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
