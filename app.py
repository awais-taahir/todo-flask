from flask import Flask


app = Flask(__name__)



@app.route("/")
def hello_world():
    return "<p>Hello, oorld!</p>"

@app.route("/products")
def products():
    return "<p>This is products page</p>"

@app.route("/blogs")
def blogs():
    return "<p>This is blogs page</p>"


if __name__ == "__main__":
    app.run(debug=True, port=8000)