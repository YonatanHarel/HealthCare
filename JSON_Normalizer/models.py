"""
pydantic models
"""
from datetime import datetime
from pydantic import BaseModel


class AIResult(BaseModel):
    score: float
    label: str


class Scan(BaseModel):
    scan_id: str
    ai_result: AIResult


class Data(BaseModel):
    patient_id: str
    scan: Scan


class Meta(BaseModel):
    model_version: str
    received_at: datetime


class ScanEntry(BaseModel):
    meta: Meta
    data: Data
