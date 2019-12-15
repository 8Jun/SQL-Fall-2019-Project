#import libaries needed
import yahoofinance as yf #https://pypi.org/project/yahoo-finance/#
import sys #https://docs.python.org/3/library/sys.html

#company profile detail
def get_profile():
    while 1:
        try:
            symbol = input("=> Enter Stock Symbol: ")
            profile = yf.AssetProfile(symbol)
            symbol_1 = symbol+"-profile.csv"
            profile.to_csv(symbol_1)
        except KeyboardInterrupt:
            print("\n=> Keyboard Interrupt! Exiting Program...")
            sys.exit()
get_profile()
     
#csv files were edited to correct format once all profiles were pulled
#this script was use to get company_execs and all_profiles