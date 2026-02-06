import os
import sys


def DirectoryFileSearch(DirName ,extension ):

    fobj = open("Marvellous.log","w")

    Border = "-"*50

    fobj.write(Border+"\n")
    fobj.write("-----------marvellous Directory Automation--------\n")
    fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("This is a File name with specific extenstion Script\n")
    fobj.write(Border+"\n")


    Ret = os.path.exists(DirName)
    if (Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False ):
        print("It is not a directory")
        return
    fobj.write(f"The file name with extension is : {extension}\n")
    
    for FolderName, SubFolder, FileName in os.walk(DirName):
        
        for fname in FileName:
            name, ext = os.path.splitext(fname)
            if(ext == extension):
                fobj.write(fname+"\n")
    fobj.write(Border+"\n")
    fobj.write("-----------marvellous Directory Automation--------\n")
    fobj.write(Border+"\n")


def main():

    Border = "-"*50

    if(len(sys.argv) != 3):
        print("Invalid Number of arguments")
        print("Please specify the name of directory with extension")
        return
    
    DirectoryFileSearch(sys.argv[1],sys.argv[2])

    print("The log file created successfully")

if __name__ == "__main__":
    main()