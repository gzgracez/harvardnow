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
    sidebar = soup.findAll("section", { "class" : "widget widget-primary" })[0]
    print sidebar
    # machine = washer_div.next_sibling
    # if machinetype == 'washer':
    #     while 'id' not in machine.attrs or machine['id'] != 'dryer':
    #         machines.append({'lr': roomid,
    #          'id': machine.a['id'],
    #          'name': `(machine.a.text)`.split('\\xa0')[0][2:],
    #          'time': machine.a.p.text})
    #         machine = machine.next_sibling
    # else:
    #     while machine and machine.name == 'li':
    #         machines.append({'lr': roomid,
    #          'id': machine.a['id'],
    #          'name': `(machine.a.text)`.split('\\xa0')[0][2:],
    #          'time': machine.a.p.text})
    #         machine = machine.next_sibling
    # return machines

def makeSpecial():
    s = "Current Food: \n"
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
