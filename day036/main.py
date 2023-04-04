import requests
import time
from os import environ
from dotenv import load_dotenv

load_dotenv('config.env', override=True)

STOCK_NAME = "TSLA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API = environ.get("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = environ.get("NEWS_API_KEY")
BOT_TOKEN = environ.get("BOT_TOKEN")
CHAT_ID = environ.get("CHAT_ID")

def telegram_bot_send_text(bot_message):
    bot_token = BOT_TOKEN
    bot_chatID = CHAT_ID
    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}'
    bot_response = requests.get(send_text)
    return bot_response.json()

def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
        return round(abs(current - previous) / previous, 5) * 100.0
    except ZeroDivisionError:
        return 0

while True:
    alpha_vantage_parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK_NAME,
        "apikey": STOCK_API,
    }

    news_api_parameters = {
        "q": f"{STOCK_NAME} Market Update",
        "pageSize": 3,
        "apiKey": NEWS_API_KEY,
    }

    alpha_vantage_response = requests.get(STOCK_ENDPOINT, params=alpha_vantage_parameters)
    alpha_vantage_response.raise_for_status()
    stock_data = alpha_vantage_response.json()

    news_api_response = requests.get(NEWS_ENDPOINT, params=news_api_parameters)
    news_api_response.raise_for_status()
    news_data = news_api_response.json()

    closing_prices = [
        stock_data['Time Series (Daily)'][date]['4. close']
        for _, date in zip(range(3), stock_data['Time Series (Daily)'])
    ]

    yd_price = float(closing_prices[0])
    dyd_price = float(closing_prices[1])

    difference = yd_price - dyd_price
    up_down = None
    up_down = "🔺" if difference > 0 else "🔻"

    if get_change(yd_price, dyd_price) >= 5:
        for article in range(3):
            market_performance = [
                f"*{STOCK_NAME}:* {up_down} `{get_change(yd_price, dyd_price)}%`"
            ]
            news_headlines = [f"*Headline:* {news_data['articles'][article]['title']}"]
            news_description = [
                f"*Description:* `{news_data['articles'][article]['description']}`"
            ]
            news = (market_performance + news_headlines + news_description)
            joined_string = "\n".join(news)
            telegram_bot_send_text(joined_string)
    time.sleep(3600) # Wait for 1 hour before running the bot again
