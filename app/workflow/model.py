from app import db
from datetime import datetime

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    status = db.Column(db.String, default='RUNNING')
    workflow = db.Column(db.PickleType, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow)

    def get_created_on(self):
        return self.created_on.strftime("%c")
    
    def get_updated_on(self):
        return self.updated_on.strftime("%c")

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        return

    def commit(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        return

    @staticmethod
    def get_jobs_via_user_id(user_id):
        jobs = User.query.filter_by(user_id=user_id)
        return jobs

    def __repr__(self):
        return "id: {}, user_id: {}, workflow: {}, created_on: {}".format(self.id, \
            self.user_id, self.workflow, self.created_on)
    
# class Modules(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     module_name = db.Column(db.String)    
#     module_file = db.Column(db.String)
