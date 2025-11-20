import httpx
from .resources.servers import Servers
from .resources.instances import Instances

class Cloudpepper:
    def __init__(self, api_key: str, base_url: str = "https://api.cloudpepper.com/v1"):
        self.api_key = api_key
        self.base_url = base_url
        self.client = httpx.AsyncClient(
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            base_url=self.base_url
        )
        self.servers = Servers(self)
        self.instances = Instances(self)
