from flask import Flask
from markupsafe import escape
from flask import render_template
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(user="Postgres",
                                  password="12345678",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

cur = conn.cursor()

cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

@app.route("/")
def home():
    return "<h1>This is your First page</h1>"

@app.route("/<name>")
def nya(name):
    return f'hello {escape(name)}'

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html',person=name)