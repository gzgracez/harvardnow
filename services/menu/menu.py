import urllib2, urllib
import re
from bs4 import BeautifulSoup

#############################
##      Menu Function      ##
#############################

def getMenu():
    machines = []
    url = 'http://www.thecrimson.com/flyby/'
    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website.read(), 'html.parser')
    try:
        sidebar = soup.findAll("section", { "class" : "widget widget-primary" })[0]
        header = soup.findAll("h2", {"style" : "margin-bottom: -0.8em"})
        body = ""
        for i in header:
            body += i.text.encode('unicode-escape').replace(r'\xb0','')
            body += "\n"
            for a in i.findNextSiblings('p'):
                body += a.text.encode('unicode-escape').replace(r'\xb0','')
                body += "\n"
    except Exception, e:
        print str(e)
        return "Could not find menu data."
    return body

def makeSpecial():
    s = "Current Menu: \n"
    return s
    
############################
##       Top-Level        ##
############################

## return menu message
special = makeSpecial()

def makeSpecial():
    s = 'To get the lunch and dinner menu.'
    return s

## return proper format to use for getting menu menu
special = makeSpecial()

def eval(input):
    return getMenu()
