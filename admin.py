from flask import Flask, render_template, request, session, redirect
from utils import *
from werkzeug.security import generate_password_hash, check_password_hash

def admin_sys(app):    
    @app.route('/admin')
    def admin_menu():
        return admin_template('html/admin/admin.html')

    # =====================================
    # =============== USERs ===============
    # =====================================
    @app.route('/admin/users', methods=['GET', 'POST'])
    def admin_users():
        return admin_template('html/admin/users/admin_users.html', headers=getHeaderDB('users'), rows=getRowDB('SELECT * FROM users'))
    
    @app.route('/admin/users/<id>', methods=['GET', 'POST'])
    def admin_users_modification(id):
        if request.method == 'POST':
            # '' for check and None for not check
            actual_user = session.get('user')
            actual_password = session.get('password')
            isadmin = 0
            username = request.form.get('username_input')
            hashpass = request.form.get('password_input')
            id_input = request.form.get('id_input')

            print("vbqzdvghzqvhd : ",request.form.get('admin_check'))
            if request.form.get('admin_check') == 'on':
                isadmin = 1



            if actual_user == getRowDB(f"SELECT user FROM users WHERE id={id}")[0][0]:
                session['user'] = username
                session['password'] = actual_password
                print(session.get('user'))




            print(request.form.get('id_input'), username, hashpass, type(id))
            setRowDB(f"""UPDATE users SET id={id_input},user="{username}",hashpassword="{hashpass}",admin={isadmin} WHERE id={id}""", 'users')
            return redirect('/admin/users')
         
        return admin_template('html/admin/users/admin_users_modify.html', user_data=getRowDB(f'SELECT * FROM users WHERE id={id}'))
    
    @app.route('/admin/users/add', methods=['GET', 'POST'])
    def admin_user_add():

        if request.method == "POST":
            username = request.form.get('username_input')
            passw = request.form.get('password_input')
            hashpass = generate_password_hash(passw)

            isadmin = 0

            if request.form.get('admin_check') == '':
                isadmin = 1
            
            setRowDB(f"""INSERT INTO users VALUES(null, "{username}", "{hashpass}", {isadmin})""", 'users')

            return redirect('/admin/users')

            
        return admin_template('html/admin/users/admin_users_add.html')
    
    @app.route('/admin/users/delete/<id>', methods=['GET', 'POST'])
    def admin_user_delete(id):
        setRowDB(f"DELETE FROM users WHERE id={id}", 'users')
        return redirect('/admin/users')
    

    # =====================================
    # ============= CATEGORYs =============
    # =====================================

    @app.route('/admin/category')
    def admin_category():
        return admin_template('html/admin/category/admin_category.html', headers=getHeaderDB('categorys'), rows=getRowDB('SELECT * FROM categorys'))
    
    @app.route('/admin/category/<id>', methods=['GET', 'POST'])
    def admin_category_modify(id):
        
        category_data = getRowDB(f"SELECT category,id FROM categorys WHERE id={id}")

        print(category_data)

        if request.method == "POST":
            category_name = request.form.get('category_name')
            category_id = request.form.get('category_id')

            setRowDB(f"""UPDATE categorys SET id={category_id},category="{category_name}" WHERE id={id}""", "categorys")


            return redirect('/admin/category')

        return admin_template('html/admin/category/admin_category_modify.html', category_data=category_data)

    @app.route('/admin/category/add', methods=['GET', 'POST'])
    def admin_category_add():

        if request.method == "POST":
            category_name = request.form.get('category_name')


            setRowDB(f"""INSERT INTO categorys VALUES(null,"{category_name}")""", "categorys")

            return redirect('/admin/category')

        return admin_template('html/admin/category/admin_category_add.html')

    @app.route('/admin/category/delete/<id>', methods=['GET', 'POST'])
    def admin_category_remove(id):

        setRowDB(f"DELETE FROM categorys WHERE id={id}", "categorys")

        return redirect('/admin/category')
    
    # =====================================
    # ============  MESSAGES  =============
    # =====================================

    @app.route('/admin/message')
    def admin_message():
        return admin_template('html/admin/message/admin_message.html', headers=getHeaderDB('messages'), rows=getRowDB('SELECT * FROM messages ORDER BY category_id') )

    @app.route('/admin/message/<id>', methods=['GET', 'POST'])
    def admin_message_modify(id):

        if request.method == "POST":
            title = request.form.get('message_title')
            content = request.form.get('message_content')
            category_id = request.form.get('category_select')
            message_id = request.form.get('message_id')

            setRowDB(f"""UPDATE messages SET id={message_id},title="{title}",content="{content}",category_id={category_id} WHERE id={id}""", 'messages')

            return redirect('/admin/message')

        return admin_template('html/admin/message/admin_message_modify.html', messages_data=getRowDB(f"SELECT title,content,category_id,id FROM messages WHERE id={id}"), categorys=getRowDB(f"SELECT * FROM categorys"))


    @app.route('/admin/message/add', methods=['GET', 'POST'])
    def admin_message_add():

        if request.method == "POST":
            title = request.form.get('message_title')
            content = request.form.get('message_content')
            category_id = request.form.get('category_select')

            setRowDB(f"""INSERT INTO messages VALUES(null,"{title}","{content}",{category_id})""", 'messages')

            return redirect('/admin/message')

        return admin_template('html/admin/message/admin_message_add.html', categorys=getRowDB(f"SELECT * FROM categorys"))

    @app.route('/admin/message/delete/<id>', methods=['GET', 'POST'])
    def admin_message_delete(id):
        setRowDB(f"DELETE FROM messages WHERE id={id}", 'messages')

        return redirect('/admin/message')
    