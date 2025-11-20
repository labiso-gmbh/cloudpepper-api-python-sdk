import httpx
from .resources.servers import Servers
from .resources.instances import Instances
from .resources.backups import Backups, BackupSchedules, BackupProviders
from .resources.users import Users
from .resources.instance_templates import InstanceTemplates


class Cloudpepper:
    def __init__(
        self, api_key: str, base_url: str = "https://api.cloudpepper.io"
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.client = httpx.AsyncClient(
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            base_url=self.base_url,
            timeout=httpx.Timeout(30.0, connect=5.0)
        )
        self.servers = Servers(self)
        self.instances = Instances(self)
        self.backups = Backups(self)
        self.backup_schedules = BackupSchedules(self)
        self.backup_providers = BackupProviders(self)
        self.users = Users(self)
        self.instance_templates = InstanceTemplates(self)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.aclose()

    async def close(self):
        """Close the HTTP client and release resources."""
        await self.client.aclose()
