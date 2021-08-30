import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API="DH7322L6I8HUWQAD"
NEWS_API="3dfa4f2a80324bd9bf8e9b4e56fe3425"

TWILIO_SID="AC10294f136641b91d8c0e198d7adf0545"
TWILIO_AUTH_TOKEN="8ed5d2b11eea5898fd74316e3d7b9a46"


parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API,
}
# Codes Related To Stocks
stock_response=requests.get(STOCK_ENDPOINT,params=parameters)
data=stock_response.json()["Time Series (Daily)"]

data_list=[value for key,value in data.items()]
yesterday_data=data_list[0]
yesterday_closing=yesterday_data["4. close"]


day_before_yesterday_data=data_list[1]
day_before_yesterday_closing=day_before_yesterday_data["4. close"]



difference=float(yesterday_closing) - float(day_before_yesterday_closing)

diff_percent=abs((difference/float(yesterday_closing)))* 100


if diff_percent> 1:
    #  Codes Related To News On Those Stock's Company
    News_params={
        "apiKey":NEWS_API,
        "qInTitle":COMPANY_NAME,

    }
    News_response=requests.get(NEWS_ENDPOINT,params=News_params)
    articles=News_response.json()["articles"]

    three_articles=articles[:3]
    print(three_articles)
    formatted_article=[f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(TWILIO_SID,TWILIO_AUTH_TOKEN)
    for article in formatted_article:
        message = client.messages \
                .create(
                     body=article,
                     from_='+16783378253',
                     to=input("Enter your phone number:+91")
                 )
    print(message.status)
        



