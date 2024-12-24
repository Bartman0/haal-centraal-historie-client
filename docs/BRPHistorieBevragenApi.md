# brp_historie_client.BRPHistorieBevragenApi

All URIs are relative to *https://apigw.npr.idm.diginetwerk.net/lap/api/brp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verblijfplaatshistorie**](BRPHistorieBevragenApi.md#verblijfplaatshistorie) | **POST** /verblijfplaatshistorie | 


# **verblijfplaatshistorie**
> VerblijfplaatshistorieQueryResponse verblijfplaatshistorie(historie_query=historie_query)



Raadpleeg de verblijfplaatshistorie van een persoon op de opgegeven peildatum of binnen de opgegeven periode. Het meest actuele adres staat bovenaan.  Zoek met burgerservicenummer 

### Example


```python
import brp_historie_client
from brp_historie_client.models.historie_query import HistorieQuery
from brp_historie_client.models.verblijfplaatshistorie_query_response import VerblijfplaatshistorieQueryResponse
from brp_historie_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apigw.npr.idm.diginetwerk.net/lap/api/brp
# See configuration.py for a list of all supported configuration parameters.
configuration = brp_historie_client.Configuration(
    host = "https://apigw.npr.idm.diginetwerk.net/lap/api/brp"
)


# Enter a context with an instance of the API client
with brp_historie_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = brp_historie_client.BRPHistorieBevragenApi(api_client)
    historie_query = brp_historie_client.HistorieQuery() # HistorieQuery |  (optional)

    try:
        api_response = api_instance.verblijfplaatshistorie(historie_query=historie_query)
        print("The response of BRPHistorieBevragenApi->verblijfplaatshistorie:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BRPHistorieBevragenApi->verblijfplaatshistorie: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **historie_query** | [**HistorieQuery**](HistorieQuery.md)|  | [optional] 

### Return type

[**VerblijfplaatshistorieQueryResponse**](VerblijfplaatshistorieQueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Zoekactie geslaagd  |  * warning -  <br>  * X-Rate-Limit-Limit -  <br>  * X-Rate-Limit-Remaining -  <br>  * X-Rate-Limit-Reset -  <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**406** | Not Acceptable |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**0** | Er is een onverwachte fout opgetreden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

