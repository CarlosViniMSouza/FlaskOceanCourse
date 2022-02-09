import sqlite3
import sqlite3

from flask import Flask

database = "blog.db"
secret_key = "pao_de_queijo"

app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(database)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
