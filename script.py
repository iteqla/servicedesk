# Deletes files

import glob
import os
import shutil

t1 = (os.environ['temp'])              #get the Windows %temp% folder
destino = "C:\\prove"

# This loop guarantees that the file is really in Windows %TEMP% folder
def del_temp_files():
    tmp_path = t1
    for dirpath, dirname, filename in os.walk(tmp_path):
        if dirpath.startswith(os.environ['temp']):
           shutil.copy2((glob.glob('*.*')), destino)
        else:
            print("CAREFUL!!!", dirpath)

del_temp_files()
