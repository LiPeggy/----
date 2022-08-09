from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
#MY SQL在Flask的初始化
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = os.getenv('USER')
app.config["MYSQL_PASSWORD"] = os.getenv('PASSWORD')
app.config["MYSQL_DB"] = "ptwa"

mysql = MySQL(app)

@app.route("/", methods=['POST', 'GET'])
def home():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        if name == "" or email =="" or message == "":
            return render_template('index.html', data=False)
        try:
            cur.execute(
            "INSERT INTO `ptwa`.`ptwa` (`name`, `email`, `message`) VALUES (%s, %s, %s)" , [name,email,message])
            mysql.connection.commit()
            return render_template('index.html', data=True)
        except Exception as e:
            print(e)
            return render_template('index.html', data=False)
    else:
        return render_template('index.html', data=None)

if __name__ == '__main__':
    app.run()