# OpschortingBijhouding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reden** | [**Waardetabel**](Waardetabel.md) |  | [optional] 
**datum** | [**AbstractDatum**](AbstractDatum.md) |  | [optional] 

## Example

```python
from brp_historie_client.models.opschorting_bijhouding import OpschortingBijhouding

# TODO update the JSON string below
json = "{}"
# create an instance of OpschortingBijhouding from a JSON string
opschorting_bijhouding_instance = OpschortingBijhouding.from_json(json)
# print the JSON string representation of the object
print(OpschortingBijhouding.to_json())

# convert the object into a dict
opschorting_bijhouding_dict = opschorting_bijhouding_instance.to_dict()
# create an instance of OpschortingBijhouding from a dict
opschorting_bijhouding_from_dict = OpschortingBijhouding.from_dict(opschorting_bijhouding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


