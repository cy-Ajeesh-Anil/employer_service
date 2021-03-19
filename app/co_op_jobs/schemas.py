from app import ma, db
from marshmallow import post_load, fields, validate

from in_models import CoOpJob
from .services import CoOpJobService


class CoOpJobSchema(ma.SQLAlchemySchema):
    id = fields.Integer(dump_only=True)
    address = fields.Str(required=True, validate=[validate.Length(min=4, max=250)])
    job_title = fields.Str(required=True, validate=[validate.Length(min=4, max=250)])
    job_description = fields.Str(required=True, validate=[validate.Length(min=4, max=250)])
    vacancy = fields.Integer(required=True)
    duration = fields.Integer(required=True)
    url = fields.Str(required=True, validate=[validate.Length(min=4, max=250)])
    role = fields.Str(required=True, validate=[validate.Length(min=4, max=250)])
    details = fields.Str(required=True, validate=[validate.Length(min=4, max=250)])
    intention = fields.Str(required=True, validate=[validate.Length(min=4, max=250)])
    remote = fields.Boolean(required=True)
    alumni = fields.Boolean(required=True)
    hourly_rate = fields.Float(required=True)
    expires_on = fields.DateTime(required=True)

    class Meta:
        model = CoOpJob
        fields = (
            "id",
            "created_on",
            "updated_on",
            "address",
            "job_title",
            "job_description",
            "vacancy",
            "duration",
            "url",
            "role",
            "details",
            "intention",
            "remote",
            "alumni",
            "hourly_rate",
            "expires_on")

    @post_load
    def create_oru_update_job(self, data, **kwargs):
        if self.instance: # update current instance
            job = CoOpJobService.update_job(self.instance, data)

        else: # create  new instance
            job = CoOpJobService.create_job(data)

        db.session.commit()
        return job


