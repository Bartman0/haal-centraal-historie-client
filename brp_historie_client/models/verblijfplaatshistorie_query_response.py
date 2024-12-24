# coding: utf-8

"""
    BRP historie bevragen

    API voor het zoeken en raadplegen van historische verblijfplaatsen, partners, nationaliteiten en verblijfstitels uit de BRP (inclusief de RNI).  Zie de [Functionele documentatie](https://github.com/VNG-Realisatie/Haal-Centraal-BRP-historie-bevragen/tree/v1.0.0/features) voor nadere toelichting. 

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from brp_historie_client.models.abstract_verblijfplaats_voorkomen import AbstractVerblijfplaatsVoorkomen
from brp_historie_client.models.opschorting_bijhouding import OpschortingBijhouding
from typing import Optional, Set
from typing_extensions import Self

class VerblijfplaatshistorieQueryResponse(BaseModel):
    """
    VerblijfplaatshistorieQueryResponse
    """ # noqa: E501
    verblijfplaatsen: Optional[List[AbstractVerblijfplaatsVoorkomen]] = None
    opschorting_bijhouding: Optional[OpschortingBijhouding] = Field(default=None, alias="opschortingBijhouding")
    geheimhouding_persoonsgegevens: Optional[StrictBool] = Field(default=None, description="Gegevens mogen niet worden verstrekt aan derden / maatschappelijke instellingen. ", alias="geheimhoudingPersoonsgegevens")
    __properties: ClassVar[List[str]] = ["verblijfplaatsen", "opschortingBijhouding", "geheimhoudingPersoonsgegevens"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of VerblijfplaatshistorieQueryResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in verblijfplaatsen (list)
        _items = []
        if self.verblijfplaatsen:
            for _item_verblijfplaatsen in self.verblijfplaatsen:
                if _item_verblijfplaatsen:
                    _items.append(_item_verblijfplaatsen.to_dict())
            _dict['verblijfplaatsen'] = _items
        # override the default output from pydantic by calling `to_dict()` of opschorting_bijhouding
        if self.opschorting_bijhouding:
            _dict['opschortingBijhouding'] = self.opschorting_bijhouding.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VerblijfplaatshistorieQueryResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "verblijfplaatsen": [AbstractVerblijfplaatsVoorkomen.from_dict(_item) for _item in obj["verblijfplaatsen"]] if obj.get("verblijfplaatsen") is not None else None,
            "opschortingBijhouding": OpschortingBijhouding.from_dict(obj["opschortingBijhouding"]) if obj.get("opschortingBijhouding") is not None else None,
            "geheimhoudingPersoonsgegevens": obj.get("geheimhoudingPersoonsgegevens")
        })
        return _obj


