# AdresVoorkomenInOnderzoek


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datum_ingang_onderzoek** | [**AbstractDatum**](AbstractDatum.md) |  | [optional] 
**type** | **bool** |  | [optional] 
**gemeente_van_inschrijving** | **bool** |  | [optional] 
**datum_van** | **bool** |  | [optional] 
**datum_tot** | **bool** |  | [optional] 
**nummeraanduiding_identificatie** | **bool** |  | [optional] 
**adresseerbaar_object_identificatie** | **bool** |  | [optional] 
**functie_adres** | **bool** |  | [optional] 

## Example

```python
from brp_historie_client.models.adres_voorkomen_in_onderzoek import AdresVoorkomenInOnderzoek

# TODO update the JSON string below
json = "{}"
# create an instance of AdresVoorkomenInOnderzoek from a JSON string
adres_voorkomen_in_onderzoek_instance = AdresVoorkomenInOnderzoek.from_json(json)
# print the JSON string representation of the object
print(AdresVoorkomenInOnderzoek.to_json())

# convert the object into a dict
adres_voorkomen_in_onderzoek_dict = adres_voorkomen_in_onderzoek_instance.to_dict()
# create an instance of AdresVoorkomenInOnderzoek from a dict
adres_voorkomen_in_onderzoek_from_dict = AdresVoorkomenInOnderzoek.from_dict(adres_voorkomen_in_onderzoek_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


