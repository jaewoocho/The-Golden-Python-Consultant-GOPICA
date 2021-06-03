!pip install --upgrade chart-studio plotly
! pip install zeep

import pandas as pd
import plotly.express as px 
import requests
from datetime import date

# Used for old API that used to work 
# import zeep
# from zeep import xsd
# from zeep import Client 

 

# Step 1 : GOPICA and user introduction
username = input('What is your user name ? : ')
today = date.today()
date = today.strftime("%B %d, %Y")


# Multiple print statements are used throughout program for improved user interface visualization and readability 
# Also these print statments build a dialogue format for GOPICA 

print('\nHello, my name is GOPICA your Golden Python Consultant ! ')
print('G.O.P.I.C.A : Golden Operating Python Intelligence Consulting Assistant \n')
print('\n\n\n\n\n\n\n')
print(f'\nGOPICA: Hello "{username}"! I will be your personal Golden Python consultant for today!')  
print(f'\nSYSTEM: Calling data and records for {username} for today on {date}.........')
print(f'\nGOPICA: Now as your golden consultant, lets start with the monthly gold prices from 1950 to 2020.')


# Step 2: Montly Gold price data timeseries from 1950 to 2020
goldprice1950 = pd.read_csv('goldprice1950.csv')
goldprice1950fig = px.line(goldprice1950, x='Date', y = 'Price USD per Oz', title = 'Gold Price from 1950 to 2020 per Oz')
goldprice1950fig.update_xaxes(rangeslider_visible=True, 
        rangeselector=dict(buttons=list([dict(count=1, label='1 Month', step = 'month', stepmode = 'backward'), 
                                         dict(count=6, label='6 Month', step = 'month', stepmode = 'backward'), 
                                         dict(count=1, label='Year to Date', step = 'year', stepmode = 'todate'), 
                                         dict(count=1, label='1 Year', step = 'year', stepmode = 'backward'),
                                         dict(step='all')])))
goldprice1950fig.show()

print(f'\nGOPICA: {username}, this is a data trend of monthly gold data prices from 1950 to 2020.')
print(f'\n        Navigate through the data graph by pressing each time period button from 1 Month to 1 Year.')
print(f'\n        {username}, you can customize which data plots to display by dragging and moving the white bars below the graph.')
print('\n\n\n\n\n\n\n')


#Step 3: Daily Gold price data timeseries from  2020 - High, Low, Average
print(f'GOPICA: "{username}", as we are done viewing through the data trends from 1950 to 2020, now lets look deeper in to the daily datasets from 2011 to 2020.')
goldprice2020 = pd.read_csv('goldprice2020g.csv')
goldprice2020fig = px.line(goldprice2020, x = 'Date', y =goldprice2020.columns, hover_data={'Date':'|%B %d, %Y'}, title = 'Gold Price from 2011 to 2020 Price value: Average, High, Low Price ' )
goldprice2020fig.update_xaxes(rangeslider_visible=True, 
        rangeselector=dict(buttons=list([dict(count=1, label='1 Month', step = 'month', stepmode = 'backward'), 
                                         dict(count=6, label='6 Month', step = 'month', stepmode = 'backward'), 
                                         dict(count=1, label='Year to Date', step = 'year', stepmode = 'todate'), 
                                         dict(count=1, label='1 Year', step = 'year', stepmode = 'backward'),
                                         dict(step='all')])))
goldprice2020fig.show()

print(f'\nGOPICA: {username}, this is a data trend of daily gold data prices from 2011 to 2020.')
print(f'\n        Navigate through the data graph by pressing each time period button from 1 Month to 1 Year.')
print(f'\n        {username}, you can customize which data plots to display by dragging and moving the white bars below the graph.')
print(f'\n        There is a new feature for this timeseries graph as you can see with the High, Low, and Average(price) prices on the right.')
print(f'\n        You can compare single or two daily price changes with the variables of high, low and average by clicking on the variables.')
print(f'\n        For example, try clicking on the low and price variables on the right to look at the daily changes of high gold prices!')
print('\n\n\n\n\n\n\n')

#Step 4: Daily Percent Changes for Gold price data timeseries from  2020 - High, Low, Average
print(f'GOPICA: "{username}", as we are done viewing through the daily datasets from 2011 to 2020 , now lets look deeper in to the daily changes in percent from 2011 to 2020!')
goldprice2020per = pd.read_csv('goldprice2020.csv')
goldprice2020per['Percent %'] = goldprice2020per['Chg%'] * 100
goldprice2020perfig = px.line(goldprice2020per, x='Date', y = 'Percent %', title = 'Gold Price from 2011 to 2020: Daily Gold price Value Change Percentage (%)')
goldprice2020perfig.update_xaxes(rangeslider_visible=True, 
        rangeselector=dict(buttons=list([dict(count=1, label='1 Month', step = 'month', stepmode = 'backward'), 
                                         dict(count=6, label='6 Month', step = 'month', stepmode = 'backward'), 
                                         dict(count=1, label='Year to Date', step = 'year', stepmode = 'todate'), 
                                         dict(count=1, label='1 Year', step = 'year', stepmode = 'backward'),
                                         dict(step='all')])))

