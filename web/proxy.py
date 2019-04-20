import requests
import bs4
from random import randrange
"""
@req array [{"url":{"GET":{"param1":"data2","param2":"data2"}}},{"url":{"post":{"param":"data","param2":"data2"}}}, {url:{"PUT:{"param":"data","param2":"data2"}}}, ]
@headers = {'user-agent': 'my-app/0.0.1'}
"""
class proxy:
    def __init__(self,req,headers=None,encoding="utf8",proxyAut=True):
        self.ordenedList = []
        self.proxyAut = proxyAut
        self.encoding = encoding
        self.req = req
        self.headers = headers
        self.reqContent = []

    def getProxyList(self):
        r = requests.get("https://free-proxy-list.net/anonymous-proxy.html")
        html = bs4.BeautifulSoup(r.content, "html5lib")
        rows = html.find_all('tbody')
        rows = html.find_all('tr')
        rows_names = rows.pop(0)
        rows_names = [x.contents for x in rows_names.find_all("th")]
        rows = [x.find_all("td") for x in rows]
        content = []
        for row in rows:
            content.append([z.contents for z in row])
        for _,row in zip(range(len(content)),content):
            listing = {}
            for x,y in zip(rows_names,row):
                listing[x[0]] = y[0]
            if len(listing) == 0:
                break
            self.ordenedList.append(listing)


    def doRequests(self):
        for x in self.req:
            Nrandom = randrange(0, len(self.ordenedList))
            if self.ordenedList[Nrandom]["Https"] == "no":
                proxy = {"http":self.ordenedList[Nrandom]["IP Address"]+":"+self.ordenedList[Nrandom]["Port"]}
            else:
                proxy = {"https":self.ordenedList[Nrandom]["IP Address"]+":"+self.ordenedList[Nrandom]["Port"]}
            for key,val in x.items():
                url = key
                for requestType,params in val.items():
                    if requestType == "GET":
                        thisrequest = requests.post(url=url,headers=self.headers,params=params, proxy=proxy)
                    elif requestType == "POST":
                        thisrequest = requests.post(url=url, headers=self.headers,data=params, proxy=proxy)
                    elif requestType == "PUT":
                        thisrequest = requests.put(url=url, headers=self.headers,data=params,proxy=proxy)
                    elif requestType == "DELETE":
                        thisrequest = requests.delete(url=url,headers=self.headers,data=params, proxy=proxy)
                    elif requestType == "HEAD":
                        thisrequest = requests.head(url=url,headers=self.headers,data=params, proxy=proxy)
                    elif requestType == "OPTIONS":
                        thisrequest = requests.options(url=url,headers=self.headers,data=params, proxy=proxy)
                    thisrequest.encoding = self.encoding
                    self.reqContent.append(thisrequest)

                    