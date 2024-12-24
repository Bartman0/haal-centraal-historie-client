# RaadpleegMetPeriode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datum_van** | **date** | De begindatum van de periode waarover de resource wordt opgevraagd.  | 
**datum_tot** | **date** | De einddatum van de periode waarover de resource wordt opgevraagd.  | 

## Example

```python
from brp_historie_client.models.raadpleeg_met_periode import RaadpleegMetPeriode

# TODO update the JSON string below
json = "{}"
# create an instance of RaadpleegMetPeriode from a JSON string
raadpleeg_met_periode_instance = RaadpleegMetPeriode.from_json(json)
# print the JSON string representation of the object
print(RaadpleegMetPeriode.to_json())

# convert the object into a dict
raadpleeg_met_periode_dict = raadpleeg_met_periode_instance.to_dict()
# create an instance of RaadpleegMetPeriode from a dict
raadpleeg_met_periode_from_dict = RaadpleegMetPeriode.from_dict(raadpleeg_met_periode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


