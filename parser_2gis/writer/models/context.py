from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class Context(BaseModel):
    # Факторы остановки поиска
    stop_factors: Optional[list] = None


class ContextStopFactor(BaseModel):
    # Название фактора
    name: Optional[str] = None
    
    # Тип фактора (например, "rubric")
    type: Optional[str] = None