import os
import pandas as pd

path = "media/DLData/mtp_ab_data"
path2 = "media/DLData/anuraag_data/ACRIN_BRAIN"

df = pd.read_csv("patientID.csv")
s = df['SUID']

for files in os.listdir(path):
    print (int(filter(str.isdigit, files)))
