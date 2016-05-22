#Here we have mapped two urls to same page. The content of the page will be dependent on the url. Note that if we have to include non html content on our
#page we have to use {% %}.

from flask import Flask,render_template
app=Flask(__name__) 

@app.route('/')
@app.route('/user/<username>')  
def user(username=None):#setting it default to None
    return render_template("user.html",name=username)  

if __name__=="__main__": 
    app.run(debug=True)
    

    
