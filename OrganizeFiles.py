import shutil
import os
#print statements will be used for testing.
#This script should classify files according to their file extension/format. By creating folders.
#I NEED TO EDIT THIS TO SEARCH FOR THE DOT FROM BACK, some files have multiple dots.
#NEED EDIT
itemsList = os.listdir()

numberOfExtensions = len(itemsList)
extensionsList = []
#This loop should iterate through each item and check extensions. Create folder for each extension.
for i in itemsList:

    if '.' in i:
        
        x = i.index(".")
        
        #extensionS is the storing occurance of the file extension. 'extensionString'
        extensionS = i[x:]
        #Testing to see if working correctly.
        #print(extensionS)
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
    if not i == "OrganizeFiles":
        shutil.move(fileCurrentPath,destinationPath)

#print(extensionsList)


