# Waardetabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**omschrijving** | **str** |  | [optional] 

## Example

```python
from brp_historie_client.models.waardetabel import Waardetabel

# TODO update the JSON string below
json = "{}"
# create an instance of Waardetabel from a JSON string
waardetabel_instance = Waardetabel.from_json(json)
# print the JSON string representation of the object
print(Waardetabel.to_json())

# convert the object into a dict
waardetabel_dict = waardetabel_instance.to_dict()
# create an instance of Waardetabel from a dict
waardetabel_from_dict = Waardetabel.from_dict(waardetabel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


