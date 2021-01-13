import base64
import ssl
import sys
import json
import getpass
import requests
import urllib3
import operator
import pprint
import simplejson as json
import sqlite3
from sqlite3 import Error

con = sqlite3.connect('ise-company1.db3')

def sql_insert(con, comp1):
    cursorObj = con.cursor()
    cursorObj.execute('insert into company_name(company) values (?)', ([comp1]))
    con.commit()


def sql_update(con, comp2, comp3):
    cursorObj = con.cursor()
    cursorObj.execute('update company_name SET name = ? where name is NULL', ([comp2]))
    cursorObj.execute('update company_name SET ID1 = ? where ID1 is NULL', ([comp3]))
    con.commit()

a1 = []
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
t = "page="
url = "https://<ISE IP ADDRESS>:9060/ers/config/guestuser?size=100&sortdsc=name&"

for i in range(1, 7):
    username = []
    ids = []
    b = str(i)
    m = url + t + str(b)
    payload = {}
    headers = {'Accept': 'application/json',    'cache-control': "no-cache"}
    result = requests.request("GET", m, headers=headers, data=payload, verify=False, auth=('<ISE_ERS_USERNAME>', '<ISE_ERS_PASSWORD>')).json()
    total = result['SearchResult']['total']
    companies = []
    xx = []
    print(total)
################TO GET USERNAME & ID & COMPANY##################################
    for k in range(0, total):
        z = result['SearchResult']['resources'][k]['name']
        comp2 = z
        xx.append(z)
        y = result['SearchResult']['resources'][k]['id']
        xx.append(y)
        comp3 = y
        url2 = "https://<ISE IP ADDRESS>:9060/ers/config/guestuser/"
        n1 = url2 + y
        payload = {}
        headers = {'Accept': 'application/json', 'cache-control': "no-cache"}
        r2 = requests.request("GET", n1, headers=headers, data=payload, verify=False, auth=('<ISE_ERS_USERNAME>', '<ISE_ERS_PASSWORD>')).json()
        b1 = str(r2["GuestUser"]["guestInfo"]["company"])
        xx.append(b1)
        comp1 = b1
        xx.clear()
        sql_insert(con, comp1)
        sql_update(con, comp2, comp3)
#        print(b1)
#    print(k)
print("done")


