import requests
from bs4 import BeatifulSoup

para = input("Euro mu Dolar mı")
if para == "Euro":
    eurourl = "https://kur.doviz.com/serbest-piyasa/euro"
    x = requests.get(eurourl)
    fark = BeautifulSoup(x.content, "html.parser")
    malzemeler = fark.find_all("div", {"class": "flex justify-between mt-8"})
    for y in malzemeler:
        euro = y.find_all("div", {"class": "text-xl font-semibold text-white"})
        euro2 = str(euro)
        euro3 = euro2.replace('[<div class="text-xl font-semibold text-white" data-socket-attr="s" data-socket-key="EUR" data-socket-type="C">'," ")
        euro4 = euro3.replace("</div>]", " ")
        print(euro4)
elif para == "Dolar":
    dolarurl = "https://kur.doviz.com/serbest-piyasa/amerikan-dolari"
    x = requests.get(dolarurl)
    fark = BeautifulSoup(x.content, "html.parser")
    malzemeler2 = fark.find_all("div", {"class": "flex justify-between mt-8"})
    for dolar in malzemeler2:
        dolar2 = dolar.find_all("div", {"class": "text-xl font-semibold text-white"})
        dolar3 = str(dolar2)
        dolar4 = dolar3.replace('[<div class="text-xl font-semibold text-white" data-socket-attr="s" data-socket-key="USD" data-socket-type="C">', " ")
        dolar5 = dolar4.replace('</div>]', " ")
        print(dolar5)