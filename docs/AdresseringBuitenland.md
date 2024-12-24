# AdresseringBuitenland


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adresregel1** | **str** | Het eerste deel van een adres is een combinatie van de straat en huisnummer.  | [optional] 
**adresregel2** | **str** | Het tweede deel van een adres is een combinatie van woonplaats eventueel in combinatie met de postcode.  | [optional] 
**adresregel3** | **str** | Het derde deel van een adres is optioneel. Het gaat om een of meer geografische gebieden van het adres in het buitenland.  | [optional] 
**land** | [**Waardetabel**](Waardetabel.md) |  | [optional] 
**in_onderzoek** | [**AdresseringBuitenlandInOnderzoek**](AdresseringBuitenlandInOnderzoek.md) |  | [optional] 

## Example

```python
from brp_historie_client.models.adressering_buitenland import AdresseringBuitenland

# TODO update the JSON string below
json = "{}"
# create an instance of AdresseringBuitenland from a JSON string
adressering_buitenland_instance = AdresseringBuitenland.from_json(json)
# print the JSON string representation of the object
print(AdresseringBuitenland.to_json())

# convert the object into a dict
adressering_buitenland_dict = adressering_buitenland_instance.to_dict()
# create an instance of AdresseringBuitenland from a dict
adressering_buitenland_from_dict = AdresseringBuitenland.from_dict(adressering_buitenland_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


