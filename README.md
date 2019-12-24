# StocksPuller
 This program is a pet project of mine. To aid in finding information about individual stocks (for day trading or investing), I created this program
 to poll data about stock(s) from yahoo finance and save them into an Excel spreadsheet.
 
 
 Information About Each Script:
 
 MainMenu.py - Command-line user interface for the program. 
 
 Yahoo_Finance.py - This script pulls stock data from Yahoo Finance. Saves data into .json file.
 
 DataUpdate.py - Reads each line of selected text file with a list of stock tickers, and passes that ticker to Yahoo_Finance.py for data retireval
 
 Cruncher.py - Processes .json file information, and writes it into an .csv file
 
 MainMenuAll.py - This is purely for automation. It will process all text files in the "Lists" folder upon running it (see .zip file). It invokes DataUpdate.py and Cruncher.py. I use this script, combined with Windows Task Sceduler, on one of my virual machines to provide myself with daily reports about stocks.
 


The following libraries are required for using the scripts:
OS,
html,
requests,
json,
argparse,
Collections,
csv,
datetime

All of these can be found in Python's Pip. You will need Python 3. I am using Python 3.7 64 bit on Windows 10.


-- NOTE: Please do not run multiple instances of the MainMenu script at once. It won't crash if you do this, but Yahoo Finance will end up delivering a bunch of null data, largely defeating the purpose of the program. Normally, i have a < 1% null query rate with a list of 3000 stocks. If i run multiple instances to process multiple files in parallel, the null query rate is closer to 20% or so. If you use a single instance of the either the MainMenu or MainMenuAll scripts to process each stock list in sequence, you will avoid this problem. 

