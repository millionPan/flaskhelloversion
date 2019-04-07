from flask import Flask,render_template
from flask import request,flash
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo

# 数据库
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)


# 配置数据库的地址
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:6060@127.0.0.1:3306/hello_sql'
#跟踪数据库的修改-不建议开启 未来的版本中会移除
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key="itheima"

db=SQLAlchemy(app)

#两张表
# 角色（管理员/普通用户）
# 用户（角色ID）
# 数据库模型，需要继承db.Model
class Role(db.Model):
# 定义表名
   __tablename__='roles'
# 定义字段 db.Column表示是一个字段
   id=db.Column(db.Integer,primary_key=True)
   name=db.Column(db.String(16),unique=True)

class User(db.Model):
# 定义表名
    __tablename__='users'
# 定义字段 db.Column表示是一个字段
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(16),unique=True)
#db.ForeignKey('roles.id') 表示是外键，表名.id
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
# 目的：实现一个简单的登录的逻辑处理
# 1.路由需要有get和post两种请求方式  -->需要判断请求方式
# 2.获取请求的参数
# 3.判断参数是否填写&密码是否相同
# 4.如果判断都没有问题，就返回一个success
# 给模板传递消息flash-->需要对消息加密，因此需要设置secret。key：模板中需要遍历消息

# 使用wtf实现表单
# 自定义表单类

class LoginForm(FlaskForm):
     username = StringField('用户名：',validators=[DataRequired()])
     password=PasswordField('密码：',validators=[DataRequired()])
     password2=PasswordField('确认密码：',validators=[DataRequired(), EqualTo('password','密码填入的不一致')])
     submit=SubmitField('提交')

@app.route('/form',methods=['GET','POST'])
def login():
    login_form=LoginForm()

     # 1.判断请求方式
    if request.method=='POST':

        # 2.获取请求的参数
        username=request.form.get('username')
        password=request.form.get('password')
        password2=request.form.get('password2')
        print(password)

        #3.验证参数，wtf
        #CSRF_token
        if login_form.validate_on_submit():
            print(username,password)
            return 'success'
        else:
            flash('参数有误')
    return render_template('index.html',form=login_form)

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
    #删除表
    db.drop_all()
    #创建表
    db.create_all()
    #插入行
    role=Role(name='admin')
    db.session.add(role)
    db.session.commit()
    user=User(name='heima',role_id=role.id)
    db.session.add(user)
    db.session.commit()

    #查询演练
    User.query.all()

    app.run(debug=True)