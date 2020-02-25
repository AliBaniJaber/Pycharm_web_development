from flask import Flask , redirect , request ,url_for , render_template

 
app = Flask(__name__)#2



@app.route('/')
def fun():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)