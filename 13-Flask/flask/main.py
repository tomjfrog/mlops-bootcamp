from flask import Flask, render_template

'''
Create an instance of Flask class
which will be the Web Server Gateway Interface (WSGI)
'''
### WSGI Application
app=Flask(__name__)

# Create a route
@app.route("/")
def welcome():
    return "<html><h1>Welcome to the Flask Course</h1></html>"


@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def greet():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True) 




