from Robinhood import Robinhood
my_trader = Robinhood()

res = my_trader.order_history()

orders = res.get('results')
valid_orders = [order for order in orders if order['state'] != 'cancelled']

order_list = []
for order in valid_orders:
    for execution in order.get('executions'):
        order_list.append({
            'excuted_at': execution.get('timestamp'),
            'price': execution.get('price'),
            'quantity': execution.get('quantity'),
            'side': order.get('side'),
            'state': order.get('state'),
            'symbol': my_trader.symbol(order.get('instrument')
                .replace("https://api.robinhood.com/instruments/", "")
                .replace("/", ""))[0][0]
        })


d = {}

for order in order_list:
    symbol = order.get('symbol')
    if not d.get(symbol):
        d[symbol] = {
            'quantity': 0,
            'revenue': 0
        }

    if order.get('side') == 'buy':
        d[symbol]['quantity'] += (float)(order.get('quantity'))
        d[symbol]['revenue'] -= (float)(order.get('quantity')) * (float)(order.get('price'))
    else:
        d[symbol]['quantity'] -= (float)(order.get('quantity'))
        d[symbol]['revenue'] += (float)(order.get('quantity')) * (float)(order.get('price'))

for k, v in d.items():
    v['revenue'] += (float)(my_trader.quote_data(k).get('previous_close')) * (float)(v.get('quantity'))
    v['quantity'] = 0


for k, v in d.items():
    print(k + ":  " + str(v.get('revenue')))