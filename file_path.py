# Get file path 
import os
import sys

## Need to be able to customize JPG file url 

# User upload the photo - Insert into HTML 
# request.form.file — Get the file information and save using os.paht.join and display image by finding from the path 
#SQL has binary blob type and can insert into a blob format 
# Store as binary large ojbect and find most recent saved image 
# os.path — Navigate exactly where you want to go 

 
if len(sys.argv) < 2:
    print("Please provide a file name as an argument.")
else:
    # Get the filename provided as an argument
    filename = sys.argv[1]

    # Check if the file exists
    if os.path.exists(filename):
        # Get the absolute path of the file
        file_path = os.path.abspath(filename)
        print(f"The path of '{filename}' is: {file_path}")
    else:
        print(f"The file '{filename}' does not exist.")

