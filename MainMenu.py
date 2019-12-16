import os
import Cruncher as cruncher
import DataUpdate as dataUpdate
while True:
    #Resets Path
    abspath1 = os.path.abspath(__file__)
    dname = os.path.dirname(abspath1)
    os.chdir(dname)
    print("1. Query Current Results Only")
    print("2. Pull Current List Data and Query Results")
    print("q. quit")
          
    entry = input("What would you like to do?: ")

    if entry == '1':
       os.chdir(r"Lists")
       print()
       dataUpdate.listFile()
       print()
       entry2 = input("What is the File Name of the .txt file? (leave out the .txt): ")
       #'Crunches' the resulting .json files into .csv files
       cruncher.main(entry2,dname)
    if entry == '2':
        print()
        os.chdir(r"Lists")
        dataUpdate.listFile()
        print()
        entry = input("What is the File Name of the .txt file? (leave out the .txt): ")
        os.chdir(dname)
        #Calls the script that calls the script that pulls down Yahoo Finance information
        dataUpdate.listUpdate(entry,dname)
        cruncher.main(entry,dname)
        
    elif entry == 'q':
        break;


