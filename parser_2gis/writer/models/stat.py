from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class Stat(BaseModel):
    # Timestamp рекламы
    adst: Optional[int] = None
    
    # Является ли рекламируемым
    is_advertised: Optional[bool] = None
    
    # ID рубрики
    rubr: Optional[str] = None
    
    # Тип источника
    source_type: Optional[int] = None