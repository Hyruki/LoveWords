from flask import Flask, render_template, request, session, redirect
from utils import *
from werkzeug.security import generate_password_hash, check_password_hash

def admin_sys(app):    
    @app.route('/admin')
    def admin_menu():
        return admin_template('jinja/admin/admin.jinja')

    @app.route('/admin/users')
    def admin_users():
        return admin_template('jinja/admin/users/admin_users.jinja')