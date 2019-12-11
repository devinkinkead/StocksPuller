import os
import json


def main():
    dataPull()


def dataPull():
    os.chdir(r"QueryResults")

    with open(r'Data.txt', "w+") as newFile:
        newFile.write(str("Ticker"))
        newFile.write(":")
        newFile.write(str("1 Year Target"))
        newFile.write(":")
        newFile.write(str("Current Price"))
        newFile.write(":")
        newFile.write(str("Beta"))
        newFile.write(":")
        newFile.write(str("Earnings Per Share"))
        newFile.write(":")
        newFile.write(str("Price to Book"))
        newFile.write(":")
        newFile.write(str("Price/Earnings to Growth Ratio"))
        newFile.write(":")
        newFile.write(str("Debt to Equity"))
        newFile.write(":")
        newFile.write(str("Cash Per Share"))
        newFile.write(":")
        newFile.write(str("Revenue Growth"))
        newFile.write(":")
        newFile.write(str("Gross Profits"))
        newFile.write(":")
        newFile.write(str("Profit Margin"))
        newFile.write(":")
        newFile.write(str("Return on Assets"))
        newFile.write(":")
        newFile.write(str("Current Ratio"))
        newFile.write("\n")
    os.chdir('..')
    file = open('Nasdaq.txt')
    os.chdir(r"Stocks")
    for line in file:
        text = file.readline()
        text = text.replace("\n", "")
               
           
        
        with open(text + ".json") as jFile:
            data = json.load(jFile)
            counter = 0
            for x in data:
                os.chdir("..")
                os.chdir(r"QueryResults")
                if counter > 0:
                 with open(r'Data.txt', "a+") as newFile:
                    newFile.write(str(data[x]))
                    newFile.write(":")
                counter += 1
            with open(r'Data.txt', "a+") as newFile:
                     newFile.write("\n")
            os.chdir('..')
            os.chdir(r'stocks')
        print(str(text + ".json"+" Processed") )  
        
    

    print("\n\n\n\n\nResults Processed")


if __name__ == '__main__':
    main()
