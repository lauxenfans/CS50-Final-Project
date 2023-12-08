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