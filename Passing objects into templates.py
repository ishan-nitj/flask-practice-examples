from flask import Flask,render_template
app=Flask(__name__) 

@app.route('/')  
def home():
    return render_template("home.html")

@app.route('/shopping')  
def shopping():
    food=['Burger','Pizza','Apple Pie']
    return render_template("shopping.html",food=food)

if __name__=="__main__": 
    app.run(debug=True)
    

    
