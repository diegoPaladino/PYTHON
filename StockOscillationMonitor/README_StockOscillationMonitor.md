# StockOscillationMonitor

## Introduction
StockOscillationMonitor is a Python-based program designed to monitor significant stock price fluctuations in the top five companies listed on the Brazilian Stock Exchange (B3). When a substantial drop in stock prices is detected, the program sends an SMS alert to a specified phone number.

## List of Materials Needed
- Python 3.x
- Requests library
- Twilio library
- Twilio account and phone number
- Alpha Vantage API key

## Project Purpose
The purpose of this project is to provide real-time monitoring of stock prices and alert users to significant drops in value, enabling them to take timely action in response to market changes. This tool is especially beneficial for investors and traders who need to stay informed about market movements.

## Pros and Cons
### Pros
- Real-time monitoring of stock prices
- Automated SMS alerts for significant drops
- Easy to set up and use

### Cons
- Depends on third-party services (Twilio and Alpha Vantage)
- Limited to the top five B3 stocks
- Requires internet access for data retrieval and SMS sending

## General Guidelines
### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/StockOscillationMonitor.git
   cd StockOscillationMonitor
