import httpx
from typing import Optional, Dict, Any
from ..exceptions import (
    AuthenticationError,
    PermissionError,
    NotFoundError,
    ValidationError,
    RateLimitError,
    ServerError,
    APIError,
)


class APIResource:
    def __init__(self, client: httpx.AsyncClient):
        self.client = client

    def _handle_error(self, response: httpx.Response) -> None:
        """Convert HTTP errors to custom exceptions."""
        try:
            error_data = response.json()
            error_message = error_data.get("error", response.text)
        except Exception:
            # If response is not JSON, use status text or truncated body
            error_message = (
                response.text[:200] if len(response.text) < 200
                else f"{response.text[:200]}..."
            )

        status_code = response.status_code

        if status_code == 401:
            raise AuthenticationError(
                error_message, status_code, response
            )
        elif status_code == 403:
            raise PermissionError(error_message, status_code, response)
        elif status_code == 404:
            raise NotFoundError(error_message, status_code, response)
        elif status_code == 400:
            raise ValidationError(error_message, status_code, response)
        elif status_code == 429:
            raise RateLimitError(error_message, status_code, response)
        elif 500 <= status_code < 600:
            raise ServerError(error_message, status_code, response)
        else:
            raise APIError(error_message, status_code, response)

    async def _get(
        self, path: str, params: Optional[Dict[str, Any]] = None
    ) -> Any:
        response = await self.client.get(path, params=params)
        if response.status_code >= 400:
            self._handle_error(response)
        return response.json()

    async def _post(
        self, path: str, json: Optional[Dict[str, Any]] = None
    ) -> Any:
        response = await self.client.post(path, json=json)
        if response.status_code >= 400:
            self._handle_error(response)
        return response.json()

    async def _patch(
        self, path: str, json: Optional[Dict[str, Any]] = None
    ) -> Any:
        response = await self.client.patch(path, json=json)
        if response.status_code >= 400:
            self._handle_error(response)
        return response.json()

    async def _put(
        self, path: str, json: Optional[Dict[str, Any]] = None
    ) -> Any:
        response = await self.client.put(path, json=json)
        if response.status_code >= 400:
            self._handle_error(response)
        return response.json()

    async def _delete(self, path: str) -> Any:
        response = await self.client.delete(path)
        if response.status_code >= 400:
            self._handle_error(response)
        return response.json()
