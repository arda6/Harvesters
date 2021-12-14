import requests
from bs4 import BeautifulSoup as bs
import time
getir = requests.get("https://www.google.com/search?q=inurl%3A.php%3Fid%3D&rlz=1C1CHZN_trTR975TR975&sxsrf=AOaemvIGqO5M0HONTd9v6tp4Pe56MT-q1A%3A1638888497412&ei=MXSvYc7DGMGlptQP1ZOQsAg&ved=0ahUKEwiOoNu199H0AhXBkokEHdUJBIYQ4dUDCA8&uact=5&oq=inurl%3A.php%3Fid%3D&gs_lcp=Cgdnd3Mtd2l6EANKBAhBGAFQlx1YziJg5iRoA3AAeACAAYUCiAH5B5IBBTAuMy4ymAEAoAEBwAEB&sclient=gws-wiz", headers={"User-Agent":"Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"})
al = getir.status_code
ala = str(al)
source = bs(getir.content,"lxml")
head = source.find_all("h3",attrs={"class","LC20lb MBeuO DKV0Md"})
for link in head:
    #print(link.text)
    print("[#]          Google Dork Scanner           [#]  ")
    print("[#]          "+link.text+"         [#]")
    print("[#]          "+ala+"         [#] \n")
    time.sleep(0.2)