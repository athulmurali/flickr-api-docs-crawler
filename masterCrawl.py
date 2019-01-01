from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
TD_INDEX_API_METHODS = 2
class Parser:

  @staticmethod
  def get_links(url):
    html=urlopen(url)
    soup=BeautifulSoup(html,"html.parser")
    for all in soup.findAll("h2"):
      print (''.join(all.findAll(text=True)))
  def getAPIMethods(url):
    html=urlopen(url)
    print("\n\n\ngettingAPiMethods\n\n")
    soup=BeautifulSoup(html,"html.parser")
    td = soup.findAll('td')[TD_INDEX_API_METHODS]
    apiMethods = {}
    apiDict=[]
    print("total ul : ", len(td.findAll('ul')))
    print("total h3  : ", len(td.findAll('h3')))
    print("\n\n****Awesome !....\n\n")
    apiDict = []
    for childH3,childUl in zip(td.find_all('h3'),td.findAll('ul')):
      ulDict =[]
      if childH3 and childH3.text: 
        # print(childH3.text)
        pass
      if childUl!= None:
        for li in childUl.findAll('li'):
          if li!=None:
            liDict = {"apiTitle" : li.text,
            "link": li.a["href"]  } 
            ulDict.append(liDict)
            # print(ulDict)
      apiDict.append({ "title" : childH3.text,
                        "api":
                        ulDict })  

    with open('apiLinks.json', 'w') as outfile:
      json.dump(apiDict, outfile, sort_keys=True, indent=4) 
    return apiDict
  def getNotes(htmlPage):
    print("getting Notes")
  def getStatusCode(htmlPage):
    print("getting Status code")
  def getSpanResponse():
    print("hi")
  # API Methods


url="https://www.flickr.com/services/api/"

API_METHODS_parent_id="yui_3_11_0_1_1529698034404_261" 
Parser.get_links(url)
print(type(Parser.getAPIMethods(url)))

