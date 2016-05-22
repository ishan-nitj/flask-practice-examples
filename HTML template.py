#Make 2 folders:
#1)template :for storing html files
#2)static :for storing files that donot change like css files

from flask import Flask,render_template
app=Flask(__name__) 

@app.route('/')  
def home():
    return render_template("home.html")

@app.route('/user/<username>')  
def user(username):
    return render_template("user1.html",name=username) #Here name is passed to html document
#Make sure to put {{name}} in html document wherever you want the username to be dispalyed in the html document

if __name__=="__main__": 
    app.run(debug=True)
    

    
