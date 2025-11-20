import httpx

class APIResource:
    def __init__(self, client: httpx.AsyncClient):
        self.client = client

    async def _get(self, path: str, params: dict = None):
        response = await self.client.get(path, params=params)
        response.raise_for_status()
        return response.json()

    async def _post(self, path: str, json: dict = None):
        response = await self.client.post(path, json=json)
        response.raise_for_status()
        return response.json()

    async def _patch(self, path: str, json: dict = None):
        response = await self.client.patch(path, json=json)
        response.raise_for_status()
        return response.json()

    async def _put(self, path: str, json: dict = None):
        response = await self.client.put(path, json=json)
        response.raise_for_status()
        return response.json()

    async def _delete(self, path: str):
        response = await self.client.delete(path)
        response.raise_for_status()
        return response.json()
