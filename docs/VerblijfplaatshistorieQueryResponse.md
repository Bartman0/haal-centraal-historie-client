# VerblijfplaatshistorieQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verblijfplaatsen** | [**List[AbstractVerblijfplaatsVoorkomen]**](AbstractVerblijfplaatsVoorkomen.md) |  | [optional] 
**opschorting_bijhouding** | [**OpschortingBijhouding**](OpschortingBijhouding.md) |  | [optional] 
**geheimhouding_persoonsgegevens** | **bool** | Gegevens mogen niet worden verstrekt aan derden / maatschappelijke instellingen.  | [optional] 

## Example

```python
from brp_historie_client.models.verblijfplaatshistorie_query_response import VerblijfplaatshistorieQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerblijfplaatshistorieQueryResponse from a JSON string
verblijfplaatshistorie_query_response_instance = VerblijfplaatshistorieQueryResponse.from_json(json)
# print the JSON string representation of the object
print(VerblijfplaatshistorieQueryResponse.to_json())

# convert the object into a dict
verblijfplaatshistorie_query_response_dict = verblijfplaatshistorie_query_response_instance.to_dict()
# create an instance of VerblijfplaatshistorieQueryResponse from a dict
verblijfplaatshistorie_query_response_from_dict = VerblijfplaatshistorieQueryResponse.from_dict(verblijfplaatshistorie_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


