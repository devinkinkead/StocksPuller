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

def listUpdate(entry,dname):
      os.chdir(dname)
      os.chdir(r"Stocks")
      if not os.path.isdir(entry):
            os.mkdir(entry)
      try:
            os.chdir(dname)
            os.chdir(r"Lists")
            file = open(entry+".txt")
            for line in file:
                  text = line
                  text = text.replace("\n","")
                  try:      
                        yahoo.main(text,entry,dname)
                  except:
                        print(text+" Parsing Failed.")
            file.close()
            print("Exiting File....")
            
      except :
            print("Entered File Name Doesn't Exist")
                  
            
            

def listFile():
        file_list = os.listdir()
        print(file_list)
