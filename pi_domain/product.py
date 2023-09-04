from typing import Dict, List, Set
from enum import Enum
from pydantic import BaseModel, Extra
from pydantic.dataclasses import dataclass, ConfigDict

class Key:
    pass


class AttributeType(Enum):
    multiple: bool = False
    String = 0


class Attribute(BaseModel):
    pass


class Value:
    pass


class ScopeType(Enum):
    Public = 1
    Private = 2
    Secure = 3


class Scope(BaseModel):
    name: str
    type: ScopeType
    attributes: Dict[str, Attribute] = []

    def add_attribute(self, name: str, attribute: Attribute) -> 'Scope':
        return self


class RelationshipType(Enum):
    DependsUpon = 1
    DerivedFrom = 2
    Supersedes = 3


class Relationship(BaseModel):
    target_id: str
    relationship_type: RelationshipType
    scopes: Set[Scope]


class KeyTypes(Enum):
    ProductId = "PID"
    AccreditedSystemId = "ASID"


class ProductStatus(Enum):
    Invalid = 0
    Valid = 1


class Product(BaseModel):
    short_name: str
    long_name: str
    status: ProductStatus = ProductStatus.Invalid
    keys: dict[str, str] = dict()
    values: dict[str, str] = dict()
    scopes: Set[Scope] = set()
    dependency_scopes: Set[Scope] = set()

    def validate(self):
        pass

    def set_key(self, name: str, value: str):
        pass

    def set_value(self, name: str, value: any):
        pass

    def add_scope(self, scope: Scope) -> 'Product':
        return self

    def add_dependency_scope(self, scope: Scope) -> 'Product':
        return self

    def add_relationship(self, type: RelationshipType, product: 'Product') -> 'Product':
        return self
