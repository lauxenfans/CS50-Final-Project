import pysftp as sftp 

import urllib
from urllib.request import urlopen 
from http.cookiejar import CookieJar

import time 

cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor[cj])