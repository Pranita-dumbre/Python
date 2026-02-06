import os
import sys
import shutil

def DirectoryCopy(src, dest):
    fobj = open("Marvellous.log","w")

    Border = "-"*50

    fobj.write(Border+"\n")
    fobj.write("-----------marvellous Directory Automation--------\n")
    fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("This is a File replace the extension Script\n")
    fobj.write(Border+"\n")


    if not os.path.exists(src):
        print("Source directory does not exist")
        return


    if not os.path.isdir(src):
        print("Source is not a directory")
        return

    if not os.path.exists(dest):
        os.makedirs(dest)


    for foldername, subfolders, filenames in os.walk(src):
        for fname in filenames:
            src_path = os.path.join(foldername, fname)
            dest_path = os.path.join(dest, fname)
            shutil.copy(src_path, dest_path)
            fobj.write(f"Copied file : {src_path} -> {dest_path}\n")

    fobj.write(Border+"\n")
    fobj.write("-----------End of Application--------\n")
    fobj.write(Border+"\n")

def main():
    Border = "-"*50

    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        print("Usage : DirectoryCopy.py <SourceDir> <DestDir>")
        return

    src = sys.argv[1]
    dest = sys.argv[2]

    DirectoryCopy(src, dest)

    print(Border)
    print("-----------marvellous Directory Automation--------")
    print(Border)
    

if __name__ == "__main__":
    main()
