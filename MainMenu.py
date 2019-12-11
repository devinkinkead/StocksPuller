import pywinauto as auto
import os
import time
import Cruncher as cruncher
import DataUpdate as dataUpdate
while True:
    print("1. Query Results")
    print("2. Refresh List Data")
    print("q. quit")
          
    entry = input("What would you like to do?: ")

    if entry == '1':
        cruncher.main()
    if entry == '2':
        dataUpdate.listUpdate()
        cruncher.main()
    elif entry == 'q':
        break;


