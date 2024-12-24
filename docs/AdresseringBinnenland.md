# AdresseringBinnenland


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adresregel1** | **str** | Het eerste deel van een adres is een combinatie van de straat en huisnummer.  | [optional] 
**adresregel2** | **str** | Het tweede deel van een adres is een combinatie van woonplaats eventueel in combinatie met de postcode.  | [optional] 
**in_onderzoek** | [**AdresseringBinnenlandInOnderzoek**](AdresseringBinnenlandInOnderzoek.md) |  | [optional] 

## Example

```python
from brp_historie_client.models.adressering_binnenland import AdresseringBinnenland

# TODO update the JSON string below
json = "{}"
# create an instance of AdresseringBinnenland from a JSON string
adressering_binnenland_instance = AdresseringBinnenland.from_json(json)
# print the JSON string representation of the object
print(AdresseringBinnenland.to_json())

# convert the object into a dict
adressering_binnenland_dict = adressering_binnenland_instance.to_dict()
# create an instance of AdresseringBinnenland from a dict
adressering_binnenland_from_dict = AdresseringBinnenland.from_dict(adressering_binnenland_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


