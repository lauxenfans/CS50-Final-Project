# CS50-Final-Project
A “design document” for your project in the form of a Markdown file called DESIGN.md that discusses, technically, how you implemented your project and why you made the design decisions you did. Your design document should be at least several paragraphs in length. Whereas your documentation is meant to be a user’s manual, consider your design document your opportunity to give the staff a technical tour of your project underneath its hood.

# WriteRight - DESIGN.md
WriteRight - A Whiteboard that Reverse Image Searches
Catherine Li, Louis Auxenfans, Sava Thurber

- whiteboard primarily uses the tkinter library to create a window on which a user can draw via interactions with the canvas widget. 
- several functions include drawing (drawing small circles that give the illusion of a continuous line), erasing, ink color and size changing, text display, text size formatting, and random shape generation. Throughout the process, Sava consulted the tkinter documentation to find built-in functions and to help with syntax. Certain button presses are bound to events to trigger functions.
- when the user is done drawing, they have to option to save the drawing, which automatically takes a screenshot of the canvas and saves it in the user's active directory
- the user has the option of uploading the saved file into google images to get returned the first few real-life pictures that look like what they drew.