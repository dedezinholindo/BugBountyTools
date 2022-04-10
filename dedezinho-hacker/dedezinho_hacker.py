import argparse, sys
import GET_URLS.get_urls as get_url
import GET_SUBDOMAINS.get_subdomain as get_sub


parser = argparse.ArgumentParser(description='Set your Token and Amount example: "sniper.py -t 0x34faa80fec0233e045ed4737cc152a71e490e2e3 -a 0.2 -s 15"')
parser.add_argument('-sub', '--subdomains', action="store_true",  help='str, which bsc we are going to use')
parser.add_argument('-sqli', '--sqlinjection', action="store_true",  help='str, use or not richbot')
parser.add_argument('-xss', '--xsscan', action="store_true",  help='float, Amount in Bnb to snipe e.g. "-a 0.1"')
parser.add_argument('-lfi', '--lfiscan', action="store_true",  help='int, how mutch tx you want to send? It Split your BNB Amount in e.g. "-tx 5"')
parser.add_argument('-subtake', '--subdomaintakeover',action="store_true",  help='Check if your token to buy is a Honeypot, e.g. "-hp" or "--honeypot"')
parser.add_argument('-open', '--openredirect', action="store_true", help='No Buy, Skipp buy, if you want to use only TakeProfit/StopLoss/TrailingStopLoss')
parser.add_argument('-urls', '--geturls', action="store_true", help='int, Percentage TakeProfit from your input BNB amount "-tp 50" ')
parser.add_argument('-all', '--alloptions', action="store_true", help='int, Percentage TakeProfit from your input BNB amount "-tp 50" ')
parser.add_argument('-a', '--archive',default=None, help='float, Amount in Bnb to snipe e.g. "-a 0.1"')
args = parser.parse_args()

class DedezinhoHacker():
    
    def __init__(self):
        self.parseArgs()
        
        
    def parseArgs(self):
        self.sub = args.subdomains
        self.a = args.archive
        self.sqli = args.sqlinjection
        self.xss = args.xsscan
        self.lfi = args.lfiscan
        self.subtake = args.subdomaintakeover
        self.open = args.openredirect
        self.urls = args.geturls
        self.all = args.alloptions
        if not self.number_arguments(self.all, self.sub, self.sqli, self.xss, self.lfi, self.subtake, self.open, self.urls):
            print("Just one argument per time")
            raise SystemExit
        if self.a == None:
            print("[ERROR] Specify de archive with the options -a")
            raise SystemExit
    
    def number_arguments(self, a, b, c, d, e, f, g, h):
        count = 0
        if a:
            count += 1
        if b:
            count += 1
        if c:
            count += 1
        if d:
            count += 1
        if e:
            count += 1
        if f:
            count += 1
        if g:
            count += 1
        if h:
            count += 1
        if count == 1:
            return True
        return False

    def main(self):
        if self.all:
            get_sub.main(self.a)
            get_url.get_all(self.a, "total200")
            return
        
        if self.sub:
            get_sub.main(self.a) 
            return
        
        if self.urls:
            get_url.get_all(self.a, "total200")
            return
            
DedezinhoHacker().main()