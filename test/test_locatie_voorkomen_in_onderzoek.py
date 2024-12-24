# coding: utf-8

"""
    BRP historie bevragen

    API voor het zoeken en raadplegen van historische verblijfplaatsen, partners, nationaliteiten en verblijfstitels uit de BRP (inclusief de RNI).  Zie de [Functionele documentatie](https://github.com/VNG-Realisatie/Haal-Centraal-BRP-historie-bevragen/tree/v1.0.0/features) voor nadere toelichting. 

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from brp_historie_client.models.locatie_voorkomen_in_onderzoek import LocatieVoorkomenInOnderzoek

class TestLocatieVoorkomenInOnderzoek(unittest.TestCase):
    """LocatieVoorkomenInOnderzoek unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LocatieVoorkomenInOnderzoek:
        """Test LocatieVoorkomenInOnderzoek
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LocatieVoorkomenInOnderzoek`
        """
        model = LocatieVoorkomenInOnderzoek()
        if include_optional:
            return LocatieVoorkomenInOnderzoek(
                datum_ingang_onderzoek = brp_historie_client.models.abstract_datum.AbstractDatum(
                    type = '', 
                    lang_formaat = 'pr1c2v7s6dju', ),
                type = True,
                gemeente_van_inschrijving = True,
                datum_van = True,
                datum_tot = True,
                functie_adres = True
            )
        else:
            return LocatieVoorkomenInOnderzoek(
        )
        """

    def testLocatieVoorkomenInOnderzoek(self):
        """Test LocatieVoorkomenInOnderzoek"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()