# coding: utf-8

"""
    BRP historie bevragen

    API voor het zoeken en raadplegen van historische verblijfplaatsen, partners, nationaliteiten en verblijfstitels uit de BRP (inclusief de RNI).  Zie de [Functionele documentatie](https://github.com/VNG-Realisatie/Haal-Centraal-BRP-historie-bevragen/tree/v1.0.0/features) voor nadere toelichting. 

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from brp_historie_client.models.invalid_params import InvalidParams

class TestInvalidParams(unittest.TestCase):
    """InvalidParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvalidParams:
        """Test InvalidParams
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvalidParams`
        """
        model = InvalidParams()
        if include_optional:
            return InvalidParams(
                type = 'https://www.vng.nl/realisatie/api/{major-versie}/validaties/integer',
                name = 'huisnummer',
                code = 'integer',
                reason = 'Waarde is geen geldig getal.'
            )
        else:
            return InvalidParams(
        )
        """

    def testInvalidParams(self):
        """Test InvalidParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
