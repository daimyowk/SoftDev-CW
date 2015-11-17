''' wget gets webpage on command line 
one way to get data is to get the website '''
import urllib2
import json
#from bs4 import BeautifulSoup

url="https://www.nytimes.com"

request = urllib2.urlopen(url)
result = request.read()
print result
#same as wget
#like reading a file
# beautiful soup  = screen scraping lib
#useful if no other way to get data
#soup = BeautifulSoup(result,'html.parser')
# for a in soup 
# problem with screen scaper is if website changes,all hell breaks loose (breaks)
#api application programming interface - speficiation for calling data
# simple to use
# restful api - apis where url request string, put in parameters as get parameters
#like function call but in url
#api require a key most of the time
# save api key as a variable

#xml form of html
r= json.loads(result)
print r # convert into  dictionaies

d={'name':'thomas', 'age':30}
print json.dumps(d) #converts into json string

#oauth let be a proxy
#api console
#giving website to playyyyy

