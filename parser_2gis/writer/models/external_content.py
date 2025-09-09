from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class ExternalContent(BaseModel):
    # Количество элементов контента
    count: Optional[int] = None
    
    # URL основной фотографии
    main_photo_url: Optional[str] = None
    
    # Подтип контента
    subtype: Optional[str] = None
    
    # Тип контента
    type: Optional[str] = None