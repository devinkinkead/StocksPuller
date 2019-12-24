import os
import Cruncher as cruncher
import DataUpdate as dataUpdate
while True:
    #Resets Path
    print()
    abspath1 = os.path.abspath(__file__)
    dName = os.path.dirname(abspath1)
    os.chdir(dName)
    print("1. Query Current Results Only")
    print("2. Pull Current List Data and Query Results")
    print("3. Get Data from Individual Stock and Save in Excel")
    print("q. quit")
          
    entry = input("What would you like to do?: ")

    if entry == '1':
       os.chdir(r"Lists")
       print()
       #prints list of text files
       dataUpdate.listFile()
       print()
       entry2 = input("What is the File Name of the .txt file? (leave out the .txt): ")
       #'Crunches' the resulting .json files into .csv files
       cruncher.dataPull(entry2,dName)
       
    elif entry == '2':
        print()
        os.chdir(r"Lists")
        print()
        #prints list of text files
        dataUpdate.listFile()
        print()
        entry2 = input("What is the File Name of the .txt file? (leave out the .txt): ")
        os.chdir(dName)
        #Calls the script that calls the script that pulls down Yahoo Finance information
        dataUpdate.listUpdate(entry2,dName)
        cruncher.dataPull(entry2,dName)

    elif entry == '3':
        ticker = input("Please type the stock ticker that you want to look up: ")
        dataUpdate.individualUpdate(ticker,dName)
        cruncher.individualDataPull("individual",dName,ticker)

    elif entry == 'q':
        break;

    else:
        print("Invalid Selection. Please select options 1-3 (or q for quit.)")

