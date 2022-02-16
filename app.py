from flask import Flask, g
import sqlite3


database = "blog.db"
secret_key = "pao_de_queijo"


app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(database)


@app.before_request
def beforeRequest():
    g.db = connect_db()


@app.teardown_request
def endRequest(exc):
    g.db.close()


@app.route('/')
def show_posts():
    sql = "SELECT title, text FROM inputs ORDER BY id DESC"
    cur = g.db.execute(sql)
    inputs = []
    for title, text in cur.fetchall():
        inputs.append({"title": title, "text": text})
    return render_templates("showInputs.html", posts=inputs)


if __name__ == '__main__':
    app.run()

"""
Teacher Repository: https://github.com/feulo-ocean/aula_python_web
"""
