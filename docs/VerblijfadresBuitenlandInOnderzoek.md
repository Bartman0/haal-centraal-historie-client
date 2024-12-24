# VerblijfadresBuitenlandInOnderzoek


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datum_ingang_onderzoek** | [**AbstractDatum**](AbstractDatum.md) |  | [optional] 
**regel1** | **bool** |  | [optional] 
**regel2** | **bool** |  | [optional] 
**regel3** | **bool** |  | [optional] 
**land** | **bool** |  | [optional] 

## Example

```python
from brp_historie_client.models.verblijfadres_buitenland_in_onderzoek import VerblijfadresBuitenlandInOnderzoek

# TODO update the JSON string below
json = "{}"
# create an instance of VerblijfadresBuitenlandInOnderzoek from a JSON string
verblijfadres_buitenland_in_onderzoek_instance = VerblijfadresBuitenlandInOnderzoek.from_json(json)
# print the JSON string representation of the object
print(VerblijfadresBuitenlandInOnderzoek.to_json())

# convert the object into a dict
verblijfadres_buitenland_in_onderzoek_dict = verblijfadres_buitenland_in_onderzoek_instance.to_dict()
# create an instance of VerblijfadresBuitenlandInOnderzoek from a dict
verblijfadres_buitenland_in_onderzoek_from_dict = VerblijfadresBuitenlandInOnderzoek.from_dict(verblijfadres_buitenland_in_onderzoek_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


