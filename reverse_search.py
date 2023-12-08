# Reverse Image Search 
import requests 
from PIL import Image 
from io import BytesIO
from serpapi import GoogleSearch

#Replace with directory to file of interest to work generally 
uploaded_image_url = "https://purepng.com/public/uploads/large/purepng.com-applefoodsweettastyhealthyfruitapple-9815246780899e3jo.png"

params = {
  "engine": "google_reverse_image",
  "image_url": uploaded_image_url,
  "api_key": "b6da2d59ed058bbd9aed17229429a0e9a9fd3287ace73d54373536b5d8f4de61"
}

search = GoogleSearch(params)
results = search.get_dict()
inline_images = results["inline_images"]

###   Display JPG file  ###
# Will grab url from thumbnail
for image_info in inline_images:
    image_url = image_info.get('original')
    if image_url:
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
    
    #Display the image 
        img.show()

