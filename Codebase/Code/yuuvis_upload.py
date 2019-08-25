import requests
import json

key = "9247ef2009ba4e86a10874c39a1f1868"
#relative path to your content file
contentFilePath = r'C:\Users\kvemishe\Desktop\Postman\IncidentReport.md'
#relative path to your metadata file
metaDataFilePath = r'C:\Users\kvemishe\Desktop\Postman\metadata.json'

""" test1 = open(metaDataFilePath, 'rb')
test2 = open(contentFilePath, 'rb') """

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'api.yuuvis.io'

header_name = 'Content-Type'
#headerDict['Content-Type'] = 'multipart/form-data, application/x-www-form-urlencoded'
header_name = 'Ocp-Apim-Subscription-Key'
headerDict['Ocp-Apim-Subscription-Key'] = key
print(headerDict['Ocp-Apim-Subscription-Key'])

session = requests.Session()

multipart_form_data = {
    'data' :('data.json', open(metaDataFilePath, 'rb'), 'application/json'),
    'cid_63apple' : ('content.pdf', open(contentFilePath, 'rb'), 'application/pdf')
}
print(str(baseUrl+'/dms/objects'))
response = session.post(str(baseUrl+'/dms/objects'), files= multipart_form_data, headers=headerDict)
print(response.json())
