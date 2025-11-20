from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class Server(BaseModel):
    id: str
    name: str
    status: str

class ServerDetail(Server):
    provider: str
    provider_id: str
    features: Dict[str, Any]
    last_heartbeat: str
    odoo_version: str
    os_id: str
    ip_v4: str

class Instance(BaseModel):
    id: str
    parent_id: Optional[str]
    name: str
    domain: str
    alias_domains: List[str]
    status: str
    server_id: str

class InstanceDetail(Instance):
    features: Dict[str, Any]
    modules: List[Dict[str, Any]]
    server: ServerDetail

class Backup(BaseModel):
    id: str
    instance: Optional[Instance]
    status: str
    completed_at: str
    size: int
    notes: Optional[str]

class BackupSchedule(BaseModel):
    id: str
    instance_id: str
    schedule: str
    retention: int
    provider_id: Optional[str]

class User(BaseModel):
    uid: str
    email: str
    email_verified: bool
    display_name: Optional[str]
    phone_number: Optional[str]
    metadata: Dict[str, Any]

class InstanceTemplate(BaseModel):
    id: str
    name: str
    schedules: Dict[str, Any]
    is_default: bool
