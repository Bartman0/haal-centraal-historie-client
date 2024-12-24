# AdresseringBuitenlandInOnderzoek


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datum_ingang_onderzoek** | [**AbstractDatum**](AbstractDatum.md) |  | [optional] 
**adresregel1** | **bool** |  | [optional] 
**adresregel2** | **bool** |  | [optional] 
**adresregel3** | **bool** |  | [optional] 
**land** | **bool** |  | [optional] 

## Example

```python
from brp_historie_client.models.adressering_buitenland_in_onderzoek import AdresseringBuitenlandInOnderzoek

# TODO update the JSON string below
json = "{}"
# create an instance of AdresseringBuitenlandInOnderzoek from a JSON string
adressering_buitenland_in_onderzoek_instance = AdresseringBuitenlandInOnderzoek.from_json(json)
# print the JSON string representation of the object
print(AdresseringBuitenlandInOnderzoek.to_json())

# convert the object into a dict
adressering_buitenland_in_onderzoek_dict = adressering_buitenland_in_onderzoek_instance.to_dict()
# create an instance of AdresseringBuitenlandInOnderzoek from a dict
adressering_buitenland_in_onderzoek_from_dict = AdresseringBuitenlandInOnderzoek.from_dict(adressering_buitenland_in_onderzoek_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


