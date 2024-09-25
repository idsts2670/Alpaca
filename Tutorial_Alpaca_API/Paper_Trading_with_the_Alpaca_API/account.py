import alpaca_trade_api as tradeapi
from alpaca_trade_api import REST
import config

api = tradeapi.REST(config.ALPACA_API_KEY_PAPER, config.ALPACA_API_SECRET_KEY_PAPER, base_url=config.ALPACA_BASE_URL)

class Account:
    def __init__(self) -> None:
        self.account_number = ''
        self.cash = ''
        self.equity = ''
        self.regt_buying_power = ''

#acc = api.get_account()
#print(acc)
acc = Account()


def accDetails():
    a = api.get_account()
    acc.account_number = getattr(a, 'account_number')
    acc.cash = getattr(a, 'cash')
    acc.equity = getattr(a, 'equity')
    acc.regt_buying_power = getattr(a, 'buying_power')

# Run the account details function
accDetails()

print(acc.account_number)