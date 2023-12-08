"""
For Documentation: Get file path 
Will get the file directory of the image you made and return it. Uses os and sys library to get the name of the file you typed in terminal command argument 
""" 

# Import relevant libraries 
import os
import sys

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