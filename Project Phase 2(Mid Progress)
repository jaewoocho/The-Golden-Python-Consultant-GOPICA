Abstract Idea Refactor: 

For the project of "The Golden Python Consultant : GOPICA", it will be a python program that will advise clients(users) after analyzing data from the web. 
The origin of the idea comes from the marvel movie series of Ironman, where JARVIS(Just a Rather very Intelligent System) analyzes and consults Ironman. 
I will also give my program a name like GOPICA as a reference to JARVIS.
When the user is curious on when to buy gold, the program will act like an consultant. 
The program will extract gold price data from a csv file and sort the data. 
Then after sorting and analyzing the gold data, it will show graphs(time series graphs) and tables as evidence. 
After the data is shown the program will compare and contrast the data to provide adivce to the consultant wheter or not to buy gold right now. 
For the algorithm of analyzing, I will incorporate a algorithm for the program to decide whether or not to suggest on buying gold for the user.
As the program works out, there would be possible add ons and upgrades that could make the program more like an consultant. 
This could include extracting financial news article data sets and other concepts that were learned in class to further make upgrades on the consultant.

Project Research and References:

1.  Gold Price Data (1950 - 2020) in INR & USD
The gold price dataset(1950-2020) will be used as a past gold price data set, which was found on kaggle.com. 
The dataset contains gold price data from 1950 to 2020 for each month. 
I need this for the project as it will be a broad dataset to cover up data from the far past. 
As history is repeated from the past to the present and future, the data from 50 years ago to the present will create data trends that could help the user analyze gold prices on a broad spectrum.
The data will be presented with the table and a visual time series graph will be used to show trends in the change of gold prices from 1950 to 2020. 
There will be a time series graph that is interactive as the user can drag and look at different gold price data.
This dataset would be a like a broad overview with a bigger picture for the user to start with as they analyze data trends inorder to choose if they would buy gold or not.
URL : https://www.kaggle.com/svigneshkumars/gold-price-data-1950-2020-in-inr-usd

2.Gold Price (2011-2020) - The dataset contains records of price from 2011 - 2020
-The Gold price dataset(2011-2020) will be a dataset that will be used to analyze gold price data in the modern time, which was also found in kaggle.com.
The gold price data set for 2011-2020 contains data from 2011 to 2020 with gold prices, high, low, and daily changes in the price as percentages. 
I had to change the format of dates and add another column of percent to further make the data more comprehensive and usable for the future data plots. 
This dataset would be used to increase the precision of the data of project with the 10 year dataset to increase the accurate density of the data. 
When it comes to investing, precision is the key factor for users as even small data values could bring dramatic changes to their life. 
For example, if the user buys one oz of gold, the change of a few decimals in the price wouldn't matter alot. 
However, if the user invests thousands and millions of money for gold, a few changes in the decimals would bring huge benefits or losses. 
As the 10 year dataset contains gold prices per day for 10 years, this will create a more accurate view as it is more recent and compacted with data.

URL : https://www.kaggle.com/shikhnu/gold-price

3.Px Plotly timeseries graph / data visualization
I needed a module to visualize my datasets, I thought that plotly was the best module I could use. 
As I am using gold price datasets, I thought that a timeseries graph would be the best form to visualize my data like in the visual data that is represented in the news with COVID19, stock prices, election polls, and many other trends of data. 
As I digged deeper inside the documentation, the deeper I digged in, the more features and functions I found to upgrade my GOPICA project. 
From px Plotly, I created 3 different timeseries from gold prices of 1950-2020, gold prices of 2011- 2020 price changes, and daily gold price percent changes of 2020.

-For the first gold price timeseries of 1950, it visualizes the data trends with each data plot shown for the user to analyze the trend. 
The buttons of month, 6 months, and year are short keys to zoom inside the data for specific dates. 
The range on the bottom of the graph is a interactive navigation bar for each of the data values that could be dragged around and adjusted for the user to analyze specific data values.
Moving the white bars can select the amount of months or years of data and the middle highlighted bar of the data can be moved to specific months and years of the data plot.

-For the second price timeseries of 2011-2020, it visualizes the data trends of changes in the price of gold from average, high, and low prices per day. 
From a big picture of the data it may look like just a long line, however as the user goes deeper into the data, they could see the trends of gold price data changes. 
The user can also select to compare or single view the data trends by selecting the values on the right under variable.
As the user clicks on the blue price line on the right(under variable), the user can view the difference between the high and low values of the gold prices for that specific date. 
This could also work with single views of the user looking at only the higest values of the gold prices per day.

-For the third timeseries graph(2011-2020), it is an extension of the second timeseries graph as it shows the difference of daily gold price values for every day.
As the user looks for more precision and the daily percent changes in gold prices, the third graph gives the user a deeper and different angle for the gold prices for the user.

URLs: 
Plotly Main: https://plotly.com/ 
layout: https://plotly.com/python/reference/layout/xaxis/#layout-xaxis-rangeselector 
Time format URLs for graph: https://github.com/d3/d3-time-format 
Plotly graphs: https://plotly.com/python/time-series/

