import yfinance as yf
import time
from playsound import playsound

def monitor_stock(stock_ticker, alert_duration=900):
    """
    Monitors a given stock and plays an alert sound when the stock is updated.

    :param stock_ticker: Ticker symbol of the stock.
    :param alert_duration: Duration for the alert sound in seconds.
    """
    print(f"Monitoring {stock_ticker}...")
    
    try:
        while True:
            stock_info = yf.Ticker(stock_ticker).info
            print(f"Current price of {stock_ticker}: {stock_info['regularMarketPrice']}")
            
            playsound('alert_sound.mp3')  # Path to your alert sound file
            time.sleep(alert_duration)  # Alert for 15 minutes or until interaction

    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    monitor_stock("BBAS3.SA")  # Stock ticker for Banco do Brasil

#can make this code to bitcoin?
