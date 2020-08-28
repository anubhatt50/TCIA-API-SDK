from tciaclient import TCIAClient
import urllib2, urllib,sys

####################################  Function to print server response #######
def printServerResponse(response):
    if response.getcode() == 200:
        print "Server Returned:\n"
        print response.read()
        print "\n"
    else:
        print "Error: " + str(response.getcode())

tcia_client = TCIAClient(baseUrl="https://services.cancerimagingarchive.net/services/v4",resource = "TCIA")

f = open('patientID.csv', "w")

try:
    response = tcia_client.get_series(collection = "ACRIN-FMISO-Brain" , modality = None , studyInstanceUid = None , outputFormat = "csv" )
    f.write(response)
    f.close()

except urllib2.HTTPError, err:
    print "Errror executing program:\nError Code: ", str(err.code), "\nMessage:", err.read()
