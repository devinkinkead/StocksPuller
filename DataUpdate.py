import pywinauto as auto
import os
import time
import yahoo_finance as yahoo


##def SP500Update():
##
##
##        file = open('SP500.txt') 
##        for line in file:
##            text = file.readline()
##            text = text.replace("\n","")
##            yahoo.main(text)
##        file.close()
##
##def NasdaqUpdate():
##       file = open('Nasdaq.txt') 
##       for line in file:
##            text = file.readline()
##            text = text.replace("\n","")
##            yahoo.main(text)
##       file.close()

def listUpdate():
      os.chdir(r"Lists")
      listFile()
      entry = input("What is the File Name of the .txt file? (leave out the .txt): ")
      file = open(entry+".txt")
      for line in file:
            text = file.readline()
            text = text.replace("\n","")
            os.chdir("..")
            yahoo.main(text)
      file.close()
def listFile():
        file_list = os.listdir()
        print(file_list)
