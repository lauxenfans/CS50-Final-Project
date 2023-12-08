# CS50-Final-Project
A “design document” for your project in the form of a Markdown file called DESIGN.md that discusses, technically, how you implemented your project and why you made the design decisions you did. Your design document should be at least several paragraphs in length. Whereas your documentation is meant to be a user’s manual, consider your design document your opportunity to give the staff a technical tour of your project underneath its hood.

# WriteRight - DESIGN.md
WriteRight - A Whiteboard that Reverse Image Searches
Catherine Li, Louis Auxenfans, Sava Thurber

For this project, our goal was to create a website that has a whiteboard feature through which a user can draw using a variety of colors, and be able to take those images and import them into Google Reverse Image Search, outputting images that matched. 

We divided up the project into three separate portions: the whiteboard program itself (lfg.py), the website which the whiteboard was integrated into(app.py and helpers.py), and the program that took the image from the whiteboard and inserted it into Google's Reverse Image Search Engine (reverse_search.py). We decided to split up the project to have each of the three portions work separately, and then worked to combine all of the parts together. Outlined below are the design choices for each of the three portions.

*Note: Due to the limitations of CS50, we were able to get all 3 portions of the code to work separately, but were unable to get all 3 portions of the website to link together. Below is the design process for how each of the individual portion of the code work. We will include notes in this format with the linking portions that we had hoped to include, but were unable to implement due to the limiations of this project.*

Programs Used:
    - Python
    - Flask
    - JavaScript
    - HTML
    - CSS
    - SQL

**Whiteboard Implementation - Sava, lfg.py**
    For our whiteboard, we decided to primarily utilize the Tkinter library to create a window on which a user can draw via interactions with the canvas widget. We decided on tkinter because it had the smoothest integration with canvas style drawing, which was what we wanted to focus on to create the most functional and representative whiteboard. Additionally, because Tkinter is a python library, this would also make for easier implementation down the road with our website. THe whiteboard uses the tkinter library to create a window on which a user can design and draw via interactions with the canvas widget.

    In the Tkinter library, there are several functions that include drawing (drawing small circles that give the illusion of a continuous line), erasing, ink color and size changing, text display, text size formatting, and random shape generation. Throughout the process, Sava consulted the tkinter documentation to find built-in functions and to help with syntax. After doing so and utilizng certain button presses are bound to events to trigger functions, we were able to create a fully functional whiteboard design that has many additional designs that can be implemented into the design. Certain button presses are bound to events to trigger functions, and are listed next to the functions.

    The list of possible functions are below:
        - Draw: This is the default function on the whiteboard. Hold down your mouse and you will see drawing occuring.
        
        - Color: Change the color of your brush across the whole pallate spectrum. These colors are in RGB.
            - Brush Size: The slider just to the right of this box will adjust the size of the brush with values close to 0 being a very thin brush and large values creating a very wide brush.

        - Erase: When selected, a box on the far right will appear that says "Erase Active" in red text 

        - Text box: This empty box allows you to type text inside which you can use as a brush to see text on your whiteboard screen. Double click your mouse to see it on the screen!
            - Text Size: The slider just to the right of this box will adjust the size of the text with values close to 0 being smaller font size and large values being larger font size.
        
        - Random: When selected, a series of random shapes and lines will appear in varying colors.

        - Clear: This will clear your canvas

        - Save: When the user is done drawing, they have to option to save the drawing, which automatically takes a screenshot of the canvas and saves it in the user's active directory
            - The user then has the option of uploading the saved file into the Reverse Google Image Search as described below.
            **Note that for the sake of demonstration, Sava has hardcoded in his preferred directory as the screenshot_path variable. For a user to specify their own preferred directory, they should add their own file path.**
            *Note: Unfortunately, we have run into issues with the website not running on all computers and the save function not saving the screenshot as an actual png. This makes the implementation for the reverse image search difficult as the file does not save correctly* 

    Throughout the process, Sava consulted the tkinter documentation to find built-in functions and to help with syntax.


**Website Implementation - Catherine, app.py, helpers.py**
    For our website, we decided that we would want to utilize flask and python to create a website that would allow for form submissions and better integration with other libraries and APIs. When creating the website, Catherine decided to base the structure of our project on the code that she had written for her Finance problem set. She decided to utilize a simiilar setup by utilizing "app.py" for all the website routing, "helpers.py" to store additional functions to be referenced later on, a "templates" folder to keep all of the HTML files, a "styles" folder with the CSS implementation, and a "whiteboard.db" database to hold user's login information.
    
    All files except those listed below were based off of the code written for her Finance problem set.

    *app.py* utilized routing within the website to allow for the WriteRight functionality. In order to access the whtieboard functionality, users will first have to register with a secure password (must have at least 7 characters and include special characters ["!", "@", "$", "%", "#", "&"]). Once logged in, then users will be able to see a button that when clicked, will allow for a popup window with the canvas and whiteboard functionality.
    
        - @app.route('/whiteboard')
        This route to the whiteboard creates the popup window. Utilizing the code that Sava wrote above for the whiteboard, I implemented the portion of the code that runs the whiteboard in the "lfg.py" code into the route. This route references functions from the Whiteboard class from "lfg.py", which are implemented into the "helpers.py" program. These function are referenced at the top in imports. After the window is closed, "whiteboard.html" is rendered.

        - @app.route('/')
        This route renders the "index.html" page which has a welcome note to the user!

        - @app.route('/revImageSearch')
        This route renders the "revImageSearch.html" page which has a link to Google's Reverse Image Search page. 
        *Note: Because it is illegal to webscrape off of Google's code, we have decided to link directly to the page here. If we were able to save the image drawn on the whiteboard directly to the user's directory, this would be where we would implement "reverse_search.py" to directly access the image that we drew on the whiteboard, and then generate the images with the best match.*
    
    *helpers.py* is where Catherine wrote all of the helper functions that were used in the app.py route.
        - class Whiteboard:
        The creation of the class and subsequent objects allows for the functions written in Whiteboard to be accessed outside of "helpers.py" and used in the code for "app.py". This is the rest of the code that is a part of the whiteboard implementation from Sava's code above.

    Throughout the process, Catherine consulted the internet to help debug and work through the code.

**Reverse Image Search Implementation - Louis, reverse_search.py**
    For the reverse image search implmentation portion, we decided to utilize SerpAPI, which is an API that allows for images to be reverse searched given a file. When writing this code, Louis decided to try to best replicated reverse Google Image search. Generally, the reverse Google Image search should receive the file directory of an image (if stored locally in the user's files) or the URL of an image (if stored otherwise) and should output several images taken from Google Images that look similar to the input image.
    
    Note that for the purposes of a demonstration (as shown in our video demo) we have hardcoded the URL of an image of an apple, and when the program is run, more images of apples appear from Google Images. Notice that for other image inputs, the user should replace "uploaded_image_url" with the file directory or URL of the image they would like to search.
    
    Additionally, for the sake of demonstration (as seen in our video), we have also hardcoded the API key to make the program run smoother. Make sure to replace the API key in the params dictionary with your own SerpAPI key.
    
    The reverse Google Image search implements SerpAPI to help generate relevant search results given an image input. The output when running "python3 reverse_search.py" will be a series of images with the closest match to the imported image.
