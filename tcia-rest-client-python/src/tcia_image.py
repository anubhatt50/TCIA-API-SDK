from tciaclient import TCIAClient
import urllib,sys,csv
import os
import pandas as pd

####################################  Function to print server response #######

def printServerResponse(response):
    if response.getcode() == 200:
        print ("Server Returned:\n")
        print (response.read())
        print ("\n")
    else:
        print ("Error: " + str(response.getcode()))

for i in range(len(df)):
    dPath = os.path.join("/media/DLData/anuraag_data/ACRIN_BRAIN",str(df['PatientID'].iloc[i]).replace('"',''),str(df['SeriesDate'].iloc[i]).replace('"',''),str(df['Modality'].iloc[i]).replace('"',''))
    tcia_client.get_image(seriesInstanceUid = df['SUID'].iloc[i].replace('"','') , downloadPath  =dPath , zipFileName =str(df['SeriesDescription'].iloc[i]).replace('"','')+".zip");
