import requests
from bs4 import BeautifulSoup as bs
import time
getir = requests.get("https://raidforums.com/Forum-Databases", headers={"User-Agent":"Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"})
al = getir.status_code
ala = str(al)
source = bs(getir.content,"lxml")
head = source.find_all("span",attrs={"class","forum-display__thread-subject"})
for link in head:
    merhabalaraq = link.text
    print("[#]          raidforums          [#] ")
    print("[#]           "+merhabalaraq+"           [#] ")
    print("[#]           "+ala+"         [#] \n")
    time.sleep(0.3)