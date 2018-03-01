from flask import Flask, render_template, request, redirect
from flask import url_for
from users import User
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/homepage',methods={'POST'})
def homepage():
    if request.form.get('login') == 'login':
      with open('users.csv') as fp:
          reader = csv.reader(fp)
          for line in reader:
              if (request.form.get('username') == line[1]) and (request.form.get('password') == line[2]):
                  return render_template('homepage.html',username=line[1])
    if request.form.get('login') == 'register':
        bankid = request.form.get('bankid')
        username = request.form.get('username')
        password = request.form.get('password')
        name = request.form.get('flname')
        designation = request.form.get('designation')
        fp = open('users.csv','a')
        writer = csv.writer(fp)
        writer.writerow([bankid, username, password, name, designation])
        fp.close()
        return render_template('homepage.html',username=username)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
