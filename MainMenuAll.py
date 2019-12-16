import os
import Cruncher as cruncher
import DataUpdate as dataUpdate
while True:
    #Resets Path
    abspath1 = os.path.abspath(__file__)
    dname = os.path.dirname(abspath1)
    os.chdir(dname)
    print()
    os.chdir(r"Lists")
    for fileName in os.listdir():
        fileName = fileName.replace(".txt","")
        entry = fileName
        print(entry)
        dataUpdate.listUpdate(entry,dname)
        cruncher.main(entry,dname)
    break
