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
        
def isadmin() -> bool:
    user = session.get('user')
    password = session.get('password')

    if user == None or password == None:
        return False
    else:

        admincheck = getRowDB(f"SELECT admin FROM users WHERE user='{user}' and hashpassword='{password}'")[0][0]

        if admincheck == 1:
            return True
        else:
            return False


# Templating MODS
def modern_template(dir : str, *arg, **kwargs) -> None:
    try:
        is_login = islogin()

        return render_template(dir,is_login=is_login, *arg, **kwargs)
    except Exception as e:
        print(e)

def admin_template(dir : str, *arg, **kwargs) -> None:
    try:
        if isadmin():
            return render_template(dir, *arg, **kwargs)
        else:
            return redirect('/')
    except Exception as e:
        print(e)



# SQL MODS
def getRowDB(request : str) -> list:
    con = sqlite3.connect('data.db')
    c = con.cursor()

    c.execute(request)

    result = c.fetchall()

    c.close()

    return result

def setRowDB(request : str) -> None:
    con = sqlite3.connect('data.db')
    c = con.cursor()

    c.execute(request)

    con.commit()

    con.close()


def getHeaderDB(table_name : str) -> list:
    con = sqlite3.connect('data.db')
    c = con.cursor()

    c.execute(f"PRAGMA table_info({table_name});")

    result = c.fetchall()

    c.close()

    return result
