# AdresVoorkomen

Gegevens over het adres voorkomen van een persoon. * **gemeenteVanInschrijving** - wordt gevuld met waarden uit de landelijke tabel 'Gemeenten'. * **functieAdres** - wordt gevuld met waarden voor 'Functie_Adres' in 'tabelwaarden.csv'. * **aanduidingBijHuisnummer** - wordt gevuld met waarden voor 'Aanduiding_Bij_Huisnummer' in 'tabelwaarden.csv'. * **datumVan** : de datum van aangifte of ambtshalve melding van verblijf en adres. * **datumTot** : de datum van aangifte of ambtshalve melding van volgende verblijf en adres. * **verblijftNietOpAdresVanaf** : geeft aan op welke datum is vastgesteld dat de persoon niet langer op dit adres of deze locatie woont. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verblijfadres** | [**VerblijfadresBinnenland**](VerblijfadresBinnenland.md) |  | [optional] 
**functie_adres** | [**Waardetabel**](Waardetabel.md) |  | [optional] 
**adresseerbaar_object_identificatie** | **str** | De verblijfplaats van de persoon kan een ligplaats, een standplaats of een verblijfsobject zijn.  | [optional] 
**nummeraanduiding_identificatie** | **str** | Unieke identificatie van een nummeraanduiding (en het bijbehorende adres) in de BAG.  | [optional] 
**gemeente_van_inschrijving** | [**Waardetabel**](Waardetabel.md) |  | [optional] 
**datum_van** | [**AbstractDatum**](AbstractDatum.md) |  | [optional] 
**datum_tot** | [**AbstractDatum**](AbstractDatum.md) |  | [optional] 
**verblijft_niet_op_adres_vanaf** | [**AbstractDatum**](AbstractDatum.md) |  | [optional] 
**in_onderzoek** | [**AdresVoorkomenInOnderzoek**](AdresVoorkomenInOnderzoek.md) |  | [optional] 
**adressering** | [**AdresseringBinnenland**](AdresseringBinnenland.md) |  | [optional] 

## Example

```python
from brp_historie_client.models.adres_voorkomen import AdresVoorkomen

# TODO update the JSON string below
json = "{}"
# create an instance of AdresVoorkomen from a JSON string
adres_voorkomen_instance = AdresVoorkomen.from_json(json)
# print the JSON string representation of the object
print(AdresVoorkomen.to_json())

# convert the object into a dict
adres_voorkomen_dict = adres_voorkomen_instance.to_dict()
# create an instance of AdresVoorkomen from a dict
adres_voorkomen_from_dict = AdresVoorkomen.from_dict(adres_voorkomen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


