import os
import json
import csv
from datetime import date

##def main(folderName,dName):
##    #Get path of mainMenu file. Will be a base reference point in this file.
##    os.chdir(dName)
##    dataPull(folderName,dName)

# Used for lists of stocks
def dataPull(folderName,dName):
    #nullCount = 0
    os.chdir(dName)
    os.chdir(r"Lists")
    try: 
        file = open(folderName+'.txt')
        csvName = fileHeader(folderName,dName)
        for line in file: #file is the .txt file with list of stocks.
            text = line
            text = text.replace("\n", "")
            
            #Navigate to stocks folder
            os.chdir(dName)
            os.chdir(r"Stocks")   
            os.chdir(folderName)

            try: #.json file should be named after each ticker on the list
                with open(text + ".json") as jFile:
                    data = json.load(jFile)
                    os.chdir(dName)
                    os.chdir(r"QueryResults")
                    newFile = open(csvName,"a+")
                    with newFile:
                        writer = csv.writer(newFile)
                        writer.writerow(data.values())
                        
                             
                                
                    
                    
                print(str(text + ".json"+" Processed") )  
                
            except FileNotFoundError: #Happens when .json file doesn't exist. 
                 print(str(text + ".json"+" Not Processed. Doesn't Exist"))
                 

            except TypeError: #Happens when file is null when pulling down from Yahoo.
                print(str(text + ".json"+" Not Processed. Null File"))
                
                

    except FileNotFoundError : #Happens when the list file doesn't exist
         print("Entered File doesn't Exist")
         os.chdir(dName)
         #nullCount += 1    
    
    print("\n\n\n\n\nResults Processed")
    #print("NullCount is: "+str(nullCount))


# Used for 1 stock.
def individualDataPull(folderName,dName,ticker):
    os.chdir(dName)
    #Add file header to the final .csv
    csvName = fileHeader(folderName,dName)
    #Navigate to stocks folder
    os.chdir(dName)
    os.chdir(r"Stocks")   
    os.chdir(folderName)

    
                         
    try: #.json file should be named after each ticker on the list
        with open(ticker + ".json") as jFile:
            data = json.load(jFile)
            os.chdir(dName)
            os.chdir(r"QueryResults")
            newFile = open(csvName,"a+")
            with newFile:
                writer = csv.writer(newFile)
                writer.writerow(data.values())   
                        
            
            
        print(str(ticker + ".json"+" Processed") )  
        
    except FileNotFoundError: #Happens when .json file doesn't exist. 
         print(str(ticker + ".json"+" Not Processed. Doesn't Exist"))
         

    except TypeError: #Happens when file is null when pulling down from Yahoo.
        print(str(ticker + ".json"+" Not Processed. Null File"))

def fileHeader(folderName,dName):
        #Navigate to queryResults
    os.chdir(dName)
    os.chdir(r"QueryResults")
    #First row in the final file
    csvName = folderName+'-'+str(date.today())+".csv"
    newFile = open(csvName,"w")
    with newFile:
        writer = csv.writer(newFile)
        header = ['Ticker',str("Current Price"),str("1 Year Target"),str("Beta"),str("Earnings Per Share"),str("Price to Book"),str("Price/Earnings to Growth Ratio"),
                  str("Debt to Equity"),str("Cash Per Share"),str("Revenue Growth"),str("Gross Profits"),str("Profit Margin"),str("Return on Assets"),str("Current Ratio"),str("Quick Ratio")]
        writer.writerow(header)
    return csvName

##if __name__ == '__main__':
##    main(folderName,dName)
