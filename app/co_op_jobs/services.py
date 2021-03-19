from app import db
from typing import List

from in_models import CoOpJob


class CoOpJobService:

    @staticmethod
    def get_all() -> List[CoOpJob]:
        return CoOpJob.query.filter_by(is_delete=False)

    @staticmethod
    def get_by_id(job_id: int) -> CoOpJob:
        job = CoOpJob.query.get(job_id)
        if job and job.is_delete != True:
            return job
        return None

    @staticmethod
    def delete_by_id(job_id: int):
        job = CoOpJob.query.get(job_id)
        if job and job.is_delete != True:
            job.is_delete = True
            db.session.commit()
            return True, "Deleted."
        else:
            return False, "Job does not exist"

    @staticmethod
    def create_job(data):
        job = CoOpJob(**data)
        db.session.add(job)
        db.session.commit()
        return job

    @staticmethod
    def update_job(instance, data):
        for field, value in data.items():
            setattr(instance, field, value)
        db.session.commit()
        return instance

