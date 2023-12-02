import cv2
import requests
import numpy as np
import json

# Function to perform reverse image search using Google Custom Search API
def reverse_image_search(image_path, api_key, custom_search_engine_id):
    # Read the image using OpenCV 
    """
    f = open('apple.png', "rb")
    rawImage = f.read()
    f.close()

    # Convert rawImage to Mat 
    pilImage = Image.open(StringIO(rawImage));
    npImage = np.array(pilImage)
    matImage = cv.fromarray(npImage)
    """

    with open('apple.png', 'rb') as infile:
        buf = infile.read()
    #x = np.fromstring(buf, dtype = 'uint8')

    # Decode array into image 
    #img = cv2.imdecode(x, cs2.IMREAD_UNCHANGED)
    
    
    # Convert the image to base64 encoding
    # _, img_encoded = cv2.imencode('.png', img)
    # img_base64 = img_encoded.tobytes()

     
    # Make a POST request to the Google Custom Search API
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={custom_search_engine_id}&searchType=image'
    headers = {'Content-Type': 'application/json'}
    data = {
        "requests": [
            {
                "image": {
                    "content": buf
                }
            }
        ]
    }

    response = requests.get(url, headers=headers, json=json.dumps(data))
    results = response.json()

    return results

# Path to the image you want to perform reverse image search on
image_path = 'apple.png'

# Your Google Custom Search API key and Custom Search Engine ID
api_key = 'AIzaSyC3d59M5694VMl8kLscZpyDVhaYFD569Z8'
custom_search_engine_id = '8097be5676b3248b1'

# Perform reverse image search
search_results = reverse_image_search(image_path, api_key, custom_search_engine_id)

# Process the search results
if 'items' in search_results:
    for item in search_results['items']:
        print("Title:", item.get('title', ''))
        print("Link:", item.get('link', ''))
        print("Image:", item.get('image', {}).get('contextLink', ''))
        print("-----------------------------------")
else:
    print("No search results found.")
