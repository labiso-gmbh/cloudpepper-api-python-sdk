# Cloudpepper API Python SDK

[![PyPI version](https://badge.fury.io/py/cloudpepper.svg)](https://badge.fury.io/py/cloudpepper)
[![Python Support](https://img.shields.io/pypi/pyversions/cloudpepper.svg)](https://pypi.org/project/cloudpepper/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modern, async-first Python SDK for the Cloudpepper API. Manage your Odoo instances, servers, backups, and users programmatically with ease.

## Features

- 🚀 **Async/Await Support** - Built on `httpx` for high-performance async operations
- 🎯 **Type-Safe** - Full type hints with Pydantic models for auto-completion and validation
- 🔧 **Comprehensive** - Complete coverage of the Cloudpepper API
- 📦 **Easy to Use** - Intuitive, resource-based API design
- 🛡️ **Error Handling** - Custom exceptions for better error management
- 🔄 **Context Manager** - Automatic resource cleanup with async context managers

## Installation

Install from PyPI using pip:

```bash
pip install cloudpepper
```

## Quick Start

```python
import asyncio
from cloudpepper import Cloudpepper

async def main():
    async with Cloudpepper(api_key="your_api_key") as client:
        # List all servers
        servers = await client.servers.list()
        print(f"Found {len(servers)} servers")
        
        # List all instances
        instances = await client.instances.list()
        for instance in instances:
            print(f"Instance: {instance.name} ({instance.status})")

asyncio.run(main())
```

## Usage Examples

### Server Management

```python
from cloudpepper import Cloudpepper
from cloudpepper.models import ServerCreate

async with Cloudpepper(api_key="your_api_key") as client:
    # Create a new server
    server = await client.servers.create(
        ServerCreate(
            type="cloudpepper",
            region="fra",
            plan="vhp-2c-4gb-amd",
            config={"odoo_version": "17.0"}
        )
    )
    print(f"Server created: {server.id}")
    
    # Get server details
    server_detail = await client.servers.get(server.id)
    print(f"Server status: {server_detail.status}")
    
    # Update server
    await client.servers.update(
        server.id,
        name="Production Server"
    )
    
    # Delete server
    await client.servers.delete(server.id)
```

### Instance Management

```python
from cloudpepper import Cloudpepper
from cloudpepper.models import InstanceCreate

async with Cloudpepper(api_key="your_api_key") as client:
    # Create a new Odoo instance
    instance = await client.instances.create(
        InstanceCreate(
            server_id="server-uuid",
            config={
                "name": "mycompany",
                "domain": "mycompany.example.com",
                "odoo_version": "17.0"
            }
        )
    )
    
    # Get instance status
    status = await client.instances.get_status(instance.id)
    print(f"Instance status: {status}")
    
    # Restart instance
    await client.instances.restart(instance.id)
    
    # Stop instance
    await client.instances.stop(instance.id)
    
    # Start instance
    await client.instances.start(instance.id)
```

### Backup Management

```python
async with Cloudpepper(api_key="your_api_key") as client:
    # List all backups
    backups = await client.backups.list()
    
    # Get specific backup
    backup = await client.backups.get("backup-id")
    
    # Add backup schedule
    schedule = await client.backup_schedules.add(
        instance_id="instance-uuid",
        schedule="0 2 * * *",  # Daily at 2 AM
        retention=7
    )
    
    # Update backup schedule
    await client.backup_schedules.update(
        instance_id="instance-uuid",
        schedule_id=schedule.id,
        retention=14
    )
    
    # Delete backup schedule
    await client.backup_schedules.delete(
        instance_id="instance-uuid",
        schedule_id=schedule.id
    )
```

### User Management

```python
async with Cloudpepper(api_key="your_api_key") as client:
    # List all users
    users = await client.users.list()
    
    # Create a new user
    user = await client.users.create(
        email="user@example.com",
        password="secure_password",
        role="USER"
    )
    
    # Update user permissions
    await client.users.update(
        user_id=user.uid,
        role="ADMIN"
    )
    
    # Delete user
    await client.users.delete(user.uid)
```

### Module Management

```python
async with Cloudpepper(api_key="your_api_key") as client:
    # Add a module to an instance
    module = await client.instances.add_module(
        instance_id="instance-uuid",
        repo="https://github.com/OCA/web.git",
        branch="17.0"
    )
    
    # Update module
    await client.instances.update_module(
        instance_id="instance-uuid",
        module_id=module["id"],
        branch="18.0"
    )
    
    # Delete module
    await client.instances.delete_module(
        instance_id="instance-uuid",
        module_id=module["id"]
    )
```

## Error Handling

The SDK provides custom exceptions for better error management:

```python
from cloudpepper import Cloudpepper
from cloudpepper.exceptions import (
    AuthenticationError,
    NotFoundError,
    ValidationError,
    RateLimitError,
    ServerError
)

async with Cloudpepper(api_key="your_api_key") as client:
    try:
        server = await client.servers.get("non-existent-id")
    except AuthenticationError:
        print("Invalid API key")
    except NotFoundError:
        print("Server not found")
    except ValidationError as e:
        print(f"Invalid request: {e.message}")
    except RateLimitError:
        print("Rate limit exceeded")
    except ServerError:
        print("Server error occurred")
```

## Configuration

### Custom Base URL

```python
client = Cloudpepper(
    api_key="your_api_key",
    base_url="https://custom.api.cloudpepper.io"
)
```

### Timeout Configuration

```python
import httpx

client = Cloudpepper(api_key="your_api_key")
client.client.timeout = httpx.Timeout(60.0, connect=10.0)
```

## API Resources

The SDK provides access to the following Cloudpepper API resources:

- **Servers** - Create, manage, and monitor cloud servers
- **Instances** - Deploy and manage Odoo instances
- **Backups** - Manage backups and backup schedules
- **Backup Providers** - Configure backup storage providers
- **Users** - Manage user accounts and permissions
- **Instance Templates** - Create reusable instance configurations

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/labiso-gmbh/cloudpepper-api-python-sdk.git
cd cloudpepper-api-python-sdk

# Install in development mode with dev dependencies
pip install -e '.[dev]'
```

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/cloudpepper --cov-report=html

# Run specific test file
pytest tests/test_instances.py
```

### Project Structure

```
cloudpepper-api-python-sdk/
├── src/
│   └── cloudpepper/
│       ├── __init__.py
│       ├── client.py           # Main client class
│       ├── exceptions.py       # Custom exceptions
│       ├── models.py          # Pydantic models
│       └── resources/         # API resource classes
│           ├── base.py
│           ├── servers.py
│           ├── instances.py
│           ├── backups.py
│           └── users.py
├── tests/                     # Test suite
├── pyproject.toml            # Project configuration
└── README.md
```

## Requirements

- Python >= 3.8
- httpx
- pydantic

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- **Documentation**: [Cloudpepper API Docs](https://api.cloudpepper.io)
- **Issues**: [GitHub Issues](https://github.com/labiso-gmbh/cloudpepper-api-python-sdk/issues)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Changelog

### Version 0.1.0 (2025-11-20)

- Initial release
- Async/await support with httpx
- Full API coverage for servers, instances, backups, and users
- Type-safe Pydantic models
- Custom exception handling
- Comprehensive test suite
