import os
import shutil

path = "/media/DLData/anuraag_data/TCGA_GBM/MR"
path2 = "/media/DLData/anuraag_data/data"

for files in os.listdir(path):
    for files2 in os.listdir(os.path.join(path, files)):
        for files3 in os.listdir(os.path.join(path, files, files2)):
            if "AX_T1" in files3 or "AXIAL_T1" in files3:
                for files4 in os.listdir(os.path.join(path, files, files2, files3)):
                    src = os.path.join(path, files, files2, files3, files4)
                    dst = "TCGA_GBM_MR_"+files+"_"+files2+"_"+files3+"_"+files4
                    dstn = os.path.join(path2,dst)
                    shutil.copy(src,dstn)
                print(files3+"->"+dst)
