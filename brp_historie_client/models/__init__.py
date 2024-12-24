# coding: utf-8

# flake8: noqa
"""
    BRP historie bevragen

    API voor het zoeken en raadplegen van historische verblijfplaatsen, partners, nationaliteiten en verblijfstitels uit de BRP (inclusief de RNI).  Zie de [Functionele documentatie](https://github.com/VNG-Realisatie/Haal-Centraal-BRP-historie-bevragen/tree/v1.0.0/features) voor nadere toelichting. 

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from brp_historie_client.models.abstract_datum import AbstractDatum
from brp_historie_client.models.abstract_verblijfplaats_voorkomen import AbstractVerblijfplaatsVoorkomen
from brp_historie_client.models.adres_voorkomen import AdresVoorkomen
from brp_historie_client.models.adres_voorkomen_in_onderzoek import AdresVoorkomenInOnderzoek
from brp_historie_client.models.adressering_binnenland import AdresseringBinnenland
from brp_historie_client.models.adressering_binnenland_in_onderzoek import AdresseringBinnenlandInOnderzoek
from brp_historie_client.models.adressering_buitenland import AdresseringBuitenland
from brp_historie_client.models.adressering_buitenland_in_onderzoek import AdresseringBuitenlandInOnderzoek
from brp_historie_client.models.bad_request_foutbericht import BadRequestFoutbericht
from brp_historie_client.models.datum_onbekend import DatumOnbekend
from brp_historie_client.models.foutbericht import Foutbericht
from brp_historie_client.models.historie_query import HistorieQuery
from brp_historie_client.models.in_onderzoek import InOnderzoek
from brp_historie_client.models.invalid_params import InvalidParams
from brp_historie_client.models.jaar_datum import JaarDatum
from brp_historie_client.models.jaar_maand_datum import JaarMaandDatum
from brp_historie_client.models.locatie_voorkomen import LocatieVoorkomen
from brp_historie_client.models.locatie_voorkomen_in_onderzoek import LocatieVoorkomenInOnderzoek
from brp_historie_client.models.opschorting_bijhouding import OpschortingBijhouding
from brp_historie_client.models.opschorting_bijhouding_basis import OpschortingBijhoudingBasis
from brp_historie_client.models.raadpleeg_met_peildatum import RaadpleegMetPeildatum
from brp_historie_client.models.raadpleeg_met_periode import RaadpleegMetPeriode
from brp_historie_client.models.rni_deelnemer import RniDeelnemer
from brp_historie_client.models.verblijfadres_binnenland import VerblijfadresBinnenland
from brp_historie_client.models.verblijfadres_binnenland_in_onderzoek import VerblijfadresBinnenlandInOnderzoek
from brp_historie_client.models.verblijfadres_buitenland import VerblijfadresBuitenland
from brp_historie_client.models.verblijfadres_buitenland_in_onderzoek import VerblijfadresBuitenlandInOnderzoek
from brp_historie_client.models.verblijfadres_locatie import VerblijfadresLocatie
from brp_historie_client.models.verblijfadres_locatie_in_onderzoek import VerblijfadresLocatieInOnderzoek
from brp_historie_client.models.verblijfplaats_buitenland_voorkomen import VerblijfplaatsBuitenlandVoorkomen
from brp_historie_client.models.verblijfplaats_buitenland_voorkomen_in_onderzoek import VerblijfplaatsBuitenlandVoorkomenInOnderzoek
from brp_historie_client.models.verblijfplaats_onbekend_voorkomen import VerblijfplaatsOnbekendVoorkomen
from brp_historie_client.models.verblijfplaats_onbekend_voorkomen_in_onderzoek import VerblijfplaatsOnbekendVoorkomenInOnderzoek
from brp_historie_client.models.verblijfplaatshistorie_query_response import VerblijfplaatshistorieQueryResponse
from brp_historie_client.models.volledige_datum import VolledigeDatum
from brp_historie_client.models.waardetabel import Waardetabel
