from flask import Flask, sqlalchemy
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite3'
db = SQLAlchemy(app)



@app.route("/")
def hello_world():
    return "<p>Hello, world!</p>"

@app.route("/products")
def products():
    return "<p>This is products page</p>"

@app.route("/blogs")
def blogs():
    return "<p>This is blogs page</p>"


if __name__ == "__main__":
    app.run(debug=True, port=8000)