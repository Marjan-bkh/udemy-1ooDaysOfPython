import requests
import datetime
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY='34JDX2TN2E7UYW49'
NEWS_API_KEY='f290dcdb24e94d439010121ad594ade7'
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_param={'function':'TIME_SERIES_DAILY','symbol':STOCK_NAME,'apikey':STOCK_API_KEY}
response=requests.get(STOCK_ENDPOINT,params=stock_param)
response.raise_for_status()
data=response.json()['Time Series (Daily)']
data_list=[value for (key,value) in data.items()]
yesterday=float(data_list[0]['4. close'])
# print(yesterday)

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday=float(data_list[1]['4. close'])
# print(day_before_yesterday)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference=abs(yesterday-day_before_yesterday)
# print(difference)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage=abs((yesterday-day_before_yesterday)/day_before_yesterday)*100
# print(percentage)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage >5:
    print('Get News')
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
news_param={'qInTitle':COMPANY_NAME,'apiKey':NEWS_API_KEY}
news_response=requests.get(NEWS_ENDPOINT,params=news_param)
articles=news_response.json()['articles']
three_articles=articles[:3]
# print(three_articles)
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
formatted_article=[f"Headline:{article['title']}. \n Breif:{article['description']}" for article in three_articles]
print(formatted_article)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

