from flask import Flask, render_template, request, session, redirect
from utils import *
from werkzeug.security import generate_password_hash, check_password_hash

def admin_sys(app):    
    @app.route('/admin')
    def admin_menu():
        return admin_template('jinja/admin/admin.jinja')

    @app.route('/admin/users', methods=['GET', 'POST'])
    def admin_users():
        return admin_template('jinja/admin/users/admin_users.jinja', headers=getHeaderDB('users'), rows=getRowDB('SELECT * FROM users'))
    
    @app.route('/admin/users/<id>', methods=['GET', 'POST'])
    def admin_users_modification(id):
        if request.method == 'POST':
            # '' for check and None for not check
            actual_user = session.get('user')
            actual_password = session.get('password')
            isadmin = 0
            username = request.form.get('username_input')
            hashpass = request.form.get('password_input')

            print("vbqzdvghzqvhd : ",request.form.get('admin_check'))
            if request.form.get('admin_check') == '':
                isadmin = 1

            if actual_user == getRowDB(f"SELECT user FROM users WHERE id={id}")[0][0]:
                session['user'] = username
                session['password'] = actual_password
                print(session.get('user'))


            print(request.form.get('id_user'), username, hashpass, type(id))
            setRowDB(f"UPDATE users SET user='{username}',hashpassword='{hashpass}',admin={isadmin} WHERE id={id}")
            return redirect('/admin/users')
         
        return admin_template('jinja/admin/users/admin_users_modify.jinja', user_data=getRowDB(f'SELECT * FROM users WHERE id={id}'))
    
    @app.route('/admin/users/add', methods=['GET', 'POST'])
    def admin_user_add():

        if request.method == "POST":
            username = request.form.get('username_input')
            passw = request.form.get('password_input')
            hashpass = generate_password_hash(passw)

            isadmin = 0

            if request.form.get('admin_check') == '':
                isadmin = 1
            
            setRowDB(f"INSERT INTO users VALUES(null, '{username}', '{hashpass}', {isadmin})")

            return redirect('/admin/users')

            
        return admin_template('jinja/admin/users/admin_users_add.jinja')
    
    @app.route('/admin/users/delete/<id>', methods=['GET', 'POST'])
    def admin_user_delete(id):
        setRowDB(f"DELETE FROM users WHERE id={id}")
        return redirect('/admin/users')
