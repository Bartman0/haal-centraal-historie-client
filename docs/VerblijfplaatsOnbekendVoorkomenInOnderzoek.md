# VerblijfplaatsOnbekendVoorkomenInOnderzoek


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datum_ingang_onderzoek** | [**AbstractDatum**](AbstractDatum.md) |  | [optional] 
**type** | **bool** |  | [optional] 
**datum_van** | **bool** |  | [optional] 
**datum_tot** | **bool** |  | [optional] 
**gemeente_van_inschrijving** | **bool** |  | [optional] 

## Example

```python
from brp_historie_client.models.verblijfplaats_onbekend_voorkomen_in_onderzoek import VerblijfplaatsOnbekendVoorkomenInOnderzoek

# TODO update the JSON string below
json = "{}"
# create an instance of VerblijfplaatsOnbekendVoorkomenInOnderzoek from a JSON string
verblijfplaats_onbekend_voorkomen_in_onderzoek_instance = VerblijfplaatsOnbekendVoorkomenInOnderzoek.from_json(json)
# print the JSON string representation of the object
print(VerblijfplaatsOnbekendVoorkomenInOnderzoek.to_json())

# convert the object into a dict
verblijfplaats_onbekend_voorkomen_in_onderzoek_dict = verblijfplaats_onbekend_voorkomen_in_onderzoek_instance.to_dict()
# create an instance of VerblijfplaatsOnbekendVoorkomenInOnderzoek from a dict
verblijfplaats_onbekend_voorkomen_in_onderzoek_from_dict = VerblijfplaatsOnbekendVoorkomenInOnderzoek.from_dict(verblijfplaats_onbekend_voorkomen_in_onderzoek_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


