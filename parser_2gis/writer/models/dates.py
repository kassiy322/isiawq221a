from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class Dates(BaseModel):
    # Дата последнего обновления в формате ISO
    updated_at: Optional[str] = None