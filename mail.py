from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ishan.nitj@gmail.com'
app.config['MAIL_PASSWORD'] = 'willingtodie'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'ishan.nitj@gmail.com', recipients = ['ishan.nitj@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   with app.open_resource("Notes.txt") as fp:
      msg.attach("Notes.txt","txt", fp.read())
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)

