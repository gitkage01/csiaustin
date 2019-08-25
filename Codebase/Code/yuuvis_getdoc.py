import requests
import json

key = "9247ef2009ba4e86a10874c39a1f1868"
#relative path to your new query file
queryFilePath = '/path/to/your/query.json'

headerDict = {}
paramDict = {}
#baseUrl = 'https' + '://' + 'api.yuuvis.io'
objectId = '805715d6-9ed9-4069-8922-bb587ce9d652'
baseUrl = 'https' + '://' + 'api.yuuvis.io'

header_name = 'Content-Type'
headerDict['Content-Type'] = 'application/json'
header_name = 'Ocp-Apim-Subscription-Key'
headerDict['Ocp-Apim-Subscription-Key'] = key

session = requests.Session()

response = session.get(str(baseUrl+'/dms/objects/'+objectId+'/contents/file'), headers=headerDict)
print(response.text)