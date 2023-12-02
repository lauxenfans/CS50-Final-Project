"""

from serpapi import *

params = {
  "engine": "google_reverse_image",
  "image_url": "https://purepng.com/photo/5928/apple",
  "api_key": "b6da2d59ed058bbd9aed17229429a0e9a9fd3287ace73d54373536b5d8f4de61"
}

search = GoogleSearch(params)
results = search.get_dict()
inline_images = results["inline_images"]
"""

import requests 
PARAMS = {'api_key':'b6da2d59ed058bbd9aed17229429a0e9a9fd3287ace73d54373536b5d8f4de61'}
r = requests.get(url = 'https://serpapi.com/search.json?engine=google_reverse_image&image_url=https://i.imgur.com/5bGzZi7.jpg', params = PARAMS)

data = r.json()
print(data)


## Customize image jpg file 