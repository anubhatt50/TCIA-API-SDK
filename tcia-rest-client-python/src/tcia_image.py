from tciaclient import TCIAClient
import urllib2, urllib,sys,csv
import pandas.pd

####################################  Function to print server response #######
'''
def printServerResponse(response):
    if response.getcode() == 200:
        print ("Server Returned:\n")
        print (response.read())
        print ("\n")
    else:
        print ("Error: " + str(response.getcode()))
'''

#tcia_client = TCIAClient(baseUrl="https://services.cancerimagingarchive.net/services/v4",resource = "TCIA")

df = pd.read_csv("patientID.csv")
s = pd['SeriesInstanceUID']
print(s)

