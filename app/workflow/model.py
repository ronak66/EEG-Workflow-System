from app import db
from datetime import datetime

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    status = db.Column(db.String, default='RUNNING')
    workflow = db.Column(db.PickleType, nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
    # updated_on = db.Column(db.DateTime, default=datetime.utcnow)

    def get_start_time(self):
        return self.start_time.strftime("%c")
    
    def get_end_time(self):
        return self.end_time.strftime("%c")

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
        jobs = Job.query.filter_by(user_id=user_id)
        return jobs

    def __repr__(self):
        return "id: {}, user_id: {}, workflow: {}, start_time: {}, end_time: {}".format(self.id, \
            self.user_id, self.workflow, self.start_time, self.end_time)
    
# class Modules(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     module_name = db.Column(db.String)    
#     module_file = db.Column(db.String)
