# VerblijfadresBinnenland


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**officiele_straatnaam** | **str** | De officiële naam van een openbare ruimte uit de Basisregistratie Gebouwen en Adressen (BAG).  | [optional] 
**korte_straatnaam** | **str** | De officiële naam van een openbare ruimte uit de Basisregistratie Gebouwen en Adressen (BAG), zo nodig verkort tot maximaal 24 tekens, of de straatnaam van een niet-BAG adres.  | [optional] 
**huisnummer** | **int** | Een nummer dat door de gemeente aan een adresseerbaar object is gegeven.  | [optional] 
**huisletter** | **str** | Een toevoeging aan een huisnummer in de vorm van een letter die door de gemeente aan een adresseerbaar object is gegeven.  | [optional] 
**huisnummertoevoeging** | **str** | Een toevoeging aan een huisnummer of een combinatie van huisnummer en huisletter die door de gemeente aan een adresseerbaar object is gegeven.  | [optional] 
**aanduiding_bij_huisnummer** | [**Waardetabel**](Waardetabel.md) |  | [optional] 
**postcode** | **str** | De door PostNL vastgestelde code die bij een bepaalde combinatie van een straatnaam en een huisnummer hoort.  | [optional] 
**woonplaats** | **str** | Een woonplaats is een gedeelte van het grondgebied van de gemeente met een naam.  | [optional] 
**in_onderzoek** | [**VerblijfadresBinnenlandInOnderzoek**](VerblijfadresBinnenlandInOnderzoek.md) |  | [optional] 

## Example

```python
from brp_historie_client.models.verblijfadres_binnenland import VerblijfadresBinnenland

# TODO update the JSON string below
json = "{}"
# create an instance of VerblijfadresBinnenland from a JSON string
verblijfadres_binnenland_instance = VerblijfadresBinnenland.from_json(json)
# print the JSON string representation of the object
print(VerblijfadresBinnenland.to_json())

# convert the object into a dict
verblijfadres_binnenland_dict = verblijfadres_binnenland_instance.to_dict()
# create an instance of VerblijfadresBinnenland from a dict
verblijfadres_binnenland_from_dict = VerblijfadresBinnenland.from_dict(verblijfadres_binnenland_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


