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

from pydantic import ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from brp_historie_client.models.abstract_datum import AbstractDatum
from brp_historie_client.models.abstract_verblijfplaats_voorkomen import AbstractVerblijfplaatsVoorkomen
from brp_historie_client.models.adressering_binnenland import AdresseringBinnenland
from brp_historie_client.models.locatie_voorkomen_in_onderzoek import LocatieVoorkomenInOnderzoek
from brp_historie_client.models.verblijfadres_locatie import VerblijfadresLocatie
from brp_historie_client.models.waardetabel import Waardetabel
from typing import Optional, Set
from typing_extensions import Self

class LocatieVoorkomen(AbstractVerblijfplaatsVoorkomen):
    """
    * **functieAdres** - wordt gevuld met waarden voor 'Functie_Adres' in 'tabelwaarden.csv'. * **gemeenteVanInschrijving** - wordt gevuld met waarden uit de landelijke tabel 'Gemeenten'. * **verblijftNietOpAdresVanaf** : geeft aan op welke datum is vastgesteld dat de persoon niet langer op dit adres of deze locatie verblijft. 
    """ # noqa: E501
    datum_van: Optional[AbstractDatum] = Field(default=None, alias="datumVan")
    datum_tot: Optional[AbstractDatum] = Field(default=None, alias="datumTot")
    functie_adres: Optional[Waardetabel] = Field(default=None, alias="functieAdres")
    verblijfadres: Optional[VerblijfadresLocatie] = None
    gemeente_van_inschrijving: Optional[Waardetabel] = Field(default=None, alias="gemeenteVanInschrijving")
    verblijft_niet_op_adres_vanaf: Optional[AbstractDatum] = Field(default=None, alias="verblijftNietOpAdresVanaf")
    in_onderzoek: Optional[LocatieVoorkomenInOnderzoek] = Field(default=None, alias="inOnderzoek")
    adressering: Optional[AdresseringBinnenland] = None
    __properties: ClassVar[List[str]] = ["type", "datumVan", "datumTot", "functieAdres", "verblijfadres", "gemeenteVanInschrijving", "verblijftNietOpAdresVanaf", "inOnderzoek", "adressering"]

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
        """Create an instance of LocatieVoorkomen from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of datum_van
        if self.datum_van:
            _dict['datumVan'] = self.datum_van.to_dict()
        # override the default output from pydantic by calling `to_dict()` of datum_tot
        if self.datum_tot:
            _dict['datumTot'] = self.datum_tot.to_dict()
        # override the default output from pydantic by calling `to_dict()` of functie_adres
        if self.functie_adres:
            _dict['functieAdres'] = self.functie_adres.to_dict()
        # override the default output from pydantic by calling `to_dict()` of verblijfadres
        if self.verblijfadres:
            _dict['verblijfadres'] = self.verblijfadres.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gemeente_van_inschrijving
        if self.gemeente_van_inschrijving:
            _dict['gemeenteVanInschrijving'] = self.gemeente_van_inschrijving.to_dict()
        # override the default output from pydantic by calling `to_dict()` of verblijft_niet_op_adres_vanaf
        if self.verblijft_niet_op_adres_vanaf:
            _dict['verblijftNietOpAdresVanaf'] = self.verblijft_niet_op_adres_vanaf.to_dict()
        # override the default output from pydantic by calling `to_dict()` of in_onderzoek
        if self.in_onderzoek:
            _dict['inOnderzoek'] = self.in_onderzoek.to_dict()
        # override the default output from pydantic by calling `to_dict()` of adressering
        if self.adressering:
            _dict['adressering'] = self.adressering.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LocatieVoorkomen from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "datumVan": AbstractDatum.from_dict(obj["datumVan"]) if obj.get("datumVan") is not None else None,
            "datumTot": AbstractDatum.from_dict(obj["datumTot"]) if obj.get("datumTot") is not None else None,
            "functieAdres": Waardetabel.from_dict(obj["functieAdres"]) if obj.get("functieAdres") is not None else None,
            "verblijfadres": VerblijfadresLocatie.from_dict(obj["verblijfadres"]) if obj.get("verblijfadres") is not None else None,
            "gemeenteVanInschrijving": Waardetabel.from_dict(obj["gemeenteVanInschrijving"]) if obj.get("gemeenteVanInschrijving") is not None else None,
            "verblijftNietOpAdresVanaf": AbstractDatum.from_dict(obj["verblijftNietOpAdresVanaf"]) if obj.get("verblijftNietOpAdresVanaf") is not None else None,
            "inOnderzoek": LocatieVoorkomenInOnderzoek.from_dict(obj["inOnderzoek"]) if obj.get("inOnderzoek") is not None else None,
            "adressering": AdresseringBinnenland.from_dict(obj["adressering"]) if obj.get("adressering") is not None else None
        })
        return _obj


