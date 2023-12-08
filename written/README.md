# CS50-Final-Project
Documentation for your project in the form of a Markdown file called README.md. This documentation is to be a user’s manual for your project. Though the structure of your documentation is entirely up to you, it should be incredibly clear to the staff how and where, if applicable, to compile, configure, and use your project. Your documentation should be at least several paragraphs in length. It should not be necessary for us to contact you with questions regarding your project after its submission. Hold our hand with this documentation; be sure to answer in your documentation any questions that you think we might have while testing your work.

# WriteRight - README.md
WriteRight - A Whiteboard that uses Google Reverse Image Search
Catherine Li, Louis Auxenfans, Sava Thurber
Link to Youtube Video: https://youtu.be/aMAx3Bsphqs

Hello there! Thank you so much for taking a look at our project. In this writeup, you will find all of the necessary compilation information and usage to get started with using WriteRight. This document should be comprehensive, however, in the case that you run into errors, please contact us via: cbli@college.harvard.edu, sthurber@college.harvard.edu, lauxenfans@college.harvard.edu.

*Note: Due to the limitations of CS50, we were unable to get all 3 portions of the website to link together. However, all 3 portions work individually. Below is the implementation for how the code works right now with some notes about debugging if you run into issues. We have found that results may vary due to different operating systems. If you would like to see each of these programs more in depth and they are not running on your computer, please contact us, and we will be very willing to demonstrate how each portion works. We will denote these potential issues in a similar format to this*

**Compilation**
    To work on our code, you will first have to get your computer up to date with the necessary installations. We decided to utilize the desktop Github and VSCode files. 

    Step 1: Download all our files from the zip folder to your VSCode 
    
    Step 2: Get the necessary libraries and programs downloaded and set up onto your computer.

        First, follow the CS50 video 'Flying the nest: https://youtu.be/vQd_fxzCIs0?si=J0lTphzZIoClXQcB' which will get your computer set up with Python and Flask. 
   
        Second, download the pip module in Python (if your computer doesn't have that already), so you can install the relevant python libraries.
        
        Now, download the relevant Python libraries that we used in our project to make the website. You can install this by running pip install [library_name] in your terminal. For certain libraries, you may need to check if they will run by using sudo apt.

        If that doesn't install the library, try running pip3 install [libray_name] or python -m pip install [library_name]

        Below are the relevant Python Libraries used for our helper functions:
        - Tkinter 
        - PIL
        - Flask_Session
        - werkzeug 
        - CS50
        - pytz 
        - requests 
        - urllib3 
        - uuid
        - serpapi

    Step 3: Make sure that our folder "CS50-Final-Project" is open on your computer. You should see in your directory a series of folders and files as seen below:
        - _pycache_ (automatically generated)
        - flask_session (automatically generated)
        - images
        - other (this has our previous versions and testing files)
        - static
        - templates
        - written
        - app.py
        - helpers.py
        - lfg.py
        - reverse_search.py
        - whiteboard.db
        
    Step 4: Assuming that all of these files are correct, you should be able to type flask run in your terminal, which will yield a link that loads the website. For more insight on how to navigate the website, see the next section "Website Navigation" below. Have fun playing around with the whiteboard!

**Website Navivation**
    Now that you are completely compiled and have run "flask run" in your terminal, you should now be able to see a website with the title of "WriteRight".

    Step 1: To use the website, first click on the Register button on the top right to create an account. Enter a username and create a password and re-confirm that password. This password will necessitate you to utilize at least 7 characters, and a special character from the list: ["!", "@", "$", "%", "#", "&"].

    Step 2: Log into the website using your newly created username and password. You should be automatically redirected to the login page, but if this is not visible, please click the "login" button in the top right.

    Step 3: Once you have sucessfully logged in, a "whiteboard" button should appear in the upper left. Click this to open up a whiteboard window where you can draw!

    Step 4: In the whiteboard window, there are multiple buttons at the top bar of the window  which provide different actionality to interact with the whiteboard as you drag your brush (pen) across the screen. From the left hand side to the right, they include:

        - Draw: This is the default function on the whiteboard. Hold down your mouse and you will see drawing occuring.
        
        - Color: Change the color of your brush across the whole pallate spectrum. These colors are in RGB.
            - Brush Size: The slider just to the right of this box will adjust the size of the brush with values close to 0 being a very thin brush and large values creating a very wide brush.

        - Erase: When selected, a box on the far right will appear that says "Erase Active" in red text 

        - Text box: This empty box allows you to type text inside which you can use as a brush to see text on your whiteboard screen. Double click your mouse to see it on the screen!
            - Text Size: The slider just to the right of this box will adjust the size of the text with values close to 0 being smaller font size and large values being larger font size.
        
        - Random: When selected, a series of random shapes and lines will appear in varying colors.

        - Clear: This will clear your canvas

        - Save: This will save your image as a png to your local directory to be later accessed (CS50-Final-Project in this case). 

*Note: Unfortunately, we have run into issues with the website not running on all computers and the save function not saving the screenshot as an actual png. After talking to many TFs about this, they told us the solution was out of the scope of CS50 as it entails threading and additinal concepts*

*Note: In the case that the website is not yielding your whiteboard canvas, run "python3 lfg.py" in your terminal to see all of the whiteboard functionalities in more detail*

**Reverse Image Search**
    Now that you have drawn your image, it is now time to reverse image search! For any image that you have saved into your computer, you will be able to run reverse_search.py. 

    Step 1: In the variable "uploaded_image_url" set your image by either imputting a URL or access the image in your computer directory.
        - The current URL "https://purepng.com/public/uploads/large/purepng.com-applefoodsweettastyhealthyfruitapple-9815246780899e3jo.png" links to an image of an apple for demonstration purposes.
    
    Step 2: Run "python3 reverse_search.py" in your code terminal.

    Step 3: Enjoy clicking through your matched images!
    

    
