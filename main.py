from os import remove, walk, listdir, scandir


"""
script to delete duplicate .extension files
"""


def filesToDelete(extension):
    filesToDelete = [] 

    # file scanning
    for files in scandir(workingDir):
        if files.name.endswith(extension) and files.is_file():
            #print(files)
            filesToDelete.append(files)
    print(filesToDelete)
    return filesToDelete
    

def removeFiles():
    #global filesToDelete
    # remove section
    for file in filesToDelete:
        remove(file)
        print("The file", file, "has been deleted.")

def listDir():
    for files in listdir(workingDir):
        print(files)

# set working dir
workingDir = input("Working dir: ")
extension = input("Define Extension: ")

# filesToDelete()
filesToDelete = filesToDelete(extension)

# ask user to continue
while True:
    try:
        opcion = input("(Y) to continue, (N) to cancel: ")
        if opcion == "Y":

        # remove files function
            removeFiles()
            print("\nThe directory now has this files:\n")
            listDir()
            print("\nThank you for using this app !\n")
            break

        elif opcion == "N":
            break

    except Exception as e:
        continue 


