#GET:Sends data in unencrypted form to the server. Most common method.

#POST:Used to send HTML form data to server. Data received by POST method is not cached by server.

from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')  
def home():
    return render_template("home.html")

@app.route('/movie',methods=['GET','POST'])  
def movie():
    if request.method=='POST':
        moviename=request.form['movie']
        return 'You have searched for %s'%moviename
    else:
        moviename=request.args.get('movie')
        return 'You have searched for %s'%moviename

if __name__=="__main__": 
    app.run(debug=True)
    

    
