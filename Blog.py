from contactwtf import *
from flask_mail import *
from flask import *
from flask_sqlalchemy import *
import math


app = Flask(__name__)
app.config['SECRET_KEY'] = "ABC"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/universe"

db = SQLAlchemy(app)
mail = Mail(app)

from Model import *


@app.route('/')
def index():
    if request.method == 'GET':
        cate = request.args.get('cate')
        if cate:
            cate = int(cate)
            cat = Category.query.filter_by(cat_id=cate).first()
            return render_template('index.html', post=cat.cat_rel, category=Category.query.all())
        else:
            post_count = 4
            posts = Post.query.all()
            last = math.ceil(len(posts)/post_count)
            page = request.args.get('page')
            if not str(page).isnumeric():
                page = 1
            page = int(page)
            posts = posts[(page-1)*post_count:(page-1)*post_count+post_count]
            if page == 1:
                prev = '#'
                next = "/?page=" + str(page+1)
            elif page == last:
                prev = "/?page=" + str(page-1)
                next = '#'
            else:
                prev = "/?page=" + str(page-1)
                next = "/?page=" + str(page+1)
            return render_template('index.html', post=Post.query.all(), category=Category.query.all(), posts=posts, prev=prev, next=next)

    elif request.methods == 'POST':
        try:
            return render_template('index.html', post=Post(), category=Category())
        except Exception as e:
            return render_template('Error.html', msg=e)


@app.route('/aboutus/')
def aboutus():
    return render_template('Aboutus.html')


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    return render_template('contactblog.html', form=form)


@app.route('/login/')
def login():
    return render_template('Login.html')


@app.route('/submit/', methods=['POST'])
def submit():
    username1 = request.form['username']
    password = request.form['password']

    try:
        user = Login.query.filter_by(username=username1).first()
        if password == user.password:
            if 'user' not in session:
                session['user'] = request.form['username']
                session['password'] = request.form['password']
            return render_template('Adminform.html')
        else:
            return render_template('Error.html', msg='Invalid password')
    except Exception as e:
        return render_template('Error.html', msg=e)


@app.route('/sendmail/', methods=['POST'])
def sendmail():
    try:
        if request.method == 'POST':
            comm = Comment(request.form['email'], request.form['subject'], request.form['message'])
            db.session.add(comm)
            db.session.commit()
            msg = Message(subject=request.form['subject'], sender=request.form['email'], recipients=['misssweta0786@gmail.com'])
            msg.body = request.form['message']
            mail.send(msg)
            return '<center><h2>Mail successfully sent</h2</center>'
    except Exception as e:
        return render_template('Error.html', msg=e)


@app.route('/category/')
def category():
    if 'user' in session:
        cat = Category()
        return render_template('Category.html', cat=cat)
    else:
        return render_template('Login.html', msg='Fill the loginform first')


@app.route('/post/')
def post():
    if 'user' in session:
        post = Post()
        return render_template('post.html', post=post)
    else:
        return render_template('Login.html', msg='Fill the loginform first')


@app.route('/add/')
def add():
    if 'user' in session:
        cat = Category()
        return render_template('Addpost.html', cat=cat)
    else:
        return render_template('Login.html', msg='Fill the loginform first')


@app.route('/postsubmit/', methods=['POST', 'GET'])
def postsubmit():
    try:
        if request.method == 'POST':
            cat = Category.query.filter_by(cat_name=request.form['category']).first()
            post = Post(post_time=request.form['time'], post_desc=request.form['desc'], post_author=request.form['author'], post_title=request.form['title'])
            db.session.add(post)
            post.blogger.append(cat)
            db.session.commit()
            return 'successfully post submitted'
    except Exception as e:
        return render_template('Error.html', msg=e)


@app.route('/catadd/')
def catadd():
    if 'user' in session:
        return render_template('catadd.html')
    else:
        return render_template('Login.html', msg='Fill the loginform first')


@app.route('/catsubmit/', methods=['GET', 'POST'])
def catsubmit():
    try:
        if request.method == 'POST':
            cat = Category(cat_name=request.form['category'])
            db.session.add(cat)
            db.session.commit()
            return 'Category successfully submitted'

    except Exception as e:
        return render_template('Error.html', msg=e)



@app.route('/readmore/')
def readmore():
    obj = request.args.get('obj')
    post = Post()
    desc = Post.query.filter_by(post_id=obj).first()
    return render_template('Readmore.html', desc=desc)


@app.route('/logout/')
def logout():
    if 'user' in session:
        session.pop('user')
        session.pop('password')
        return render_template('index.html', msg='Logged out successfully')


@app.route('/delete/')
def delete():
    post = Post()
    return render_template('Deletepost.html', post=post)


@app.route('/deletepost/', methods=['POST'])
def deletepost():
    if request.method == 'POST':
        post = request.form.getlist('post')
        for p in post:
            db.session.delete(Post.query.filter_by(post_id=p).one())
            db.session.query(Post.post_id).filter_by(post_id=p)
            db.session.commit()
        return render_template('Error.html', msg='Successfully deleted')


@app.route('/catdel/')
def catdel():
    cat = Category()
    return render_template('Deletecat.html', cat=cat)


@app.route('/deletecat/', methods=['POST'])
def deletecat():
    if request.method == 'POST':
        cat = request.form.getlist('cat')
        for c in cat:
            db.session.delete(Category.query.filter_by(cat_id=c).one())
            db.session.query(Category.cat_id).filter_by(cat_id=c)
            db.session.commit()
        return render_template('Error.html', msg='Successfully deleted')


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=80)
