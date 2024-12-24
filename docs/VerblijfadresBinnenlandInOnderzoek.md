# VerblijfadresBinnenlandInOnderzoek


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datum_ingang_onderzoek** | [**AbstractDatum**](AbstractDatum.md) |  | [optional] 
**aanduiding_bij_huisnummer** | **bool** |  | [optional] 
**huisletter** | **bool** |  | [optional] 
**huisnummer** | **bool** |  | [optional] 
**huisnummertoevoeging** | **bool** |  | [optional] 
**officiele_straatnaam** | **bool** |  | [optional] 
**postcode** | **bool** |  | [optional] 
**korte_straatnaam** | **bool** |  | [optional] 
**woonplaats** | **bool** |  | [optional] 

## Example

```python
from brp_historie_client.models.verblijfadres_binnenland_in_onderzoek import VerblijfadresBinnenlandInOnderzoek

# TODO update the JSON string below
json = "{}"
# create an instance of VerblijfadresBinnenlandInOnderzoek from a JSON string
verblijfadres_binnenland_in_onderzoek_instance = VerblijfadresBinnenlandInOnderzoek.from_json(json)
# print the JSON string representation of the object
print(VerblijfadresBinnenlandInOnderzoek.to_json())

# convert the object into a dict
verblijfadres_binnenland_in_onderzoek_dict = verblijfadres_binnenland_in_onderzoek_instance.to_dict()
# create an instance of VerblijfadresBinnenlandInOnderzoek from a dict
verblijfadres_binnenland_in_onderzoek_from_dict = VerblijfadresBinnenlandInOnderzoek.from_dict(verblijfadres_binnenland_in_onderzoek_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


