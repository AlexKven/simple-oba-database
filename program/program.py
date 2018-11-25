#!/usr/bin/python
# Hello World
from keys import *
import httplib
conn = httplib.HTTPConnection('api.pugetsound.org')
conn.request("HEAD", '/api/where/arrivals-and-departures-for-stop/1_52800.xml?key=' + GetObaKey())

res = conn.getresponse()
print res.status, res.reason
