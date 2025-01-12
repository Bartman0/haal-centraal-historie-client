# coding: utf-8

"""
    BRP historie bevragen

    API voor het zoeken en raadplegen van historische verblijfplaatsen, partners, nationaliteiten en verblijfstitels uit de BRP (inclusief de RNI).  Zie de [Functionele documentatie](https://github.com/VNG-Realisatie/Haal-Centraal-BRP-historie-bevragen/tree/v1.0.0/features) voor nadere toelichting. 

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from brp_historie_client.models.verblijfplaats_buitenland_voorkomen import VerblijfplaatsBuitenlandVoorkomen

class TestVerblijfplaatsBuitenlandVoorkomen(unittest.TestCase):
    """VerblijfplaatsBuitenlandVoorkomen unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VerblijfplaatsBuitenlandVoorkomen:
        """Test VerblijfplaatsBuitenlandVoorkomen
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VerblijfplaatsBuitenlandVoorkomen`
        """
        model = VerblijfplaatsBuitenlandVoorkomen()
        if include_optional:
            return VerblijfplaatsBuitenlandVoorkomen(
                verblijfadres = brp_historie_client.models.verblijfadres_buitenland.VerblijfadresBuitenland(
                    regel1 = '1600 Pennsylvania Avenue NW', 
                    regel2 = 'Washington, DC 20500', 
                    regel3 = 'Selangor', 
                    land = brp_historie_client.models.waardetabel.Waardetabel(
                        code = '6030', 
                        omschrijving = 'Nederland', ), 
                    in_onderzoek = null, ),
                datum_van = brp_historie_client.models.abstract_datum.AbstractDatum(
                    type = '', 
                    lang_formaat = 'pr1c2v7s6dju', ),
                datum_tot = brp_historie_client.models.abstract_datum.AbstractDatum(
                    type = '', 
                    lang_formaat = 'pr1c2v7s6dju', ),
                gemeente_van_inschrijving = brp_historie_client.models.waardetabel.Waardetabel(
                    code = '6030', 
                    omschrijving = 'Nederland', ),
                in_onderzoek = None,
                rni = brp_historie_client.models.rni_deelnemer.RniDeelnemer(
                    deelnemer = brp_historie_client.models.waardetabel.Waardetabel(
                        code = '6030', 
                        omschrijving = 'Nederland', ), 
                    omschrijving_verdrag = 'D', ),
                adressering = brp_historie_client.models.adressering_buitenland.AdresseringBuitenland(
                    adresregel1 = 'Kappeyne v d Cappellostr 26A-3', 
                    adresregel2 = '1234AA Nootdorp', 
                    adresregel3 = 'Selangor', 
                    land = brp_historie_client.models.waardetabel.Waardetabel(
                        code = '6030', 
                        omschrijving = 'Nederland', ), 
                    in_onderzoek = null, )
            )
        else:
            return VerblijfplaatsBuitenlandVoorkomen(
        )
        """

    def testVerblijfplaatsBuitenlandVoorkomen(self):
        """Test VerblijfplaatsBuitenlandVoorkomen"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
