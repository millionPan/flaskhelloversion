from flask import Flask

app=Flask(__name__)

@app.route('/a')
def hello():
    return '<h1 style="color:purple;font-size:40px;">hello,World!</h1>'

@app.route('/hello/')
def hello2():
    return 'hello,Worldtoo!'


@app.route('/user/<name>')
def user(name):
    return '<h1>hello,%s!</h1>' % name


if __name__=='__main__':
    app.run(debug=True)