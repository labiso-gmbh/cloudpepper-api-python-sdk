from ..client import Cloudpepper
from .base import APIResource

class InstanceTemplates(APIResource):
    def __init__(self, client: Cloudpepper):
        super().__init__(client.client)

    async def create(self, **kwargs):
        return await self._post("/instance-templates", json=kwargs)

    async def set_default(self, template_id: str, **kwargs):
        return await self._put(f"/instance-templates/{template_id}/default", json=kwargs)

    async def delete(self, template_id: str):
        return await self._delete(f"/instance-templates/{template_id}")
