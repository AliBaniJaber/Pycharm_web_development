from flask import Flask , redirect , request ,url_for , render_template ,make_response

app = Flask(__name__)#2


@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    return request


if __name__ == '__main__':
    app.run(debug=True)