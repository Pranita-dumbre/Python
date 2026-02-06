import os
import sys

def DirectoryFileSearch(DirName ,src, dest ):

    fobj = open("Marvellous.log","w")

    Border = "-"*50

    fobj.write(Border+"\n")
    fobj.write("-----------marvellous Directory Automation--------\n")
    fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("This is a File replace the extension Script\n")
    fobj.write(Border+"\n")


    Ret = os.path.exists(DirName)
    if (Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False ):
        print("It is not a directory")
        return
    
    for FolderName, SubFolder, FileName in os.walk(DirName):
        
         for fname in FileName:
            name, ext = os.path.splitext(fname)
            if(ext == src):
                old_path = os.path.join(FolderName, fname)
                new_path = os.path.join(FolderName, name + dest)
                os.rename(old_path, new_path)
                fobj.write(old_path+"\n")
                fobj.write("renamed\n")
                fobj.write(new_path+"\n")

    fobj.write(Border+"\n")
    fobj.write("-----------End of Application--------\n")
    fobj.write(Border+"\n")
                

def main():

    if(len(sys.argv) != 4):
        print("Invalid Number of arguments")
        print("Please specify the name of directory and with extension")
        return

    DirectoryFileSearch(sys.argv[1],sys.argv[2],sys.argv[3])

    print("Convert successfully")

if __name__ == "__main__":
    main()