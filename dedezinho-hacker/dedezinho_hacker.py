import argparse, sys
import GET_URLS.get_urls as get_url
import GET_SUBDOMAINS.get_subdomain as get_sub


parser = argparse.ArgumentParser(description='Set the informations or exploits that you want to execute"')
parser.add_argument('-sub', '--subdomains', action="store_true",  help='get all the subdomains')
parser.add_argument('-sqli', '--sqlinjection', action="store_true",  help='test SQL injection flaws')
parser.add_argument('-xss', '--xsscan', action="store_true",  help='test Cross Site Scripting flaws')
parser.add_argument('-lfi', '--lfiscan', action="store_true",  help='test Local File Inclusion flaws')
parser.add_argument('-subtake', '--subdomaintakeover',action="store_true",  help='test subdomain takeover flaw')
parser.add_argument('-open', '--openredirect', action="store_true", help='Test Open Redirect flaws')
parser.add_argument('-urls', '--geturls', action="store_true", help='Get all the ulrs in the webarchive history ')
parser.add_argument('-all', '--alloptions', action="store_true", help='Check all flaws')
parser.add_argument('-a', '--archive',default=None, help='The archive with the key domains that we will analyze')
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
