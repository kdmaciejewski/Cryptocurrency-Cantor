import requests

key = "https://api.binance.com/api/v3/ticker/price?symbol="

currencies = ["BTCUSDT", "ETHUSDT", "DOGEUSDT", "BNBUSDT"]
j = 0
prices = []

for i in currencies:
    url = key + currencies[j]
    data = requests.get(url)
    data = data.json()
    j = j + 1
    prices.append(float(data['price']))
    #print(f"{data['symbol']} price is {data['price']}")

waluty = {"BTC": prices[0], "ETH" : prices[1], "DOGE" : prices[2], 'BNB' : prices[3], 'USD': 1}


def exchange(val1, cur1, cur2):
    if cur1 == 'USD' and cur2 != 'USD':
        res = val1 / waluty[cur2]
        return (f"{val1} {cur1} na {res} {cur2}", True)

    elif cur1 == cur2:
        return ("", False)

    elif cur1 != 'USD' and cur2 == 'USD':
        res = val1 * waluty[cur1]
        return (f"{val1} {cur1} na {res} {cur2}", True)

    elif cur1 != 'USD' and cur2 != 'USD':
        pre = val1 * waluty[cur1]
        res = pre / waluty[cur2]
        return (f"{val1} {cur1} na {res} {cur2}", True)

    return ("", False)

def bitcoin():
    return prices[0]

def etherium():
    return prices[1]

def dogecoin():
    return prices[2]

def binance():
    return prices[3]

if __name__ == '__main__':
    print(type(prices[0]))
    print(prices[0])
    print(exchange(1, 'BTC', 'USD'))
    # print(bitcoin())
    # etherium()
    # dogecoin()
    # binance()