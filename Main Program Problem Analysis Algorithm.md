Main Program Problem Analysis Algorithm : High level Abstract of Gopica

Inputs: -User name

Outputs:

3 visual gold dataset representation timeseries
Gold price data
Current date
Financial news title and summary
Sentiment anaylsis
Descision with data results and whether or not to buy gold right now
Algorithm (Steps in Program):

1) Run / Execute

2) Step 1: Introduction from GOPICA

3) Ask user name

4) Call current date from jupyter server time ex) December 07, 2020 GOPICA dialouge

5) Step 2: Data graphs time series visual data trend represented (1950-2020) GOPICA dialouge

6) Step 3: Data graphs time series visual data trend represented (2020) High, low, average GOPICA dialouge

7) Step 4: Data graphs time series visual data trend represented (2020) Daily percent change GOPICA dialouge

8) Step 5: Call gold data real time data 1) Call date / real time 2) Gold price right now

GOPICA dialouge

old algorithm 1) Call date / real time 2) Gold price right now 3) Highest Today  4)𝐿𝑜𝑤𝑒𝑠𝑡𝑇𝑜𝑑𝑎𝑦  5) Change in percent compared from previous date

9) Step 6: Financial news titles and auto generated summary shown - Top three articles

GOPICA dialouge
10) Calculate sentiment levels of the auto generated news titles

GOPICA dialouge
11) Inside calculate sentiment levels of financial news sentiment for algorithm calculation 1) positive = 1, neutral = 0, negative = -1

Old algorithm########### if current price > previous gold price - 3 elif current price < previous gold price + 3 else current price + 0 (First part of rank system algorithm whether or not to invest or not) ###################

GOPICA dialouge

12) Step 7: News sentiment algorithm scoring if news title is positive + 1 elif news title is negative -1 else news title neutral + 0

13) Final algorithm of buying gold Calculate with rank system(example) if x > 1 = buy right now elif 1 > x > 0 Look at for a while else: 0 > x do not buy right now

14) Show results of whether or not to buy gold with the current price an date
