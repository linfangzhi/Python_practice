import shutil
import os

path = r'D:\cv'

for (root,dirs,files) in os.walk(path):
    if files:
        print(root,files)
        for file_name in files:
            shutil.move(root+'\\'+file_name,path+'\\'+file_name)