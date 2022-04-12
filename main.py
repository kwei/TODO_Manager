from asyncio import tasks
from flask import Flask, render_template, g, request, redirect, url_for, session
import os
from model.SQL import SQL
from config import Config
from module.DB_Controller_Member import DB_Controller_Member
from module.DB_Controller_Task import DB_Controller_Task

app = Flask(__name__, 
            static_url_path="",
            static_folder=os.getcwd()+"/templates/static",
            template_folder=os.getcwd()+"/templates")

app.secret_key = "TeamT5 Interview Test"

sql = SQL()
db_controller_member = DB_Controller_Member(sql)
db_controller_task = DB_Controller_Task(sql)

@app.route('/home')
def home():
    msg = ''
    isLogged = False
    if "isAuth" in session:
        msg = "Have been logged."
        isLogged = True
        return render_template('main.html', msg = msg, isLogged = isLogged, userName = session["userName"])
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    isLogged = False
    if request.method == "POST" and "userName" in request.form and "password" in request.form:
        userName = request.form["userName"]
        password = request.form["password"]
        
        if not db_controller_member.isExist(userName, password):
            msg = "Incorrect userName or password."
        else:
            account = db_controller_member.fetch(userName, password)
            session["isAuth"] = True
            session['id'] = account['id']
            session['userName'] = account['userName']
            isLogged = True
            msg = "log-in successfully."

            return redirect(url_for('home'))

    return render_template('login.html', msg = msg, isLogged = isLogged)

@app.route('/logout')
def logout():
    session.pop("isAuth", None)
    session.pop("id", None)
    session.pop("userName", None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    isRegistered = False
    if request.method == "POST" and "userName" in request.form and "password" in request.form and "password-check" in request.form:
        userName = request.form["userName"]
        password = request.form["password"]
        password_check = request.form["password-check"]
        isRegistered = True

        if db_controller_member.isExist(userName, password):
            msg = "Account already exists."
        elif not userName or not password or not password_check:
            msg = "Please complete the entire form."
        elif password != password_check:
            msg = "The password-check should be equal to the password."
        else:
            db_controller_member.insert(userName, password)
            msg = "Registered successfully."
    
    elif request.method == "POST":
        msg = "Please complete the entire form."

    return render_template('register.html', msg = msg, isRegistered = isRegistered)




if __name__ == "__main__":
    config = Config()
    schemas = dict()
    table_names=["members", "tasks"]
    schemas["members"] = "CREATE TABLE members (\
                            id INTEGER PRIMARY KEY AUTOINCREMENT,\
                            userName varchar(255) NOT NULL,\
                            userPassword varchar(255) NOT NULL,\
                            tasks varchar(255));"
    schemas["tasks"] = "CREATE TABLE tasks (\
                            id INTEGER PRIMARY KEY AUTOINCREMENT,\
                            taskIndex int NOT NULL,\
                            title varchar(255) NOT NULL,\
                            content varchar(255) NOT NULL,\
                            createTime time NOT NULL,\
                            createDate date NOT NULL);"

    sql.db_name = config.db_name
    sql.table_names = table_names
    sql.schemas = schemas

    sql.init_db()

    app.run()