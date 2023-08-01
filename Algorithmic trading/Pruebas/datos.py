import pandas as pd
import unicorn_binance_websocket_api as uni

bwsam = uni.BinanceWebSocketApiManager(exchange="binance.com")

bwsam.create_stream("kline_1m", "ETHUSDT", output="UnicornFy")

def obtener_precio(data):

    time = pd.to_datetime(data["event_time"], unit="ms")
    precio = float(data["kline"]["close_price"])

    print(precio)

while True:

    data = bwsam.pop_stream_data_from_stream_buffer()

    if data and len(data) > 3:
        obtener_precio(data)