goldprice2020perfig.show()

print(f'\nGOPICA: {username}, this is a data trend of daily percent changes in the average gold data prices from 2011 to 2020 from above.')
print(f'\n        Navigate through the data graph by pressing each time period button from 1 Month to 1 Year.')
print(f'\n        {username}, you can customize which data plots to display by dragging and moving the white bars below the graph.')
print('\n\n\n\n\n\n\n')


# Step 5: Realtime Gold prices - old APi and recent real time gold price API formulas are included
print(f'GOPICA: "{username}", as we are done viewing through the daily percent changes datasets from 2011 to 2020, now lets look for real time gold prices for today!')

# Current code - only 50 requests per month 

# URl for new real time gold api https://rapidapi.com/solutionsbynotnull/api/live-metal-prices
url = "https://live-metal-prices.p.rapidapi.com/v1/latest"
headers = {
    'x-rapidapi-key': "99facf63e8msh609b5b752061891p1d89c7jsn3725a00f6c5f",
    'x-rapidapi-host': "live-metal-prices.p.rapidapi.com"
    }
querystring = {'gold' : 'price'}
response = requests.get(url, headers = headers, params = querystring)
realtimegold2 = response.json()
currentgoldprice = realtimegold2['rates']['XAU']

print(f'\nGOPICA: The current date for today is {date}.')
print(f'\n        The current price for gold today : ${currentgoldprice}!\n')


### Old code - If API worked out again Figure 1: in the bottom #####################################################################
# header = xsd.Element('{http://www.xignite.com/services/}Header', xsd.ComplexType([xsd.Element('{http://www.xignite.com/services/}Username',xsd.String())]))
# header_apikey = header(Username='4ED4EC9CDF5144AF8B27239FD359FE5F')
# client = Client('http://globalmetals.xignite.com/xGlobalMetals.asmx?WSDL')
# param = {'Symbol': 'XAU', 'Currency': 'USD'}
# realtimegold = client.service.GetRealTimeExtendedMetalQuote(**param, _soapheaders =[header_apikey])

# golddate = realtimegold['Date']
# goldtime = realtimegold['Time']
# goldname = realtimegold['Name']
# goldhigh = realtimegold['High']
# goldlow = realtimegold['Low']
# goldaverage = realtimegold['Average']
# goldsource = realtimegold['Source']

# goldprevious = realtimegold['PreviousClose']
# goldpreviousdate = realtimegold['PreviousCloseDate']
# goldchange = realtimegold['Change']
# goldpercentchange = realtimegold['PercentChange']

#print(f'\nGOPICA: The current date for today is {golddate} and most recent time update from the server is  {goldtime}')
#print(f'\n        This real time gold price information is referred from {goldsource} : https://www.swissquote.ch/index/index_quote_e.html?trackPageId=p2q1jh1xr9d1kfxlcds1bnw49*0172731080&cookieId=undefined&sessionId=p2q1jh1xr9d1kfxlcds1bnw49&_ga=2.235861640.845820955.1606234244-60345837.1606234244')
#print(f'\n        The price for {goldname} today :  ${goldaverage}!')
#print(f'\n        The highest price for {goldname} today :  ${goldhigh}!')
#print(f'        The lowest price for {goldname} today :  ${goldlow}!')

#print(f'\nGOPICA: {username}, this is the real time gold prices of from {goldpreviousdate}')
#print(f'\n        The previous price for {goldname} on {goldprevious} :  ${goldprevious}!')
#print(f'\n        From our calculations, we found out that there is a {goldchange} or {goldpercentchange} difference in gold prices from {goldpreviousdate} to {golddate}')
#print('\n\n\n\n\n\n\n')
######################################################################################################

#Step 6: Bloomberg financial news and summaries with sentiment analysis
print(f'GOPICA: "{username}", as we are done viewing through real time gold prices, now lets look at what the financial world is up to!')

# Function broke up in to code segments to handle API format change errors 

url = 'https://bloomberg-market-and-financial-news.p.rapidapi.com/news/list'
querystring = {'id' : 'markets'}
headers = {'x-rapidapi-key': "6018901125msh963d34fe02407f7p14fa7cjsna4e61dfbbbc9",'x-rapidapi-host': "bloomberg-market-and-financial-news.p.rapidapi.com"}
response = requests.get(url, headers = headers, params = querystring)
news = response.json()

newstitle1 = news['modules'][0]['stories'][0]['title']
newssum1 = news['modules'][0]['stories'][0]['autoGeneratedSummary']

newstitle2 = news['modules'][2]['stories'][0]['title']
newssum2 = news['modules'][2]['stories'][0]['autoGeneratedSummary']


newstitle3 = news['modules'][3]['stories'][0]['title']
newssum3 = news['modules'][3]['stories'][0]['autoGeneratedSummary']

