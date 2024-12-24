# OpschortingBijhoudingBasis

* **reden** - wordt gevuld met waarden voor 'Reden_Opschorting_Bijhouding' in 'tabelwaarden.csv'. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reden** | [**Waardetabel**](Waardetabel.md) |  | [optional] 

## Example

```python
from brp_historie_client.models.opschorting_bijhouding_basis import OpschortingBijhoudingBasis

# TODO update the JSON string below
json = "{}"
# create an instance of OpschortingBijhoudingBasis from a JSON string
opschorting_bijhouding_basis_instance = OpschortingBijhoudingBasis.from_json(json)
# print the JSON string representation of the object
print(OpschortingBijhoudingBasis.to_json())

# convert the object into a dict
opschorting_bijhouding_basis_dict = opschorting_bijhouding_basis_instance.to_dict()
# create an instance of OpschortingBijhoudingBasis from a dict
opschorting_bijhouding_basis_from_dict = OpschortingBijhoudingBasis.from_dict(opschorting_bijhouding_basis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


