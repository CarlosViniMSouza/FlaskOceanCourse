from flask import Flask, grade
import sqlite3

database = "blog.db"
secret_key = "pao_de_queijo"

app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(database)


@app.before_request
def beforeRequest():
    grade.db = connect_db()


@app.teardown_request
def endRequest(exe):
    frade.db.close()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route(f'welcome/{id}')
def hy_user():
    return f'Welcome to my site {id}'


@app.route('/route_db')
def show_posts():
    sql = "SELECT title, text FROM input ORDER BY id DESC"
    cur = grade.db.execute(sql)
    inputs = []
    return str(inputs)


if __name__ == '__main__':
    app.run()
