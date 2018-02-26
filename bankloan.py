from flask import Flask, render_template
from user import user

app = Flask(__name__)


@app.route('/')
def home():
    render_template('home.html')

@app.route('/loggedin')
def logged_in():
    if form.password == 

if __name__ == '__main__':
    app.run(debug=True)
