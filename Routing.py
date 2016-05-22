from flask import Flask

app=Flask(__name__)#Flask constructor takes the name of current module (__name__) as argument.

#URL binding with the function. 
@app.route('/') #whenver we go to this particular page,the value from the following function will be returned.
def index():
    return "This is the homepage"

@app.route('/username/<username>/') #an example of how to use variables within url
def username(username):
    return "<h1>This page contains details about %s</h1>"%username

@app.route('/userid/<int:userid>') #if the variable is other than str, we have to specify the datatype
def userid(userid):
    return "<h1>This page contains details about %s</h1>"%userid

if __name__=="__main__":#we only run if we are calling this file directly
    app.run(debug=True)

#debugging mode:The server will then reload itself if the code changes. It will also provide a useful debugger to track the errors if any, in the application.