# Old function used - Not used to prevent errors as financial API document format constantly changes 
# sentiment anaylsis input changed from news summary to new title as some news articles don't have summaries
# def sentiment(text):
#            key = "apikeyhiddenjcho02azure"
#            endpoint = "https://ist256-jcho02-text-analytics.cognitiveservices.azure.com/"
#            url = f'{endpoint}text/analytics/v3.0/sentiment'
#            header = { 'Ocp-Apim-Subscription-Key' : key}
#            documents = {'documents': [{'id': '1', 'text': text },]}
#            response = requests.post(url,headers=header, json=documents)
#            sentiment = response.json()
#            news_sentiment = sentiment['documents'][0]['sentiment']
#            return news_sentiment
# firstnewssentiment = sentiment(newssum1)
# secondnewssentiment = sentiment(newssum2)
# thirdnewssentiment = sentiment(newssum3)
        

key = "apikeyhiddenjcho02azure"
endpoint = "https://ist256-jcho02-text-analytics.cognitiveservices.azure.com/"
url = f'{endpoint}text/analytics/v3.0/sentiment'
header = { 'Ocp-Apim-Subscription-Key' : key}
    
documents = {'documents': [{'id': '1', 'text': newstitle1 },]}
response = requests.post(url,headers=header, json=documents)
sentiment = response.json()
firstnewssentiment = sentiment['documents'][0]['sentiment']
    
documents = {'documents': [{'id': '1', 'text': newstitle2 },]}
response = requests.post(url,headers=header, json=documents)
sentiment = response.json()
secondnewssentiment = sentiment['documents'][0]['sentiment']
    
documents = {'documents': [{'id': '1', 'text': newstitle3 },]}
response = requests.post(url,headers=header, json=documents)
sentiment = response.json()
thirdnewssentiment = sentiment['documents'][0]['sentiment']
        


print(f'\nGOPICA: {username} as you know, financial news around the world brings a great influence to the price of gold prices.')
print(f'\n        So, we will bring the three different financial news articles from our professional financial news source Bloomberg!')
print(f'\n        Also, we will provide a sentiment analysis on the financial news articles to help determine the positivity of the news!')
print('\n\n\n')

print(f'Financial News from Bloomberg on {date}')
print('\n\n\n')

print(f'First Financial News: {newstitle1} \n')
print(f'News sentiment analysis : {firstnewssentiment}\n')
print(f'News Summary: {newssum1}\n\n\n')

print(f'Second Financial News: {newstitle2} \n')
print(f'News sentiment analysis : {secondnewssentiment}\n')
print(f'News Summary: {newssum2}\n\n\n')

print(f'Third Financial News: {newstitle3} \n')
print(f'News sentiment analysis : {thirdnewssentiment}\n')
print(f'News Summary: {newssum3} \n\n\n')
print('\n\n\n\n\n\n\n')

# Step 7: Final Algorithm and final results 

print(f'GOPICA: "{username}", now we are done analyzing with financial news and the news sentiment analysis!')
print(f'\n      Right now, we have gone through gold price data trends, real time gold prices, and financial news analysis.')
print(f'\n      Now we will calculate the data outputs from the data for our special algorithm.')
print(f'\n      Please wait for a moment until we are done processing for your results on deciding to invest in gold right now.')
print('\n\n\n\n\n\n\n')
print(f'SYSTEM: Calculation is in process.................  0 % / 100%')
print('\n\n\n\n\n\n\n')
print(f'SYSTEM: Calculation is in process................. 25 % / 100%')
print('\n\n\n\n\n\n\n')
print(f'SYSTEM: Calculation is in process................. 50 % / 100%')
print('\n\n\n\n\n\n\n')
print(f'SYSTEM: Calculation is in process................. 75 % / 100%')
print('\n\n\n\n\n\n\n')
print(f'SYSTEM: Calculation computation is complete!...... 100% / 100% ! \n\n')
print(f'GOPICA: Here are your results {username} !')
print('\n\n\n\n\n\n\n')


### Old code - If API worked out again#########################################################
# goldscore = 0

# if goldaverage > goldprevious:
#    goldscore = goldscore - 3
# elif goldaverage < goldprevious:
#    goldscore = goldscore + 3
# else: 
#    goldscore = goldscore + 0


###################################################################
newsscore = 0

if firstnewssentiment == 'negative':
    newsscore = newsscore - 1 
elif firstnewssentiment == 'positive':
    newsscore = newsscore + 1
else:
    newsscore = newsscore + 0
    
if secondnewssentiment == 'negative':
    newsscore = newsscore - 1 
elif secondnewssentiment == 'positive':
    newsscore = newsscore + 1
else:
    newsscore = newsscore + 0
    
if thirdnewssentiment == 'negative':
    newsscore = newsscore - 1 
elif thirdnewssentiment == 'positive':
    newsscore = newsscore + 1
else:
    newsscore = newsscore + 0

#### Old code - If API worked out again#
# totalscore = goldscore + newsscore
# For the final calculation in the bottom, total score is suppose to be used instead of newsscore if the API worked
##################################


if newsscore > 1:
    print(f'Buy Gold Right Now! Current gold price for {date} is ${currentgoldprice} !')
elif 0 > newsscore :
    print(f'Do Not buy Gold Right Now! Current gold price for {date} is ${currentgoldprice} !')
else: 
    print(f'Buy Gold if you have some money left. Current gold price for {date} is ${currentgoldprice} !')
    
print('\n\n\n')

