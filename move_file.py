import os
import shutil
from_dir = "C:/Users/DELL/Downloads"
to_dir =  "C:/Users/DELL/OneDrive/Pictures"
list_of_files = os.listdir(from_dir)
#print(list_of_files)

for fileName in list_of_files:
 n,e = os.path.splitext(fileName)

 if e == "":
   continue

 if e in [".txt",".doc",".docx",".pdf"]: 
   path1 = from_dir + "/" + fileName
   path2 = to_dir + "/" + "documentFiles"
   path3 = to_dir + "/" + "documentFiles" + "/" + fileName
   print(path1)

   if os.path.exists(path2):
      print("moving" + fileName + "....")
      shutil.move(path1,path3)
   else:
       os.mkdir(path2)
       print("moving " + fileName + "...")
       shutil.move(path1,path3)
