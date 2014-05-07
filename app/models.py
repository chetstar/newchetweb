from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(120))
    subject = db.Column(db.String(120))
    message = db.Column(db.String(120))

    def __repr__(self):
        return '<User %r>' % (self.name)