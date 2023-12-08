# CS50-Final-Project
A “design document” for your project in the form of a Markdown file called DESIGN.md that discusses, technically, how you implemented your project and why you made the design decisions you did. Your design document should be at least several paragraphs in length. Whereas your documentation is meant to be a user’s manual, consider your design document your opportunity to give the staff a technical tour of your project underneath its hood.

# WriteRight - DESIGN.md
WriteRight - A Whiteboard that Reverse Image Searches
Catherine Li, Louis Auxenfans, Sava Thurber

For this project, our goal was to create a website that has a whiteboard feature through which a user can draw using a variety of colors, and be able to take those images and import them into Google Reverse Image Search, outputting images that matched. 

We had a couple different steps that we took for this project, mainly dividing up the project into three separate portions. We had the whiteboard program itself, the website which the whiteboard was integrated into, and the program that took the image from the whiteboard and inserted it into Google's Reverse Image Search Engine. We decided to split up the project to have each of the three portions work separately, and then work to combine all of the parts together. Outlined below are the design choices for each of the three portions.


Whiteboard Implementation
    For our whiteboard, we decided to primarily utilize the Tkinter library to create a window on which a user can draw via interactions with the canvas widget. We decided on tkinter because it had the smoothest integration with canvas style drawing, which was what we wanted to focus on to create the most functional and representative whiteboard. Additionally, because Tkinter is a python library, this would also make for easier implementation down the road with our website. 

    In the Tkinter library, there are several functions that include drawing (drawing small circles that give the illusion of a continuous line), erasing, ink color and size changing, text display, text size formatting, and random shape generation. Throughout the process, Sava consulted the tkinter documentation to find built-in functions and to help with syntax. After doing so and utilizng certain button presses are bound to events to trigger functions, we were able to create a fully functional whiteboard design that has many additional designs that can be implemented into the design.


- when the user is done drawing, they have to option to save the drawing, which automatically takes a screenshot of the canvas and saves it in the user's active directory
- the user has the option of uploading the saved file into google images to get returned the first few real-life pictures that look like what they drew.

Website Implementation
    For our website, we decided that we would want to utilize flask and python to create a website that would allow for form submissions and better integration with other libraries and APIs. We decided to base the structure of our project on the Finance problem set, but with many changes to the routing and HTML pages from there. In our website, WriteRight, when you first click on the page, you will be faced with a series of 

Reverse Image Search
