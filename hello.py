from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/hello/')
def hello2():
    return 'hello,Worldtoo!'


@app.route('/user/<name>')
def user(name):
    return render_template('user.html',username=name)


if __name__=='__main__':
    app.run(debug=True)