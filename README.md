# StocksPuller
 This program is a pet project of mine. I have recently started investing for my retirement, and I have reserved a small 
 amount of cash to dedicate to stock trading in my portfolio. I noticed it was somewhat difficult to find companies to invest in outside of the "Hottest 4 stocks to buy right now" blogs. To make my life easier, I took a script I had found online for pulling data from Yahoo Finance, and I heavily modified it to suit my needs. I then built a program around the script to turn lists of stock tickers into Excel spreadsheets of financial data.
 
 
 
 Information About Each Script:
 
 MainMenu.py - Command-line user interface for the program. 
 
 Yahoo_Finance.py - This script pulls stock data from Yahoo Finance. Saves data into .json file.
 
 DataUpdate.py - Reads each line of selected text file with a list of stock tickers, and passes that ticker to Yahoo_Finance.py for data retireval
 
 Cruncher.py - Processes .json file information, and writes it into an .csv file
 
 MainMenuAll.py - This is purely for automation. It will process all text files in the "Lists" folder upon running it (see .zip file). It invokes DataUpdate.py and Cruncher.py. I use this script, combined with Windows Task Sceduler, on one of my virual machines to provide myself with daily reports about stocks.
 
If you want to try this out for yourself, please download the included .zip file. All required libraries can be installed on pip.

The following libraries are required for using the scripts:
OS,
html,
requests,
json,
argparse,
Collections,
csv,
datetime

All of these can be found in Python's Pip. You will need Python 3.







-- NOTE: Please do not run multiple instances of the MainMenu script at once. It won't crash if you do this, but Yahoo Finance will end up delivering a bunch of null data, largely defeating the purpose of the program. I have found many .json files to be saved as null when I tried this. Normally, i have a < 1% null query rate with a list of 3000 stocks. If i run multiple instances to process multiple files, howver the null rate is closer to 20% or so. If you use the either the MainMenu or MainMenuAll scripts to process each stock list in sequence, however, you will avoid this problem. 
