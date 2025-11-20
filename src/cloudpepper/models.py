from pydantic import BaseModel, ConfigDict
from typing import Optional, List, Dict, Any


class Server(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    name: str
    status: str


class ServerCreate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    type: str
    region: str
    plan: Optional[str] = None
    size: Optional[str] = None
    instance_type: Optional[str] = None
    config: Dict[str, Any]
    ssh: Optional[Dict[str, Any]] = None


class ServerDetail(Server):
    provider: str
    provider_id: str
    features: Dict[str, Any]
    last_heartbeat: str
    odoo_version: str
    os_id: str
    ip_v4: str


class Instance(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    parent_id: Optional[str] = None
    name: str
    domain: str
    alias_domains: Optional[List[str]] = None
    status: str
    server_id: Optional[str] = None


class InstanceCreate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    server_id: str
    backup_id: Optional[str] = None
    parent_id: Optional[str] = None
    config: Dict[str, Any]
    options: Optional[Dict[str, Any]] = None


class InstanceDetail(Instance):
    features: Dict[str, Any]
    modules: List[Dict[str, Any]]
    server: ServerDetail


class Backup(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    instance: Optional[Instance] = None
    status: str
    completed_at: str
    size: int
    notes: Optional[str] = None


class BackupSchedule(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    instance_id: str
    schedule: str
    retention: int
    provider_id: Optional[str] = None


class User(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    uid: str
    email: str
    email_verified: bool
    display_name: Optional[str] = None
    phone_number: Optional[str] = None
    metadata: Dict[str, Any]


class InstanceTemplate(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    name: str
    schedules: Dict[str, Any]
    is_default: bool
