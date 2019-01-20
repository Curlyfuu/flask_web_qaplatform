from flask import Flask,render_template,url_for,request,redirect,session
import config
from models import User,Question,Comment
from exts import db
from decorator import login_required


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)




@app.route('/')
def index():
    context = {
        'questions':Question.query.order_by('-create_time').all()
    }
    return render_template('index.html',**context)

@app.route('/login/',methods=['GET',"POST"])
def login():
    if request.method =='GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone ==telephone,User.password == password).first()
        if user:
            session['user_id'] = user.id
            #如果想在31天内都不需要登陆
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return u'手机号码或者密码错误，请确认后再登陆'

@app.route('/regist/',methods=['GET',"POST"])
def regist():
    if request.method =='GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username  = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        # 手机号码验证
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return u'已被注册'
        else:
            #密码验证password1==password2
            if password1 != password2:
                return u'两次输入的密码不相等，请核对'
            else:
                user = User(telephone=telephone,username=username,password=password1)
                db.session.add(user)
                db.session.commit()
                #如注册成功，跳转到登陆界面
                return redirect(url_for('login'))
@app.route('/logout/')
def logout():
    #session.pop('user_id')
    #del session('user_id')
    session.clear()
    return redirect(url_for('login'))
@app.route('/question/',methods=['GET',"POST"])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')

    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title,content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        question.author = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))




# 钩子函数
@app.context_processor
def my_contex_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user':user}
    return {}

# 详情页面
@app.route('/detail/<question_id>')
def detail(question_id):
    question_model = Question.query.filter(Question.id == question_id).first()


    return render_template('detail.html',question = question_model)

#评论功能
@app.route('/add_comment/',methods=['POST'])
@login_required
def add_comment():
    content = request.form.get('comment_content')
    question_id = request.form.get('question_id')

    comment = Comment(content=content)
    user_id = session['user_id']
    user = User.query.filter(User.id == user_id).first()
    comment.author = user
    question = Question.query.filter(Question.id == question_id).first()
    comment.question = question
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('detail',question_id=question_id))





if __name__ == '__main__':
    app.run()
