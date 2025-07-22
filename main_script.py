import requests

def fetch_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    try:
        response = requests.get(url)
        data = response.json()
        price = data['bpi']['USD']['rate']
        print(f"Current Bitcoin price: ${price}")
    except Exception as e:
        print("Error fetching Bitcoin price:", e)

if __name__ == "__main__":
    fetch_bitcoin_price()
