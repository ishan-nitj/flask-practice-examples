from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')  
def home():
    return render_template("home.html")

@app.route('/userdetails',methods=['GET','POST'])  
def movie():
    if request.method=='POST':
        userdetails=request.form  #here userdetails is a dictionary
        return render_template("userdetails.html",userdetails=userdetails)

if __name__=="__main__": 
    app.run(debug=True)
    

    
