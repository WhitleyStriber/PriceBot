from websocket import create_connection
import json

ws = create_connection("wss://www.bitmex.com/realtime?subscribe=trade,orderBook:orderBookL2")

while 1:
    result =  ws.recv()
    data = json.loads(result)
    # for key, value in data.items():
    #     # print (key, value)

    if 'data' in data:
        # print(data['data'])
        print(data.get('data'))



ws.close()
