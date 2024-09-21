import psycopg2
from psycopg2 import Error
from flask import Flask, render_template, url_for

try:
    app = Flask(__name__)
    connection = psycopg2.connect(user="postgres",
                                  password="12345678",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    cursor = connection.cursor()
    print('entered')
    command = '''SELECT model FROM  mobile'''
    res = cursor.execute(command)
    connection.commit()
    phone1 = cursor.fetchall()

    @app.route("/")
    def phone_home():
        img = "https://cdn.pixabay.com/photo/2023/08/18/15/02/dog-8198719_640.jpg"
        return render_template("hello.html",var1 = phone1,photo=img)


except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")



