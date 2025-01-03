from flask import Flask

'''
Create an instance of Flask class
which will be the Web Server Gateway Interface (WSGI)
'''
### WSGI Application
app=Flask(__name__)

# Create a route
@app.route("/")
def welcome():
    return "Welcome to this Flask course.  It's the best course"

@app.route("/greeting")
def greet():
    return "Good Morning!"



if __name__=="__main__":
    app.run(debug=True) 




