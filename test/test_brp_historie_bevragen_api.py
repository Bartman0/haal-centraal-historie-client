# coding: utf-8

"""
    BRP historie bevragen

    API voor het zoeken en raadplegen van historische verblijfplaatsen, partners, nationaliteiten en verblijfstitels uit de BRP (inclusief de RNI).  Zie de [Functionele documentatie](https://github.com/VNG-Realisatie/Haal-Centraal-BRP-historie-bevragen/tree/v1.0.0/features) voor nadere toelichting. 

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from brp_historie_client.api.brp_historie_bevragen_api import BRPHistorieBevragenApi


class TestBRPHistorieBevragenApi(unittest.TestCase):
    """BRPHistorieBevragenApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BRPHistorieBevragenApi()

    def tearDown(self) -> None:
        pass

    def test_verblijfplaatshistorie(self) -> None:
        """Test case for verblijfplaatshistorie

        """
        pass


if __name__ == '__main__':
    unittest.main()