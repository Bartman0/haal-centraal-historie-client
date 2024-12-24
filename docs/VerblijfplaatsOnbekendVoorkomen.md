# VerblijfplaatsOnbekendVoorkomen


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datum_van** | [**AbstractDatum**](AbstractDatum.md) |  | [optional] 
**datum_tot** | [**AbstractDatum**](AbstractDatum.md) |  | [optional] 
**gemeente_van_inschrijving** | [**Waardetabel**](Waardetabel.md) |  | [optional] 
**in_onderzoek** | [**VerblijfplaatsOnbekendVoorkomenInOnderzoek**](VerblijfplaatsOnbekendVoorkomenInOnderzoek.md) |  | [optional] 
**rni** | [**RniDeelnemer**](RniDeelnemer.md) |  | [optional] 

## Example

```python
from brp_historie_client.models.verblijfplaats_onbekend_voorkomen import VerblijfplaatsOnbekendVoorkomen

# TODO update the JSON string below
json = "{}"
# create an instance of VerblijfplaatsOnbekendVoorkomen from a JSON string
verblijfplaats_onbekend_voorkomen_instance = VerblijfplaatsOnbekendVoorkomen.from_json(json)
# print the JSON string representation of the object
print(VerblijfplaatsOnbekendVoorkomen.to_json())

# convert the object into a dict
verblijfplaats_onbekend_voorkomen_dict = verblijfplaats_onbekend_voorkomen_instance.to_dict()
# create an instance of VerblijfplaatsOnbekendVoorkomen from a dict
verblijfplaats_onbekend_voorkomen_from_dict = VerblijfplaatsOnbekendVoorkomen.from_dict(verblijfplaats_onbekend_voorkomen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


