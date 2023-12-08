from flask import Flask, request, jsonify, render_template
from google_images_search import GoogleImagesSearch
import base64

app = Flask(__name__)

# Initialize GoogleImagesSearch with your API credentials
gis = GoogleImagesSearch('AIzaSyC3d59M5694VMl8kLscZpyDVhaYFD569Z8', '8097be5676b3248b1')

def validate_params(cx, api_key, search_type, num, start, safe):
    # Check if all required parameters are provided
    if cx is None or api_key is None or search_type is None or num is None or start is None or safe is None:
        return False

    # Check parameter types and values
    if not isinstance(cx, str) or not isinstance(api_key, str) \
            or not isinstance(search_type, str) or not isinstance(num, int) \
            or not isinstance(start, int) or not isinstance(safe, str):
        return False

    # Check specific parameter values (customize as needed)
    if search_type != 'image' or safe not in ['high', 'medium', 'off']:
        return False

    return True


# HTML form for file upload
@app.route('/')
def index():
    return render_template('index.html')

# Handle file upload and perform reverse image search
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Read the image file and encode it to base64
    image_content = file.read()
    image_base64 = base64.b64encode(image_content).decode('utf-8')

    # Check parameters
    # Get the content of the file and encode it to base64
    image_content = file.read()
    image_base64 = base64.b64encode(image_content).decode('utf-8')

    # Check parameters
    cx = 'AIzaSyC3d59M5694VMl8kLscZpyDVhaYFD569Z8'
    api_key = '8097be5676b3248b1'
    search_type = 'image'
    num = 1  # Number of results
    start = 1  # Starting index for results
    safe = 'off'  # Safe search option
    
    if validate_params(cx, api_key, search_type, num, start, safe):
        # Perform Google reverse image search with correct parameters
        gis.search({
            'cx': cx,
            'q': image_base64,
            'num': num,
            'start': start,
            'searchType': search_type,
            'safe': safe,
            'key': api_key
        })

        results = gis.results()
        search_url = results[0].url if results else None
        return jsonify({'searchUrl': search_url})
    else:
        return jsonify({'error': 'Invalid parameters. Check your values and formats.'})

        """ 
        # Perform Google reverse image search
        gis.search({'imgUrl': file.read()})
        results = gis.results()
        search_url = results[0].url if results else None

        return jsonify({'searchUrl': search_url})
    """

if __name__ == '__main__':
    app.run(debug=True)

    