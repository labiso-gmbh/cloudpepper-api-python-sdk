from __future__ import annotations
from typing import List, Dict, Any, TYPE_CHECKING
from .base import APIResource
from ..models import Server, ServerDetail, ServerCreate

if TYPE_CHECKING:
    from ..client import Cloudpepper


class Servers(APIResource):
    def __init__(self, client: "Cloudpepper"):
        super().__init__(client.client)

    async def list(self) -> List[Server]:
        data = await self._get("/servers")
        return [Server(**item) for item in data]

    async def create(self, server: ServerCreate) -> ServerDetail:
        data = await self._post("/servers", json=server.model_dump())
        return ServerDetail(**data)

    async def get(self, server_id: str) -> ServerDetail:
        return ServerDetail(**await self._get(f"/servers/{server_id}"))

    async def update(self, server_id: str, **kwargs) -> ServerDetail:
        data = await self._patch(f"/servers/{server_id}", json=kwargs)
        return ServerDetail(**data)

    async def delete(self, server_id: str) -> Dict[str, Any]:
        return await self._delete(f"/servers/{server_id}")

    async def get_version(self, server_id: str) -> Dict[str, Any]:
        return await self._get(f"/servers/{server_id}/version")

    async def get_stats(self, server_id: str) -> Dict[str, Any]:
        return await self._get(f"/servers/{server_id}/stats")

    async def query_prometheus(
        self, server_id: str, **kwargs
    ) -> Dict[str, Any]:
        return await self._get(
            f"/servers/{server_id}/prometheus", params=kwargs
        )

    async def update_odoo(self, server_id: str) -> Dict[str, Any]:
        return await self._post(f"/servers/{server_id}/update")
