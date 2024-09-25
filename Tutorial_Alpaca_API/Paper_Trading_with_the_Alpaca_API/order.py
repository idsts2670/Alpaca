import alpaca_trade_api as tradeapi
import requests
import json
import config

# api = tradeapi.REST(config.ALPACA_API_KEY_PAPER, config.ALPACA_API_SECRET_KEY_PAPER, base_url=config.ALPACA_BASE_URL)
ALPACA_BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = f"{ALPACA_BASE_URL}/v2/account"
ORDER_URL = f"{ALPACA_BASE_URL}/v2/orders"
HEADERS = {'APCA-API-KEY-ID': config.ALPACA_API_KEY_PAPER, 'APCA-API-SECRET-KEY': config.ALPACA_API_SECRET_KEY_PAPER}


r = requests.get(ACCOUNT_URL, headers={'APCA-API-KEY-ID': config.ALPACA_API_KEY_PAPER, 'APCA-API-SECRET-KEY': config.ALPACA_API_SECRET_KEY_PAPER})
# print(r.content)


def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)

    return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        'symbol': symbol,
        'qty': qty,
        'side': side,
        'type': type,
        'time_in_force': time_in_force
    }
    r = requests.post(ORDER_URL, json=data, headers=HEADERS)

    return json.loads(r.content)

def get_orders():
    r = requests.get(ORDER_URL, headers=HEADERS)

    return json.loads(r.content)

# response = create_order('APPL', 1, 'buy', 'market', 'gtc')
# response = create_order('NVDA', 1, 'buy', 'market', 'gtc')
# print(response)

orders = get_orders()
print(orders)