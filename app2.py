# -*- coding: utf-8-*- 

from flask import Flask
from flask import render_template
from flask import request, url_for, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'

@app.context_processor
def inject_user():
    #user = User.query.first()
    return dict(user=user)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/',methods=['GET', 'POST'])
def index():
    #movies = Movie.query.all()
    if request.method == 'POST':  # 判断是否是 POST 请求
        # 获取表单数据
        title = request.form.get('title')  # 传入表单对应输入字段的 name 值
        year = request.form.get('year')
        flash('dealing your data, plz wait')
        year = float(year)
        while year>0:
        	year = year-0.001
        # 验证数据
        # if not title or not year or len(year) > 4 or len(title) > 60:
        #     flash('Invalid input.')  # 显示错误提示
        #     return redirect(url_for('index'))  # 重定向回主页
        # # 保存表单数据到数据库
        # flash(year)  # 显示成功创建的提示
        # flash(title)
        flash('finish')
        return redirect('yourtest')  # 重定向回主页

    return render_template('index.html', movies=movies, name=user)

user = 'keyb'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]