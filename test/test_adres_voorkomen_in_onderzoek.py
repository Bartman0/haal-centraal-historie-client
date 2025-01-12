# coding: utf-8

"""
    BRP historie bevragen

    API voor het zoeken en raadplegen van historische verblijfplaatsen, partners, nationaliteiten en verblijfstitels uit de BRP (inclusief de RNI).  Zie de [Functionele documentatie](https://github.com/VNG-Realisatie/Haal-Centraal-BRP-historie-bevragen/tree/v1.0.0/features) voor nadere toelichting. 

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from brp_historie_client.models.adres_voorkomen_in_onderzoek import AdresVoorkomenInOnderzoek

class TestAdresVoorkomenInOnderzoek(unittest.TestCase):
    """AdresVoorkomenInOnderzoek unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdresVoorkomenInOnderzoek:
        """Test AdresVoorkomenInOnderzoek
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdresVoorkomenInOnderzoek`
        """
        model = AdresVoorkomenInOnderzoek()
        if include_optional:
            return AdresVoorkomenInOnderzoek(
                datum_ingang_onderzoek = brp_historie_client.models.abstract_datum.AbstractDatum(
                    type = '', 
                    lang_formaat = 'pr1c2v7s6dju', ),
                type = True,
                gemeente_van_inschrijving = True,
                datum_van = True,
                datum_tot = True,
                nummeraanduiding_identificatie = True,
                adresseerbaar_object_identificatie = True,
                functie_adres = True
            )
        else:
            return AdresVoorkomenInOnderzoek(
        )
        """

    def testAdresVoorkomenInOnderzoek(self):
        """Test AdresVoorkomenInOnderzoek"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
