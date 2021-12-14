import requests
from bs4 import BeautifulSoup as bs
import time
getir = requests.get("https://www.shodan.io/search?query=log4j+1.2", headers={"User-Agent":"Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"})
al = getir.status_code
ala = str(al)
source = bs(getir.content,"lxml")
head = source.find_all("a",attrs={"class","title text-dark"})
for link in head:
    merhabalaraq = link.text
    merhab = merhabalaraq.split("/host/")
    merhaba = str(merhab)
    list = len("[HARVEST]             "+merhaba+"            [HARVEST]   ")
    print("[IP]","-"*liste,"[IP]")
    print("[HARVEST]             "+merhaba+"            [HARVEST]   ")
    print("[ELAPSED TIME]                    "+ala+"                    [ELAPSED TIME]\n")
    #print("[#]          shodan          [#] ")
    #print("[#]           "+merhabalaraq+"           [#] ")
    #print("[#]           "+ala+"         [#] \n")
    time.sleep(0.3)