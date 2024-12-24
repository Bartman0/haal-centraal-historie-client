# RniDeelnemer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deelnemer** | [**Waardetabel**](Waardetabel.md) |  | [optional] 
**omschrijving_verdrag** | **str** | Omschrijving van het verdrag op basis waarvan een zusterorganisatie in het buitenland de gegevens bij de RNI-deelnemer heeft aangeleverd.  | [optional] 

## Example

```python
from brp_historie_client.models.rni_deelnemer import RniDeelnemer

# TODO update the JSON string below
json = "{}"
# create an instance of RniDeelnemer from a JSON string
rni_deelnemer_instance = RniDeelnemer.from_json(json)
# print the JSON string representation of the object
print(RniDeelnemer.to_json())

# convert the object into a dict
rni_deelnemer_dict = rni_deelnemer_instance.to_dict()
# create an instance of RniDeelnemer from a dict
rni_deelnemer_from_dict = RniDeelnemer.from_dict(rni_deelnemer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


