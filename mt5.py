import MetaTrader5 as mt5
from flask import Flask
from flask import jsonify
import json
import string

app=Flask(__name__)


@app.route('/')
def index():
      return('Hello world')

@app.route('/mt5')
def indexN():
      if not mt5.initialize(login=1835579, server="Deriv-Demo",password="Valentino97#"):
        print("initialize() failed, error code =",mt5.last_error())
        quit()
      pos=(mt5.account_info()._asdict())
      mt5.shutdown()
      return jsonify(pos)

@app.route('/pos')
def indexP():
      if not mt5.initialize(login=1835579, server="Deriv-Demo",password="Valentino97#"):
        print("initialize() failed, error code =",mt5.last_error())
        quit()
      pos=(mt5.positions_get())
      cc=mt5.positions_total()
      somedict ={}
      somelist=''
      y=0
      while(y<cc):
            somedict ={ 
                   "ticket" : [ x[0] for x in pos ][y],
                   "time" : [ x[1] for x in pos ][y],
                   "type" : [ x[5] for x in pos ][y],
                   "magic" : [ x[6] for x in pos ][y],
                   "volume" : [ x[9] for x in pos ][y],
                   "open" : [ x[10] for x in pos ][y],
                   "sl" : [ x[11] for x in pos ][y],
                   "tp" : [ x[12] for x in pos ][y],
                   "profit" : [ x[15] for x in pos ][y],
                   "symbol" : [ x[16] for x in pos ][y],
              }
            somelist=somelist+str(somedict)
            y=y+1
      mt5.shutdown()
      return jsonify(somelist)

if __name__ == "__main__":
    app.run()
# display data on the MetaTrader 5 package
#print("MetaTrader5 package author: ",mt5.__author__)
#print("MetaTrader5 package version: ",mt5.__version__)
 
# establish MetaTrader 5 connection to a specified trading account

 
# display data on connection status, server name and trading account


# display data on MetaTrader 5 version
#print(mt5.version())
 
# shut down connection to the MetaTrader 5 terminal
#mt5.shutdown()