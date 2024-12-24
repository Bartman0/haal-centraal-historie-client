# RaadpleegMetPeildatum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**peildatum** | **date** | De datum waarop de resource wordt opgevraagd.  | 

## Example

```python
from brp_historie_client.models.raadpleeg_met_peildatum import RaadpleegMetPeildatum

# TODO update the JSON string below
json = "{}"
# create an instance of RaadpleegMetPeildatum from a JSON string
raadpleeg_met_peildatum_instance = RaadpleegMetPeildatum.from_json(json)
# print the JSON string representation of the object
print(RaadpleegMetPeildatum.to_json())

# convert the object into a dict
raadpleeg_met_peildatum_dict = raadpleeg_met_peildatum_instance.to_dict()
# create an instance of RaadpleegMetPeildatum from a dict
raadpleeg_met_peildatum_from_dict = RaadpleegMetPeildatum.from_dict(raadpleeg_met_peildatum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


