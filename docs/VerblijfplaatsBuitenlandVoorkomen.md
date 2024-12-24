# VerblijfplaatsBuitenlandVoorkomen

* **land** - land waar de persoon is overleden. Wordt gevuld met waarden uit de landelijke tabel 'Landen'. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verblijfadres** | [**VerblijfadresBuitenland**](VerblijfadresBuitenland.md) |  | [optional] 
**datum_van** | [**AbstractDatum**](AbstractDatum.md) |  | [optional] 
**datum_tot** | [**AbstractDatum**](AbstractDatum.md) |  | [optional] 
**gemeente_van_inschrijving** | [**Waardetabel**](Waardetabel.md) |  | [optional] 
**in_onderzoek** | [**VerblijfplaatsBuitenlandVoorkomenInOnderzoek**](VerblijfplaatsBuitenlandVoorkomenInOnderzoek.md) |  | [optional] 
**rni** | [**RniDeelnemer**](RniDeelnemer.md) |  | [optional] 
**adressering** | [**AdresseringBuitenland**](AdresseringBuitenland.md) |  | [optional] 

## Example

```python
from brp_historie_client.models.verblijfplaats_buitenland_voorkomen import VerblijfplaatsBuitenlandVoorkomen

# TODO update the JSON string below
json = "{}"
# create an instance of VerblijfplaatsBuitenlandVoorkomen from a JSON string
verblijfplaats_buitenland_voorkomen_instance = VerblijfplaatsBuitenlandVoorkomen.from_json(json)
# print the JSON string representation of the object
print(VerblijfplaatsBuitenlandVoorkomen.to_json())

# convert the object into a dict
verblijfplaats_buitenland_voorkomen_dict = verblijfplaats_buitenland_voorkomen_instance.to_dict()
# create an instance of VerblijfplaatsBuitenlandVoorkomen from a dict
verblijfplaats_buitenland_voorkomen_from_dict = VerblijfplaatsBuitenlandVoorkomen.from_dict(verblijfplaats_buitenland_voorkomen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


