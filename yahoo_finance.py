from lxml import html
import requests
import json
import argparse
from collections import OrderedDict
import os

def main(ticker,tFileName,dname):
    print("Fetching data for %s" % (ticker))
    scraped_data = parse(ticker)
    scraped_data.pop("") #The first entry pulls junk data. Keeps it out of the .json
    print("Writing data to output file")
    os.chdir(dname)
    os.chdir(r"stocks")
    os.chdir(tFileName)
    with open('%s.json' % (ticker), 'w') as fp:
        json.dump(scraped_data, fp, indent=4)
    os.chdir("..")   

def parse(ticker):
    url = "http://finance.yahoo.com/quote/%s?p=%s" % (ticker, ticker)
    response = requests.get(url, verify=False)
    parser = html.fromstring(response.text)
    summary_table = parser.xpath('//div[contains(@data-test,"summary-table")]//tr')
    summary_data = OrderedDict()
    other_details_json_link = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/{0}?formatted=true&lang=en-US&region=US&modules=summaryProfile%2CfinancialData%2CrecommendationTrend%2CupgradeDowngradeHistory%2Cearnings%2CdefaultKeyStatistics%2CcalendarEvents&corsDomain=finance.yahoo.com".format(
        ticker)
    summary_json_response = requests.get(other_details_json_link)

    json_loaded_summary = json.loads(summary_json_response.text)
    try:
        try:
            y_Target_Est = json_loaded_summary["quoteSummary"]["result"][0]["financialData"]["targetMeanPrice"]['raw']
        except:
            y_Target_Est = "N/A"

        try:
            eps = json_loaded_summary["quoteSummary"]["result"][0]["defaultKeyStatistics"]["trailingEps"]['raw']
        except:
            eps = "N/A"

        try:
            pBook = json_loaded_summary["quoteSummary"]["result"][0]["defaultKeyStatistics"]["priceToBook"]['raw']
        except:
            pBook = "N/A"

        try:
            pegRatio = json_loaded_summary["quoteSummary"]["result"][0]["defaultKeyStatistics"]["pegRatio"]['raw']
        except:
            pegRatio = "N/A"

        try:
            beta = json_loaded_summary["quoteSummary"]["result"][0]["defaultKeyStatistics"]["beta"]['raw']
        except:
            beta = "N/A"

        try:
            currentPrice = json_loaded_summary["quoteSummary"]["result"][0]["financialData"]["currentPrice"]['raw']
        except:
            currentPrice = "N/A"

        try:
            dEquity = json_loaded_summary["quoteSummary"]["result"][0]["financialData"]["debtToEquity"]['raw']
        except:
            dEquity = "N/A"

        try:
            rGrowth = json_loaded_summary["quoteSummary"]["result"][0]["financialData"]["revenueGrowth"]['raw']
        except:
            rGrowth = "N/A"

        try:
            cashPerShare = json_loaded_summary["quoteSummary"]["result"][0]["financialData"]["totalCashPerShare"]['raw']
        except:
            cashPerShare = "N/A"

        try:
            grossProfits = json_loaded_summary["quoteSummary"]["result"][0]["financialData"]["grossProfits"]['raw']
        except:
            grossProfits = "N/A"

        try:
            profitMargins = json_loaded_summary["quoteSummary"]["result"][0]["financialData"]["profitMargins"]['raw']
        except:
            profitMargins = "N/A"
        try:
            returnOnAssets = json_loaded_summary["quoteSummary"]["result"][0]["financialData"]["returnOnAssets"]['raw']
        except:
            returnOnAssets = "N/A"
        try:
            currentRatio = json_loaded_summary["quoteSummary"]["result"][0]["financialData"]["currentRatio"]['raw']
        except:
            currentRatio = "N/A"
        try:
            quickRatio = json_loaded_summary["quoteSummary"]["result"][0]["financialData"]["quickRatio"]['raw']
        except:
            quickRatio = "N/A"
        for table_data in summary_table:
            raw_table_key = table_data.xpath('.//td[contains(@class,"C(black)")]//text()')
            raw_table_value = table_data.xpath('.//td[contains(@class,"Ta(end)")]//text()')
            table_key = ''.join(raw_table_key).strip()
            table_value = ''.join(raw_table_value).strip()
            summary_data.update({table_key: table_value})
            
            summary_data.update(
                {'ticker': ticker, 'currentPrice': currentPrice,'y_Target_Est': y_Target_Est,'beta': beta,
                 'eps': eps, 'pBook': pBook,
                 'pegRatio': pegRatio, 'dEquity': dEquity,
                 'cashPerShare': cashPerShare, 'rGrowth': rGrowth,
                 'grossProfits': grossProfits, 'profitMargins': profitMargins, 'returnOnAssets': returnOnAssets,
                 'currentRatio': currentRatio,'quickRatio': quickRatio})
            return summary_data


    except:
        print("Failed to parse json response")
        return {"error": "Failed to parse json response"}


if __name__ == "__main__":
    main()         
