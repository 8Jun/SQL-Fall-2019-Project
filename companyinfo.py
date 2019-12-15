#yf library
import yahoofinance as yf
import sys

#company profile detail
def get_profile():
    while 1:
        try:
            symbol = input("=> Enter Stock Symbol: ")
            profile = yf.AssetProfile(symbol)
            x = symbol+"-profile.csv"
            profile.to_csv(x)
        except KeyboardInterrupt:
            print("\n=> Keyboard Interrupt! Exiting Program...")
            sys.exit()
get_profile()
     
