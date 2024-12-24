# InvalidParams

Details over fouten in opgegeven parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**name** | **str** | Naam van de parameter | [optional] 
**code** | **str** | Systeemcode die het type fout aangeeft | [optional] 
**reason** | **str** | Beschrijving van de fout op de parameterwaarde | [optional] 

## Example

```python
from brp_historie_client.models.invalid_params import InvalidParams

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidParams from a JSON string
invalid_params_instance = InvalidParams.from_json(json)
# print the JSON string representation of the object
print(InvalidParams.to_json())

# convert the object into a dict
invalid_params_dict = invalid_params_instance.to_dict()
# create an instance of InvalidParams from a dict
invalid_params_from_dict = InvalidParams.from_dict(invalid_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


