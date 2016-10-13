import urllib2, urllib
import re
from bs4 import BeautifulSoup

#############################
##      Food Function      ##
#############################

def getMenu():
    machines = []
    url = 'http://www.thecrimson.com/flyby/'
    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website.read(), 'html.parser')
    try:
        sidebar = soup.findAll("section", { "class" : "widget widget-primary" })[0]
        menu = sidebar.findAll("p")
        body = ""
        for i in menu:
            body += i.text.encode('unicode-escape').replace(r'\xb0','')
            body += "\n"
    except Exception, e:
        print str(e)
        return "Could not find food data."
    return body

def makeSpecial():
    s = "Current Menu: \n"
    return s
    
############################
##       Top-Level        ##
############################

## return food message
special = makeSpecial()

def makeSpecial():
    s = 'To get the lunch and dinner menu.'
    return s

## return proper format to use for getting food menu
special = makeSpecial()

# def eval(input):
#     return getFood(input)
