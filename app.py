from flask import Flask, render_template, request, session, redirect
from utils import *
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = 'secret_key'


# Main Menu
@app.route('/', methods=['POST', 'GET'])
def main_page():
    return modern_template('jinja/index.jinja')

# AUTH SYS
# Login Sys
@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == "POST":
        user = request.form.get('user-input', None)
        password = request.form.get('password-input', None)
        
        is_account = getRowDB(f"SELECT hashpassword FROM users WHERE user='{user}'")[0][0]

        print(is_account)

        if is_account != {}:
            if check_password_hash(is_account, password):
                session['user'] = user
                session['password'] = is_account
                return redirect('/')
            else:
                return render_template('jinja/auth/login.jinja', error_mess = True)



    return render_template('jinja/auth/login.jinja', error_mess = False)

@app.route('/logout')
def logout():
    session.pop('user')
    session.pop('password')
    return redirect('/')

app.run(host="0.0.0.0", port="5000", debug=True)