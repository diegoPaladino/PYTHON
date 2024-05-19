import requests
import time
from twilio.rest import Client

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_phone_number = 'your_twilio_phone_number'
recipient_phone_number = 'your_phone_number'

# B3 stock symbols
stock_symbols = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA', 'BBDC4.SA', 'ABEV3.SA']

# API endpoint and key (using Alpha Vantage API as an example)
api_url = 'https://www.alphavantage.co/query'
api_key = 'your_alpha_vantage_api_key'

# Threshold for detecting significant drop
drop_threshold = 5.0  # 5% drop

def get_stock_price(symbol):
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '5min',
        'apikey': api_key
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    time_series = data['Time Series (5min)']
    latest_timestamp = sorted(time_series.keys())[0]
    latest_close = float(time_series[latest_timestamp]['4. close'])
    return latest_close

def send_sms(message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    print(f'SMS sent: {message.sid}')

def monitor_stocks():
    initial_prices = {symbol: get_stock_price(symbol) for symbol in stock_symbols}
    while True:
        for symbol in stock_symbols:
            current_price = get_stock_price(symbol)
            initial_price = initial_prices[symbol]
            drop_percentage = ((initial_price - current_price) / initial_price) * 100
            if drop_percentage >= drop_threshold:
                message = f'{symbol} has dropped by {drop_percentage:.2f}%.'
                send_sms(message)
                initial_prices[symbol] = current_price
        time.sleep(300)  # Check every 5 minutes

if __name__ == '__main__':
    monitor_stocks()
