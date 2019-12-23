from Blog import db


class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(10))

    def __init__(self, username="", password=""):
        self.username = username
        self.password = password


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_id = db.Column(db.String(40))
    subject = db.Column(db.String(30))
    message = db.Column(db.String(500))

    def __init__(self, email_id, subject, message):
        self.email_id = email_id
        self.subject = subject
        self.message = message


blog = db.Table('blog',
                db.Column('cat_id', db.Integer, db.ForeignKey('category.cat_id')),
                db.Column('post_id', db.Integer, db.ForeignKey('post.post_id')))


class Category(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(20))
    cat_rel = db.relationship('Post', secondary=blog, backref=db.backref('blogger', lazy='dynamic'))

    def __init__(self, cat_name=""):
        self.cat_name = cat_name


class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    post_time = db.Column(db.String(8))
    post_desc = db.Column(db.Text)
    post_author = db.Column(db.String(30))
    post_title = db.Column(db.String(30))

    def __init__(self, post_time="", post_desc="", post_author="", post_title=""):
        self.post_time = post_time
        self.post_title = post_title
        self.post_desc = post_desc
        self.post_author = post_author


class Subscribe(db.Model):
    sub_id = db.Column(db.Integer, primary_key=True)
    subscriber = db.Column(db.String(50))

    def __init__(self, subscriber=""):
        self.subscriber = subscriber