4.Gold real time API - XigniteGlobalMeets website
-The xigniteglobalMeets website is a website that shows the market prices of metals like gold, platinum and silver with real time prices and data. 
For some reason, all of the other APIs that contain real time gold prices are sensitive to security and only grant access to employees of the company or the "authorized" partnership employees.
Lucky after diving and experimenting to make sure if the real time gold price data was legit, xignitegolbalmeets was the only website that had a API that worked and let me extract data.
I am using a 7 day free trial API, but I am considering on either finding a new API later or just renewing the API(by creating more accounts or paying). 
I will use this to display real time gold price data for the user to make it more interactive and use the data to also incorporate it to my algorithm to decide on whether to buy or not buy gold right now.
This will bring more life and interaction to GOPICA as the data is represented in real time on the day the user wants consultanting on gold prices. 
Also the API will be used for the algorithm to work with scores in a ranking system for GOPICA to decide.

I was also considering to bring historical data API data from the past, however I realized that it wouldn't help for the algorithm and too much data from the past would just blurr the decision of the user. 
(ex) When bitcoin suddenly rose up to 8,000 dollars per bitcoin, people focused more on "oh I should have bought bitcoin when it was like 5 dollars" instead of deciding of buying bitcoin before it rose over 20,000 dollars per bitcoin).

URL: https://www.xignite.com/product/gold-metal#/DeveloperResources/Request/GetRealTimeExtendedMetalQuote

5.Zeep python module
-The zeep python module is python module that is used to read the wsdl(website document langauge) document from xignite(realtime gold price website). 
The xignite website showed how to use the API by using zeep to call the real time gold prices data and convert them in to strings for a dictionary of data to extract. 
This module is the one recommended from the real time gold price API as it the only one that I can retrieve real time gold prices right now(working and legal). 
In the reference for code, I left notes for every function and line of code, so I could change the values of the functions just in case there is a change in API rules or if I would want to get data for other metals like silver or platium.
The URLs below show on how to install and use the functions created by zeep such as zeep: xsd, client, service.

URLs: 
1)pip install zeep: https://pypi.org/project/python-zeep/ 
2) zeep formating - how to use zeep.xsd https://docs.python-zeep.org/en/master/headers.html 
3) zeep formating - how to use zeep.client: https://docs.python-zeep.org/en/master/datastructures.html 
4) zeep formating - how to use zeep.client.service: https://docs.python-zeep.org/en/master/

6.Gold price data source - Swissquote market website
-The Swissquote market webiste is the source origin, where the data of the real time gold prices go through so I could retrieve data.
The real time gold prices data runs with the flow of Swissquote marketwebsite → xignite website → API → WSDL document format → zeep retrieves code after authentication → GOPICA(The gold operating python intelligence consulting assistant).
I found it as I digged and researched the xignite API to find where the data was coming from. I also tried to get access directly from the Swissquote website, but I couldn't get access to the API.
This source is important as it is the root of the real time gold price data for GOPICA.
If there are any problems or errors with the real time data for GOPICA, this would be the first place to start to make sure if the website was down or the data in the website is working.

URls: 
Main website: https://en.swissquote.com/?sq_country=KR 
Real time prices website: https://www.swissquote.ch/index/index_quote_e.html?trackPageId=p2q1jh1xr9d1kfxlcds1bnw49*0172731080&cookieId=undefined&sessionId=p2q1jh1xr9d1kfxlcds1bnw49&_ga=2.235861640.845820955.1606234244-60345837.1606234244

7.News articles API - Bloomberg market and Financial News API (Free trial - 500 Requests per month)
-The Bloomberg Financial News API is a api that brings financial news articles from Bloomberg to display for the user and used for the algorithm of my project GOPICA. 
In the past homeworks and labs, we used the top news article titles from reddit. This was a great exercise, so I implemented this idea as the news is one of the biggest influencers against the price of gold. 
The reddit example was good, however inorder to make a deeper analysis on the future of gold prices, I thought that I should extract news titles from a more financially professional website. 
This is a important section for GOPICA as it will display the top 3 news articles and their short summaries that are generated from the Bloomsberg API.

URL: Bloomberg website: https://www.bloomberg.com/ Bloomberg API : https://rapidapi.com/apidojo/api/bloomberg-market-and-financial-news?endpoint=apiendpoint_b500b719-e908-4672-a9ba-965a8297f9db

8.Azure microsoft sentiment analysis
-The Azure Microsoft sentiment analysis API is a api that analzes the input text and generates the outputs of positive, negative, and neutral. This was the same API that was used from the past exercises and I tried to find an API that was better. However, I realized that the Microsoft Azure sentiment analysis was one of the best text sentiment anaylsis tools as it the result of millions of text sentiment analysis big data samples compressed into an API. The sentiment analysis API will advise the user to decide if the news articles are either positive, negative or neutral. Sometimes users would have a hard time to decide if a news article is displaying positive or negative influence to the world. The sentiment anaylsis api will support the user to decide the sentiment of each article. Also to further upgrade the decision of whether or not to buy gold, the sentiment api will scan the news summary for each article to further make a deeper analysis, which will also help the algorithm for GOPICA.

URL: https://docs.microsoft.com/en-us/azure/?product=analytics
