# Cloudpepper API Python SDK

A modern and pythonic Python SDK for the Cloudpepper API.

## Installation

```bash
pip install cloudpepper
```

## Usage

```python
from cloudpepper import Cloudpepper

client = Cloudpepper(api_key="YOUR_API_KEY")

# Get all servers
servers = client.servers.list()

# Create a new server
new_server = client.servers.create(
    type="cloudpepper",
    region="fra",
    plan="vhp-2c-4gb-amd",
    config={"odoo_version": "17.0"}
)
```

## Development

To install the development dependencies, run:

```bash
pip install -e '.[dev]'
```

To run the tests, run:

```bash
pytest
```
