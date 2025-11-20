from __future__ import annotations
from typing import Dict, Any, TYPE_CHECKING
from .base import APIResource
from ..models import InstanceTemplate

if TYPE_CHECKING:
    from ..client import Cloudpepper


class InstanceTemplates(APIResource):
    def __init__(self, client: "Cloudpepper"):
        super().__init__(client.client)

    async def create(self, **kwargs) -> InstanceTemplate:
        data = await self._post("/instance-templates", json=kwargs)
        return InstanceTemplate(**data)

    async def set_default(
        self, template_id: str, **kwargs
    ) -> Dict[str, Any]:
        path = f"/instance-templates/{template_id}/default"
        return await self._put(path, json=kwargs)

    async def delete(self, template_id: str) -> Dict[str, Any]:
        return await self._delete(f"/instance-templates/{template_id}")
