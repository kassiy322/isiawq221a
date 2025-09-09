from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class Attribute(BaseModel):
    # Уникальный идентификатор атрибута
    id: str
    
    # Название атрибута
    name: str
    
    # Тег атрибута для категоризации
    tag: Optional[str] = None


class AttributeGroup(BaseModel):
    # Список атрибутов в группе
    attributes: List[Attribute] = []
    
    # URL иконки группы атрибутов
    icon_url: Optional[str] = None
    
    # Является ли группа контекстной
    is_context: bool = False
    
    # Является ли группа основной
    is_primary: bool = False
    
    # Название группы атрибутов
    name: Optional[str] = None
    
    # Список ID рубрик, к которым относится группа
    rubric_ids: List[str] = []