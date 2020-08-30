import os
import pandas as pd

df = pd.read_csv("patientID.csv")
path = "/media/DLData/anuraag_data/ACRIN_BRAIN"

for i in range (len(df)):
    if not os.path.exists(os.path.join(path,str(df['PatientID'].iloc[i]).replace('"',''))): os.makedirs(os.path.join(path,str(df['PatientID'].iloc[i]).replace('"','')))
    path2 = os.path.join(path,str(df['PatientID'].iloc[i]).replace('"',''))
    if not os.path.exists(os.path.join(path2,str(df['SeriesDate'].iloc[i]).replace('"',''))): os.makedirs(os.path.join(path2,str(df['SeriesDate'].iloc[i]).replace('"','')))
    path3 = os.path.join(path2,str(df['SeriesDate'].iloc[i]).replace('"',''))
    if not os.path.exists(os.path.join(path3,str(df['Modality'].iloc[i]).replace('"',''))): os.makedirs(os.path.join(path3,str(df['Modality'].iloc[i]).replace('"','')))
    path4 = os.path.join(path3,str(df['Modality'].iloc[i]).replace('"',''))
