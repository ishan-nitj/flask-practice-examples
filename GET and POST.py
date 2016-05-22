from flask import Flask,request
#Most of the times GET method is used but when we are submitting forms POST method is used.
app=Flask(__name__) 

@app.route('/')  
def index():
    return "Method used is %s"%request.method

if __name__=="__main__": 
    app.run(debug=True)

    
