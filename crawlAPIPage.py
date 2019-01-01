from bs4 import BeautifulSoup
from urllib.request import urlopen
import logging
import json
with open('apiLinks.json') as f:
    data = json.load(f)

url="https://www.flickr.com"
apiPageDictArray = []
count = 0
crawlErrorArray  = []
errorArray=[]

for i in data:

  apiPageDict ={}

  for  j in  i.get("api"):
    link = j.get("link")
    try:
      newUrl = url +  link 
      print(" index : ",count, "crawling .... : ",newUrl, )
      html=urlopen(newUrl)
      soup= BeautifulSoup(html,"html.parser")
      infoCase =  soup.find("div", {"class": "InfoCase"})
      title= infoCase.find('h1').text
      methodDescription = infoCase.find("div", {"class": "MethodDescription"})
      methodDescriptionText = infoCase.find("div", {"class": "MethodDescription"}).text

      infoCases = infoCase.findAll("dl")
      arguments = infoCases[0].text
      
      errorCodesArray = []
      arguments = []
    
      for dt,dd in zip( infoCases[0].findAll('dt'),
      infoCases[0].findAll('dd')):
        field = dt.b.extract().text
        optional = dt.text
        description = dd.text
        argumentDict = {
          "field"     : field,
          "required"  : optional,
          "description" : description 
        }
        arguments.append(argumentDict)
        
      for dt,dd in zip( infoCases[1].findAll('dt'),
      infoCases[1].findAll('dd')):
        code = dt.text
        description = dd.text
        errorCodeDict = {
          "code" : code,
          "description" : description 
        }

        errorCodesArray.append(errorCodeDict)
      
      errorCodesSet = errorCodesArray
      
      warning =  methodDescription.find('b').text if methodDescription.find('b')  else ""

      explorerDict = {
        "title" : "",
        "link"  : "\link"
      }
      
      apiPageDict = {
        "title"         : title,
        "description"   : methodDescriptionText,
        "Warning"       : warning,
        "arguments"     : arguments,
        "errorCodes"    : errorCodesSet,
        "authentication": ""

      }
      apiPageDictArray.append(apiPageDict)
      count += 1

    except Exception as e:
      errorDict = {
        
        "link" : link,
        "error" : str(e)
      }
      logging.exception(e)
      errorArray.append(errorDict)
      
with open('apiPagesDict.json', 'w') as outfile:
      json.dump(apiPageDictArray, outfile, sort_keys=True, indent=4) 


with open('crawlErrors.json', 'w') as outfile1:
      json.dump(crawlErrorArray, outfile1, sort_keys=True, indent=4) 
