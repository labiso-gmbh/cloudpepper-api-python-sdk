from ..client import Cloudpepper
from .base import APIResource

class Users(APIResource):
    def __init__(self, client: Cloudpepper):
        super().__init__(client.client)

    async def list(self):
        return await self._get("/users")

    async def create(self, **kwargs):
        return await self._post("/users", json=kwargs)

    async def get(self, user_id: str):
        return await self._get(f"/users/{user_id}")

    async def update(self, user_id: str, **kwargs):
        return await self._put(f"/users/{user_id}", json=kwargs)

    async def delete(self, user_id: str):
        return await self._delete(f"/users/{user_id}")

    async def reset_password(self, user_id: str):
        return await self._post(f"/users/{user_id}/reset-password")
