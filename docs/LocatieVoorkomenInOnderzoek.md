# LocatieVoorkomenInOnderzoek


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datum_ingang_onderzoek** | [**AbstractDatum**](AbstractDatum.md) |  | [optional] 
**type** | **bool** |  | [optional] 
**gemeente_van_inschrijving** | **bool** |  | [optional] 
**datum_van** | **bool** |  | [optional] 
**datum_tot** | **bool** |  | [optional] 
**functie_adres** | **bool** |  | [optional] 

## Example

```python
from brp_historie_client.models.locatie_voorkomen_in_onderzoek import LocatieVoorkomenInOnderzoek

# TODO update the JSON string below
json = "{}"
# create an instance of LocatieVoorkomenInOnderzoek from a JSON string
locatie_voorkomen_in_onderzoek_instance = LocatieVoorkomenInOnderzoek.from_json(json)
# print the JSON string representation of the object
print(LocatieVoorkomenInOnderzoek.to_json())

# convert the object into a dict
locatie_voorkomen_in_onderzoek_dict = locatie_voorkomen_in_onderzoek_instance.to_dict()
# create an instance of LocatieVoorkomenInOnderzoek from a dict
locatie_voorkomen_in_onderzoek_from_dict = LocatieVoorkomenInOnderzoek.from_dict(locatie_voorkomen_in_onderzoek_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


