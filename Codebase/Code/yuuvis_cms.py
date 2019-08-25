import requests

class yuuvis:


    #headerDict['Content-Type'] = 'multipart/form-data, application/x-www-form-urlencoded'

    def __init__(self):

        #Class Variables
        self.headerDict = {}
        self.paramDict = {}

        self.baseUrl = 'https' + '://' + 'api.yuuvis.io'
        self.key = "9247ef2009ba4e86a10874c39a1f1868"

        self.header_name = 'Ocp-Apim-Subscription-Key'
        self.headerDict['Ocp-Apim-Subscription-Key'] = self.key
    
        print(self.headerDict['Ocp-Apim-Subscription-Key'])
        self.session = requests.Session()

    def getCurrenSchema(self):
        response = self.session.get(str(self.baseUrl+'/dms/schema/native'), headers=self.headerDict)
        #print(response.json())
        return response.json()


    def uploadDocument(self, contentFilePath, metaDataFilePath,):
        multipart_form_data = {
            'data' :('data.json', open(metaDataFilePath, 'rb'), 'application/json'),
            'cid_63apple' : ('content.pdf', open(contentFilePath, 'rb'), 'application/pdf')
            }
        urlQuery = str(self.baseUrl+'/dms/objects')
        try:
            response = self.session.post(urlQuery, files= multipart_form_data, headers=self.headerDict)
            response.raise_for_status()
        except request.exceptions.HTTPError as err:
            print(err)
        response_data = response.json()
        #print(response_data)
        docId = response_data['objects'][0]['properties']['enaio:objectId']['value']
        #print("docId:", docId)
        return docId, response_data


    def retrieveContentbyDocId(self, docId):
        urlQuery = str(self.baseUrl+'/dms/objects/'+ docId +'/contents/file')
        print(urlQuery)
        
        print(self.headerDict)
        try:
            response = self.session.get(urlQuery, headers=self.headerDict)
            #print(response.text)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)

        return response.text

    def retrieveMetadDatabyDocId(self, docId):
        urlQuery = str(self.baseUrl+'/dms/objects/'+ docId)
        print("MetaData Query by Id: ", urlQuery)
        
        print(self.headerDict)
        try:
            response = self.session.get(urlQuery, headers=self.headerDict)
            #print(response.text)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)

        return response.text

    def retrieveQueryResultsUsingFile(self, queryFilePath):
        query = open(queryFilePath, 'rb')
        response = self.retrieveQueryResultsUsingText(query)
        return response

    def retrieveQueryResultsUsingText(self, query):
        urlQuery = self.baseUrl + '/dms/objects/search'
        print('\n')
        #print("Search Query:", urlQuery)
        try:
           #relative path to your new query file
           header_dict = self.headerDict
           header_dict['Content-Type'] = 'application/json'
           print("Search Query:", query)
           response = self.session.post(urlQuery, data= query, headers=self.headerDict)
           print(response.json())
        except requests.exceptions.HTTPError as err:
            print(err)
        response_data = response.json()

        return response_data





