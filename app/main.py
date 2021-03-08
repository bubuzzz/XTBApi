from XTBApi.api import Client
import time
# FIRST INIT THE CLIENT
client = Client()
# THEN LOGIN

username = ''
password = ''
client.login(username, password, mode='demo')
asset = 'ETHEREUM'
# CHECK IF MARKET IS OPEN FOR EURUSD
client.check_if_market_open(asset)
# BUY ONE VOLUME (FOR EURUSD THAT CORRESPONDS TO 100000 units)
client.open_trade('buy', asset, 1)
# # SEE IF ACTUAL GAIN IS ABOVE 100 THEN CLOSE THE TRADE
trades = client.update_trades() # GET CURRENT TRADES
trade_ids = [trade_id for trade_id in trades.keys()]

print('trade id')
print(trade_ids)

for trade in trade_ids:
    print ('................................. check profit')

    while True:
        actual_profit = client.get_trade_profit(trade) # CHECK PROFIT

        print ('actual_profit %0.02f' % (actual_profit))
        if actual_profit >= 100 or actual_profit < -50:
            client.close_trade(trade) # CLOSE TRADE
        time.sleep(10000)
# CLOSE ALL OPEN TRADES
client.close_all_trades()
# THEN LOGOUT
client.logout()
