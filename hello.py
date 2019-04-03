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


# 自定义错误页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500



if __name__=='__main__':
    app.run(debug=True)