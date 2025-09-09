from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class Flags(BaseModel):
    # Есть ли фотографии
    photos: Optional[bool] = None
    
    # Центр районной области
    is_district_area_center: Optional[bool] = None