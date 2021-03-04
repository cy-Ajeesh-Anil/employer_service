from app.helpers.models import TimeStampModel
from app import db


class CoOpJob(TimeStampModel):
    """
    A job model
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String, unique=True)
    address = db.Column(db.String(255))
    job_title = db.Column(db.String(255))
    job_description = db.Column(db.String(255))
    vacancy = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    url = db.Column(db.String(255))
    role = db.Column(db.String)
    details = db.Column(db.String(255))
    intention = db.Column(db.String(255))
    remote = db.Column(db.Boolean)
    alumni = db.Column(db.Boolean)
    hourly_rate = db.Column(db.Float)
    expires_on = db.Column(db.DateTime)
    is_delete = db.Column(db.Boolean, default=False)

