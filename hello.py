from flask import Flask,render_template
from flask import request,flash

app=Flask(__name__)
app.secret_key="itheima"
# 目的：实现一个简单的登录的逻辑处理
# 1.路由需要有get和post两种请求方式  -->需要判断请求方式
# 2.获取请求的参数
# 3.判断参数是否填写&密码是否相同
# 4.如果判断都没有问题，就返回一个success
# 给模板传递消息flash-->需要对消息加密，因此需要设置secret。key：模板中需要遍历消息
@app.route('/',methods=['GET','POST'])
def hello():
    #request:请求对象--> 获取请求方式、数据

    # 1.判断请求方式
    if request.method=='POST':

        # 2.获取请求的参数
        username=request.form.get('username')
        password=request.form.get('password')
        password2=request.form.get('password2')
        print(password)

        # 3.判断参数是否填写&密码是否相同
        if not all([username,password,password2]):
            flash('参数不完整')
        elif password !=password2:
            flash('密码不一致')
        else :
            return 'success'
        # fruits=['apple','pear','grapes']
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