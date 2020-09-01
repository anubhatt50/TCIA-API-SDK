import os
import zipfile

path = '/media/DLData/anuraag_data/ACRIN_BRAIN'
for files in os.listdir(path):
    for files2 in os.listdir(os.path.join(path, files)):
        for files3 in os.listdir(os.path.join(path, files, files2)):
            for files4 in os.listdir(os.path.join(path, files, files2, files3)):
                path_old = os.path.join(path, files, files2, files3, files4)
                path_new = os.path.join(path, files, files2, files3, files4.strip('.zip'))
                os.mkdir(path_new)
                with zipfile.ZipFile(path_old, 'r') as zip_ref:
                    zip_ref.extractall(path_new)
                os.remove(path_old)
