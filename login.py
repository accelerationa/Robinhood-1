from Robinhood import Robinhood
from pathlib import Path 

my_trader = Robinhood()

file = open(str(Path.home()) + '/.robinhood/cred', 'r')
cred = file.read().splitlines()
username = cred[0]
password = cred[1]

logged_in = my_trader.login(username=username, password=password)
if not logged_in:
    raise Exception('Unable to login. ')