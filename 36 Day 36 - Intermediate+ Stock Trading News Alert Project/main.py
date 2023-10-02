import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
DIF = 0.01

NEWSAPI = "41c437ecbcad425980c8270350a06883"
ALPHAAPI = "XP7UH76UJF9X9JSB"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## TODO 1: Use https://www.alphavantage.co/documentation/#daily
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.
params_alpha = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":ALPHAAPI
}
response_alpha = requests.get(STOCK_ENDPOINT, params=params_alpha)
response_alpha.raise_for_status()

data_alpha = response_alpha.json()
data_alpha = data_alpha["Time Series (Daily)"]
# print(data_alpha)
yesterday = list(data_alpha.keys())[0]
day_before = list(data_alpha.keys())[1]
price_yesterday = float(data_alpha[yesterday]["4. close"])
price_day_before = float(data_alpha[day_before]["4. close"])
differense = round((price_yesterday - price_day_before)/price_day_before, 3)

if differense >= DIF or differense <= -DIF:
    ## TODO 2: Use https://newsapi.org/docs/endpoints/everything
    # Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
    #HINT 1: Think about using the Python Slice Operator
    params_news = {
        "q": COMPANY_NAME,
        "from": day_before,
        "sortBy":"publishedAt",
        "apiKey":NEWSAPI
    }
    response_news = requests.get(NEWS_ENDPOINT, params=params_news)
    response_news.raise_for_status()
    data_news = response_news.json()
    data_news=data_news["articles"][0:3]

    news_list =[]
    for news in data_news:
        news_dict={
            "news_title":news["title"],
            "description":news["description"]
        }
        news_list.append(news_dict)
    # print(news_list)

    for item in news_list:
        print(
            f"""
            {STOCK} {differense*100}%
            Headline: {item["news_title"]}
            Brief: {item["description"]}
            """
        )



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

