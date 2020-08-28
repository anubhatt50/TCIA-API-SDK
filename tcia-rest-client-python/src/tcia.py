from tciaclient import TCIAClient
import urllib2, urllib,sys,csv

####################################  Function to print server response #######
def printServerResponse(response):
    if response.getcode() == 200:
        print "Server Returned:\n"
        print response.read()
        print "\n"
    else:
        print "Error: " + str(response.getcode())

tcia_client = TCIAClient(baseUrl="https://services.cancerimagingarchive.net/services/v4",resource = "TCIA")

#f = open('patientID.csv', "w")

try:
    response = tcia_client.get_series(collection = "ACRIN-FMISO-Brain" , modality = None , studyInstanceUid = None , outputFormat = "csv" )
    with open('patientID.csv', 'w') as f:
        writer = csv.writer(f)
        for line in response:
            writer.writerow(line.decode('utf-8').split(','))

except urllib2.HTTPError, err:
    print "Errror executing program:\nError Code: ", str(err.code), "\nMessage:", err.read()
