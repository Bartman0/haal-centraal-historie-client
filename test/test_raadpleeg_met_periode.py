# coding: utf-8

"""
    BRP historie bevragen

    API voor het zoeken en raadplegen van historische verblijfplaatsen, partners, nationaliteiten en verblijfstitels uit de BRP (inclusief de RNI).  Zie de [Functionele documentatie](https://github.com/VNG-Realisatie/Haal-Centraal-BRP-historie-bevragen/tree/v1.0.0/features) voor nadere toelichting. 

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from brp_historie_client.models.raadpleeg_met_periode import RaadpleegMetPeriode

class TestRaadpleegMetPeriode(unittest.TestCase):
    """RaadpleegMetPeriode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RaadpleegMetPeriode:
        """Test RaadpleegMetPeriode
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RaadpleegMetPeriode`
        """
        model = RaadpleegMetPeriode()
        if include_optional:
            return RaadpleegMetPeriode(
                datum_van = 'Thu Sep 24 01:00:00 CET 1964',
                datum_tot = 'Thu Sep 24 01:00:00 CET 1964'
            )
        else:
            return RaadpleegMetPeriode(
                datum_van = 'Thu Sep 24 01:00:00 CET 1964',
                datum_tot = 'Thu Sep 24 01:00:00 CET 1964',
        )
        """

    def testRaadpleegMetPeriode(self):
        """Test RaadpleegMetPeriode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
