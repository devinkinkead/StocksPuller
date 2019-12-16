# StocksPuller
 This program is a pet project of mine. I have recently started investing for my retirement. In my portfolio, I have reserved a small 
 amount of cash to dedicate to stock trading. I noticed it was diffuclt to find information about companies outside of the "Hottest 4 stocks to buy right now" blogs. So I took a script I had found online for pulling data from Yahoo Finance, and I heavily modified it to suit my needs. 
 
 MainMenu.py - Command-line user interface for the program. 
 Yahoo_Finance.py - This script pulls stock data from Yahoo Finance. Saves data into .json file.
 DataUpdate.py - Reads each line of selected text file with a list of stock tickers, and passes that ticket to Yahoo_Finance.py for data retireval
 Cruncher.py - Processes .json file information, and writes it into an .csv file
 
 MainMenuAll.py - This is purely for automation. It will process all text files in the "Lists" folder upon running it. It invokes DataUpdate.py and Cruncher.py. I use this combined with Windows Task Sceduler on one of my virual machines to provide myself with daily reports about stocks.
 
