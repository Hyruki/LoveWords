from flask import Flask, render_template, request, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

def islogin() -> bool:
    user = session.get('user')
    password = session.get('password')

    if user == None or password == None:
        return False
    else:

        hashpass = getRowDB(f"SELECT hashpassword FROM users WHERE user='{user}'")[0][0]

        if hashpass == password:
            return True
        else:
            return False

# Templating MODS
def modern_template(dir : str, *arg, **kwargs) -> None:
    is_login = islogin()
    
    return render_template(dir,is_login=is_login, *arg, **kwargs)

def admin_template(dir : str, *arg, **kwargs) -> None:
    return render_template(dir, *arg, **kwargs)

def getRowDB(request : str) -> list:
    con = sqlite3.connect('data.db')
    c = con.cursor()

    c.execute(request)

    return c.fetchall()

def setRowDB(request : str) -> str:
    con = sqlite3.connect('data.db')
    c = con.cursor()

    c.execute(request)

    c.close()
