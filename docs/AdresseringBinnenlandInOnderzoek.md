# AdresseringBinnenlandInOnderzoek


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datum_ingang_onderzoek** | [**AbstractDatum**](AbstractDatum.md) |  | [optional] 
**adresregel1** | **bool** |  | [optional] 
**adresregel2** | **bool** |  | [optional] 

## Example

```python
from brp_historie_client.models.adressering_binnenland_in_onderzoek import AdresseringBinnenlandInOnderzoek

# TODO update the JSON string below
json = "{}"
# create an instance of AdresseringBinnenlandInOnderzoek from a JSON string
adressering_binnenland_in_onderzoek_instance = AdresseringBinnenlandInOnderzoek.from_json(json)
# print the JSON string representation of the object
print(AdresseringBinnenlandInOnderzoek.to_json())

# convert the object into a dict
adressering_binnenland_in_onderzoek_dict = adressering_binnenland_in_onderzoek_instance.to_dict()
# create an instance of AdresseringBinnenlandInOnderzoek from a dict
adressering_binnenland_in_onderzoek_from_dict = AdresseringBinnenlandInOnderzoek.from_dict(adressering_binnenland_in_onderzoek_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


