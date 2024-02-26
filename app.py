from flask import Flask, render_template, request, redirect
"""from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import check_password_hash
"""
app = Flask(__name__)
"""app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Submit(db.Model):
    username = db.Column(db.String(25), unique= True, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    author = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    file = db.Column(db.String, nullable=False)
    remark = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return '<Submit %r>' % self.username

class Login(db.Model):
    username = db.Column(db.String(200), unique= True, primary_key= True)
    password = db.Column(db.String(200), nullable=False)
       
    def __repr__(self):
        return '<Login %r>' % self.username


class SignUp(db.Model):
    fname = db.Column(db.String(200), nullable=False)
    lname = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(200), unique= True, primary_key= True)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return '<SignUp %r>' % self.username
""" 



        
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

""" @app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    try:
        username = request.form['username']
        date_created= request.form['date']
        author = request.form['author']
        title = request.form['title']
        file = request.form['file']
        remark = request.form['remark']
    
        user = Submit(username=username, date_created=date_created, author=author, title=title, file=file, remark=remark)
        db.session.add(user)
        db.session.commit()
        
        
    except Exception as e:
        print (e)
        
        return "There was an Error Submitting your file", 500 
    
@app.route('/SignIn', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = SignUp.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            return render_template('index.html')
        else:
            return 'Invalid username or password'
    else:
        return render_template('login.html')

@app.route('/SignUp', methods=['POST'])
def signup():
    try:
        user = SignUp(
            fname = request.form['fname'],
            lname = request.form['lname'],
            gender=request.form['gender'],
            username = request.form['username'],
            email = request.form['email'],
            password = request.form['password']
        )
        
        db.session.add(user)
        db.session.commit()
        
    
    except Exception as e:
        print (e)
        
        return "There was an Error SignUp", 500 

"""

def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Implement validation and sanitization logic here
        # to ensure data integrity and prevent security vulnerabilities

        # Replace these placeholder values with your actual email configuration
        sender_email = "aaintergrated@gmail.com"
        receiver_email = "aaintegrated@outlook.com"
        subject = f"Contact Form Submission from {name}"
        body = f"{name} ({email}) sent you a message:\n\n{message}"

        # Use a secure email sending library like smtplib with proper authentication
        # to send the email (code not provided due to security concerns)

        return "Thank you for your message!"
    else:
        # Display the contact form
        return

if __name__ == "__main__":
   """ db.create_all() 
   """
   app.run(debug=True)
    
    
# app.run(host='localhost', port=5000)
