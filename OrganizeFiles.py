import shutil
import os

#README
#This script should classify files according to their file extension/format. 
#Create folders and moving the files into these folders.


itemsList = os.listdir()

numberOfExtensions = len(itemsList)
extensionsList = []
#This loop should iterate through each item and check extensions. Create folder for each extension.
for i in itemsList:
    
    if '.' in i:
        
        x = i.rindex(".")
        
        #extensionS is the storing occurance of the file extension. 'extensionString'
        extensionS = i[x:]
        
        #see extensionS occurances, if equals 0, then add to extensionsList.
        countInString = extensionsList.count(extensionS)
        
        #this if make sure only create one folder per extension type.
        if countInString == 0: 
            extensionsList.append(extensionS)
            if not os.path.isdir(extensionS): 
                os.mkdir(extensionS)

    #move file into folder.
    directoryCurrent = os.getcwd()
    fileCurrentPath = os.path.abspath(i)
    destinationPath = os.path.join(directoryCurrent, extensionS)
    if not i == "OrganizeFiles.py":
        shutil.move(fileCurrentPath,destinationPath)

#print(extensionsList)


