# VerblijfadresLocatie


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locatiebeschrijving** | **str** | Omschrijving van de ligging van een verblijfsobject, standplaats of ligplaats.  | [optional] 
**in_onderzoek** | [**VerblijfadresLocatieInOnderzoek**](VerblijfadresLocatieInOnderzoek.md) |  | [optional] 

## Example

```python
from brp_historie_client.models.verblijfadres_locatie import VerblijfadresLocatie

# TODO update the JSON string below
json = "{}"
# create an instance of VerblijfadresLocatie from a JSON string
verblijfadres_locatie_instance = VerblijfadresLocatie.from_json(json)
# print the JSON string representation of the object
print(VerblijfadresLocatie.to_json())

# convert the object into a dict
verblijfadres_locatie_dict = verblijfadres_locatie_instance.to_dict()
# create an instance of VerblijfadresLocatie from a dict
verblijfadres_locatie_from_dict = VerblijfadresLocatie.from_dict(verblijfadres_locatie_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


