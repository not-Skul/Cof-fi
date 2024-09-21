import psycopg2
from psycopg2 import Error
from flask import Flask, render_template

try:
    app = Flask(__name__)
    connection = psycopg2.connect(user="postgres",
                                  password="12345678",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    cursor = connection.cursor()
    command = '''SELECT NAME,coffee_price,img_url,location FROM  CAFE'''
    res = cursor.execute(command)
    connection.commit()
    list_of_cafe = cursor.fetchall()

    @app.route("/")
    def phone_home():
        return render_template("hello.html",res = list_of_cafe)


except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")



