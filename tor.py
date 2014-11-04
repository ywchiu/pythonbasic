import requests # import vanilla requests
import requesocks # import requesocks
from BeautifulSoup import BeautifulSoup
import time
import re
checkIP = "http://findbook.tw/book/9789865751005/basic" # IP check site
def getip_requesocks(checkIP):
    print "(+) Sending request with requesocks..."
    session = requesocks.session()
    session.proxies = {'http': 'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    f = open('booklist.txt', 'r')
    for rl in f.readlines():
            ele =  rl.strip()
            if ele != 'ISBN':
                    rec = ''.join(ele.split('-'))
                    res = session.get("http://findbook.tw/book/%s/basic"%(rec))
                    res.encoding = 'utf-8'
                    soup = BeautifulSoup(res.text)
                    profile = soup.find('div',{'class':'book-profile'})
                    if profile is not None:
                            print rec,  profile.text.encode('utf-8')
                    else:
                            print rec
            time.sleep(0.1)
    f.close()
	
def main():
    print "Running tests..."
    getip_requesocks(checkIP)

if __name__ == "__main__":
    main()