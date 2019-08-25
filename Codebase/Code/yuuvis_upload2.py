import requests
import json

headerDict = {}
paramDict = {}
baseUrl = 'https' + '://' + 'yuuvis.azure-api.net'

header_name = 'Content-Type'
print(header_name)
if header_name != 'Content-Type':
    headerDict['Content-Type'] = 'multipart/form-data, application/x-www-form-urlencoded'
header_name = 'Ocp-Apim-Subscription-Key'
if header_name != 'Content-Type':
    headerDict['Ocp-Apim-Subscription-Key'] = "9247ef2009ba4e86a10874c39a1f1868"

print(headerDict.keys())
print(headerDict['Content-Type'])
print(headerDict['Ocp-Apim-Subscription-Key'])


session = requests.Session()


#relative path to your content file
contentFilePath = r'C:\Users\kvemishe\Desktop\Postman\IncidentReport.md'
#relative path to your metadata file
metaDataFilePath = r'C:\Users\kvemishe\Desktop\Postman\metadata.json'

multipart_form_data = {
    'data' :('data.json', open(metaDataFilePath, 'rb'), 'application/json'),
    'cid_63apple' : ('content.pdf', open(contentFilePath, 'rb'), 'application/pdf')
}

response = session.post(str(baseUrl+'/dms/objects'), files=multipart_form_data, headers=headerDict)
print(response.content)