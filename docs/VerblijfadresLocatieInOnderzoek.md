# VerblijfadresLocatieInOnderzoek


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datum_ingang_onderzoek** | [**AbstractDatum**](AbstractDatum.md) |  | [optional] 
**locatiebeschrijving** | **bool** |  | [optional] 

## Example

```python
from brp_historie_client.models.verblijfadres_locatie_in_onderzoek import VerblijfadresLocatieInOnderzoek

# TODO update the JSON string below
json = "{}"
# create an instance of VerblijfadresLocatieInOnderzoek from a JSON string
verblijfadres_locatie_in_onderzoek_instance = VerblijfadresLocatieInOnderzoek.from_json(json)
# print the JSON string representation of the object
print(VerblijfadresLocatieInOnderzoek.to_json())

# convert the object into a dict
verblijfadres_locatie_in_onderzoek_dict = verblijfadres_locatie_in_onderzoek_instance.to_dict()
# create an instance of VerblijfadresLocatieInOnderzoek from a dict
verblijfadres_locatie_in_onderzoek_from_dict = VerblijfadresLocatieInOnderzoek.from_dict(verblijfadres_locatie_in_onderzoek_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


