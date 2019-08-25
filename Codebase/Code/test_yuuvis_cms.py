from yuuvis_cms import yuuvis
import time
doc_session = yuuvis()

schema = doc_session.getCurrenSchema()
#print(schema)

#Test uploading document

#relative path to your content file
contentFilePath = r'C:\Users\kvemishe\Desktop\Postman\IncidentReport.md'
#relative path to your metadata file

#-----Upload a document--------------#
metaDataFilePath = r'C:\Users\kvemishe\Desktop\Postman\metadata2.json'
docId, output_response = doc_session.uploadDocument(contentFilePath, metaDataFilePath )
print("docId:", docId)

#Wait for database to update
time.sleep(1)


#-------Read the contents by docId-------#
data = doc_session.retrieveContentbyDocId(docId)
print("Content Revtrieved: \n",data)

#-------Read the metadata by docId-------#
data = doc_session.retrieveMetadDatabyDocId(docId)
print("MetaData Revtrieved: \n",data)

#-----Get Query Results by Query --------------#
query = """{
  "query": {
    "statement": "SELECT Incident,Vector FROM IncidentReports WHERE SEX= 'Male' ",
    "skipCount": 0,
    "maxItems": 5
  }
}"""

data = doc_session.retrieveQueryResultsUsingText(query)

#-----Get Query Results by File-----------------#
queryPath = r'C:\Users\kvemishe\Desktop\Postman\query.json'
data = doc_session.retrieveQueryResultsUsingFile(queryPath)

#---- Upload Multiple Documents at a time ------#
metaDataFilePath = r'C:\Users\kvemishe\Desktop\Postman\metadata2.json'
docId, output_response = doc_session.uploadDocument(contentFilePath, metaDataFilePath )
print("docId:", docId)

#Wait for database to update
time.sleep(1)
