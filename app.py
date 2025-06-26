import requests
import pandas as pd
import json
 
 
url = 'https://brasilapi.com.br/api/taxas/v1'
response = requests.get(url)
print(response)