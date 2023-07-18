import requests
import json

api_url='https://v6.exchangerate-api.com/v6/52c7cb9e0c3f4648486225a4/latest/'

bozulan_doviz = input('bozulan doviz türü : ')
alinan_doviz = input('alinan doviz türü : ')
miktar = int(input(f'ne kadar {bozulan_doviz} bozmak istiyorsunuz? : '))

result=requests.get(api_url+bozulan_doviz)
result=json.loads(result.text)

# print(result)

print('1 {0} = {1} {2}'.format(bozulan_doviz,result['conversion_rates'][alinan_doviz],alinan_doviz))

print('{0} {1} = {2} {3}'.format(miktar,bozulan_doviz,miktar*result['conversion_rates'][alinan_doviz],alinan_doviz))