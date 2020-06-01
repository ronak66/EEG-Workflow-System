from app import db, bcrypt
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow)

    def get_created_on(self):
        return self.created_on.strftime("%c")
    
    def get_updated_on(self):
        return self.updated_on.strftime("%c")

    def check_hash_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        return

    @staticmethod
    def generate_hash_password(password):
        return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")

    @staticmethod
    def get_user_via_email(email):
        user = User.query.filter_by(email=email).first()
        return user

    def __repr__(self):
        return "id: {}, username: {}, email: {}, created_on: {}".format(self.id, \
            self.username, self.email, self.created_on)
    
