# LocatieVoorkomen

* **functieAdres** - wordt gevuld met waarden voor 'Functie_Adres' in 'tabelwaarden.csv'. * **gemeenteVanInschrijving** - wordt gevuld met waarden uit de landelijke tabel 'Gemeenten'. * **verblijftNietOpAdresVanaf** : geeft aan op welke datum is vastgesteld dat de persoon niet langer op dit adres of deze locatie verblijft. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datum_van** | [**AbstractDatum**](AbstractDatum.md) |  | [optional] 
**datum_tot** | [**AbstractDatum**](AbstractDatum.md) |  | [optional] 
**functie_adres** | [**Waardetabel**](Waardetabel.md) |  | [optional] 
**verblijfadres** | [**VerblijfadresLocatie**](VerblijfadresLocatie.md) |  | [optional] 
**gemeente_van_inschrijving** | [**Waardetabel**](Waardetabel.md) |  | [optional] 
**verblijft_niet_op_adres_vanaf** | [**AbstractDatum**](AbstractDatum.md) |  | [optional] 
**in_onderzoek** | [**LocatieVoorkomenInOnderzoek**](LocatieVoorkomenInOnderzoek.md) |  | [optional] 
**adressering** | [**AdresseringBinnenland**](AdresseringBinnenland.md) |  | [optional] 

## Example

```python
from brp_historie_client.models.locatie_voorkomen import LocatieVoorkomen

# TODO update the JSON string below
json = "{}"
# create an instance of LocatieVoorkomen from a JSON string
locatie_voorkomen_instance = LocatieVoorkomen.from_json(json)
# print the JSON string representation of the object
print(LocatieVoorkomen.to_json())

# convert the object into a dict
locatie_voorkomen_dict = locatie_voorkomen_instance.to_dict()
# create an instance of LocatieVoorkomen from a dict
locatie_voorkomen_from_dict = LocatieVoorkomen.from_dict(locatie_voorkomen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


