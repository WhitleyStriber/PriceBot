from websocket import create_connection
import json

ws = create_connection("wss://www.bitmex.com/realtime?subscribe=trade,orderBook:orderBookL2")

priceAmount = None;

while 1:
    result =  ws.recv()
    data = json.loads(result)
    if 'data' in data:
        timestamp = str(data['data'][0]['timestamp'])
        symbol = str(data['data'][0]['symbol'])
        size = int(data['data'][0]['size'])
        price = int(data['data'][0]['price'])
        side = str(data['data'][0]['side'])

        priceAmount = 999999

        # Buy Side
        if (symbol == 'XBTUSD') & (price >= priceAmount) & (side == "Buy"):
            print ("{0} BitMEX {1} {2} contracts market bought at {3}".format(timestamp, symbol, size, price))

        if (symbol == 'XBTUSD') & (price >= priceAmount) & (side == "Sell"):
            print ("{0} BitMEX {1} {2} contracts market sold at {3}".format(timestamp, symbol, size, price))


ws.run_forever()
