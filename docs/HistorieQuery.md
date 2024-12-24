# HistorieQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**burgerservicenummer** | **str** |  | 

## Example

```python
from brp_historie_client.models.historie_query import HistorieQuery

# TODO update the JSON string below
json = "{}"
# create an instance of HistorieQuery from a JSON string
historie_query_instance = HistorieQuery.from_json(json)
# print the JSON string representation of the object
print(HistorieQuery.to_json())

# convert the object into a dict
historie_query_dict = historie_query_instance.to_dict()
# create an instance of HistorieQuery from a dict
historie_query_from_dict = HistorieQuery.from_dict(historie_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


