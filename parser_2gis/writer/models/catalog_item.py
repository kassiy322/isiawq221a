from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel

from .address import Address
from .adm_div_item import AdmDivItem
from .attribute_group import AttributeGroup
from .contact_group import ContactGroup
from .context import Context
from .dates import Dates
from .external_content import ExternalContent
from .flags import Flags
from .links import Links
from .name_ex import NameEx
from .org import Org
from .point import Point
from .reviews import Reviews
from .rubric import Rubric
from .schedule import Schedule
from .stat import Stat


class CatalogItem(BaseModel):
    # Уникальный идентификатор филиала организации (например "141265769336625_f91d4H3777058262347790J0e8g28765")
    id: str

    # Адрес объекта
    address: Optional[Address] = None

    # Уточнение о местоположении филиала по указанному адресу (например "офис 413")
    address_comment: Optional[str] = None

    # Представление поля address в виде одной строки (например "Димитрова проспект, 7")
    address_name: Optional[str] = None

    # Принадлежность к административной территории
    adm_div: List[AdmDivItem] = []

    # Алиас города, в котором находится объект (например "perm")
    city_alias: Optional[str] = None

    # Контакты филиала
    contact_groups: List[ContactGroup] = []

    # Текущая локаль для региона (например "ru_RU")
    locale: str

    # Полное собственное название филиала или название организации (например "Солнышко, кафе")
    name: Optional[str] = None

    # Расширеное название филиала
    name_ex: Optional[NameEx] = None

    # Отзывы
    reviews: Optional[Reviews] = None

    # Организация
    org: Optional[Org] = None

    # Координаты точки поиска, заданные в системе координат WGS84 в формате lon, lat
    point: Optional[Point] = None

    # Уникальный идентификатор проекта
    region_id: Optional[str] = None

    # Уникальный идентификатор сегмента
    segment_id: Optional[str] = None

    # Рубрики филиала
    rubrics: List[Rubric] = []

    # Время работы
    schedule: Optional[Schedule] = None

    # Смещение таймзоны в минутах относительно UTC0 (например "420")
    timezone_offset: Optional[int] = None

    # Тип объекта
    type: str

    # Признак удаленного объекта
    is_deleted: Optional[bool] = None
    
    # Группы атрибутов
    attribute_groups: Optional[List[AttributeGroup]] = None
    
    # Контекст поиска
    context: Optional[Context] = None
    
    # Даты обновления
    dates: Optional[Dates] = None
    
    # Внешний контент (фотографии и др.)
    external_content: Optional[List[ExternalContent]] = None
    
    # Флаги объекта
    flags: Optional[Flags] = None
    
    # Есть ли модель рекламы
    has_ads_model: Optional[bool] = None
    
    # Есть ли информация о квартирах
    has_apartments_info: Optional[bool] = None
    
    # Есть ли скидки
    has_discount: Optional[bool] = None
    
    # Есть ли динамическая загруженность
    has_dynamic_congestion: Optional[bool] = None
    
    # Есть ли обмен валют
    has_exchange: Optional[bool] = None
    
    # Есть ли товары
    has_goods: Optional[bool] = None
    
    # Есть ли закрепленные товары
    has_pinned_goods: Optional[bool] = None
    
    # Есть ли недвижимость
    has_realty: Optional[bool] = None
    
    # Промотируется ли объект
    is_promoted: Optional[bool] = None
    
    # Ссылки и геометрия
    links: Optional[Links] = None
    
    # Категория POI
    poi_category: Optional[str] = None
    
    # Статистическая информация
    stat: Optional[Stat] = None

    @property
    def url(self) -> str:
        return 'https://2gis.com/firm/%s' % self.id.split('_')[0]

    @property
    def timezone(self) -> str | None:
        if self.timezone_offset is None:
            return None
        sign = '-' if self.timezone_offset < 0 else '+'
        minutes = abs(self.timezone_offset)
        h = minutes // 60
        m = minutes % 60
        return '{}{:02d}:{:02d}'.format(sign, h, m)
