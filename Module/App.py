from flask import Flask , redirect , request ,url_for , render_template

app = Flask(__name__,instance_relative_config=True)#2

@app.route('/ww')
def fun():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)