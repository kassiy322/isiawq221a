from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class Geometry(BaseModel):
    # Нормали геометрии
    normals: Optional[List[str]] = None
    
    # Точки геометрии  
    points: Optional[List[str]] = None
    
    # Векторы геометрии
    vectors: Optional[List[str]] = None


class Entrance(BaseModel):
    # Геометрия входа
    geometry: Optional[Geometry] = None
    
    # ID входа
    id: Optional[str] = None
    
    # Является ли основным входом
    is_primary: Optional[bool] = None
    
    # Видим ли на карте
    is_visible_on_map: Optional[bool] = None


class NearestParking(BaseModel):
    # ID ближайшей парковки
    id: Optional[str] = None


class NearestStation(BaseModel):
    # Расстояние до станции в метрах
    distance: Optional[int] = None
    
    # ID станции
    id: Optional[str] = None
    
    # Название станции
    name: Optional[str] = None
    
    # Типы маршрутов транспорта
    route_types: Optional[List[str]] = None


class Links(BaseModel):
    # Входы в базе данных
    database_entrances: Optional[List[Entrance]] = None
    
    # Входы
    entrances: Optional[List[Entrance]] = None
    
    # Ближайшие парковки
    nearest_parking: Optional[List[NearestParking]] = None
    
    # Ближайшие станции транспорта
    nearest_stations: Optional[List[NearestStation]] = None