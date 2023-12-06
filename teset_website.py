from Flask import request, Flask, flash, redirect, render_template, request, session

# Configure application 
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

## NOtE: submit_image in request.files is the name of the file input field with name attribute as file 

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    image = flask.request.files['submit_image']
    image.save('static/file.jpg')
    caption = greedySearch((encode('static/file.jpg').reshape((1, 2048))))
    
    return render_template('index.html', prediction = caption)

## To save a drawing in tkinter 
def save_drawing():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path: