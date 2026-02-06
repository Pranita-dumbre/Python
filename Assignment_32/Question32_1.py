import os
import sys
import hashlib

def DirectoryFileSearch(DirName):

    fobj = open("Marvellous.log","w")

    Border = "-"*50

    fobj.write(Border+"\n")
    fobj.write("-----------marvellous Directory Automation--------\n")
    fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write(Border+"\n")

    Ret = os.path.exists(DirName)
    if (Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False ):
        print("It is not a directory")
        return
    
    for FolderName, SubFloderName, FileName in os.walk(DirName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            Checksum = CalculateChecksum(fname)

            fobj.write(f"File name : {fname} Checksum : {Checksum}\n")

def CalculateChecksum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def main():

    Border = "-"*50
    print(Border)
    print("-----------marvellous Directory Automation--------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid Number of arguments")
        print("Please specify the name of directory with extension")
        return
    
    DirectoryFileSearch(sys.argv[1])

    print("Log file created successfully")
   

if __name__ == "__main__":
    main()