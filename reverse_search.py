
# Reverse Image Search 
import requests 
from PIL import Image 
from io import BytesIO
from serpapi import GoogleSearch

## Need to be able to customize JPG file url 

# User upload the photo - Insert into HTML 
# request.form.file — Get the file information and save using os.paht.join and display image by finding from the path 
#SQL has binary blob type and can insert into a blob format 
# Store as binary large ojbect and find most recent saved image 
# os.path — Navigate exactly where you want to go 

 


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

