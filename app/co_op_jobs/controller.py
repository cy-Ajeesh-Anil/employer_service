from flask import request
from flask_restx import Namespace, Resource
from marshmallow import ValidationError

from app.response import Response
from app.status_constants import HttpStatusCode

from .schemas import CoOpJobSchema
from .services import CoOpJobService


api = Namespace("CoOpJob", description="Namespace for CoOpJob")


@api.route("/")
class CoOpJobs(Resource):
    """
    Class for handle CoOpJobs end points
    """

    def get(self):
        """
        Return all jobs
        """
        jobs = CoOpJobService.get_all()

        return Response.success(
            CoOpJobSchema().dump(jobs, many=True),
            HttpStatusCode.OK,
            message="List of jobs")

    def post(self):
        """
        create new job
        """
        payload = request.json
        schema = CoOpJobSchema()
        try:
            result = schema.load(payload)
        except ValidationError as err:
            return Response.error(err.messages,
                                  status_code=HttpStatusCode.BAD_REQUEST,
                                  message="Form validation error.")

        return Response.success(schema.dump(result),
                                status_code=HttpStatusCode.CREATED,
                                message="Job created successful.")


@api.route("/<id>")
class CoOpJob(Resource):
    """
    Class for handing CoOpJob Endpoints
    """

    def get(self, id):
        """
        get a job details
        """
        job = CoOpJobService.get_by_id(id)
        if job:
            return Response.success(
                CoOpJobSchema().dump(job),
                status_code=HttpStatusCode.OK,
                message="Detail of the job.")
        else:
            return Response.error({},
                                  status_code=HttpStatusCode.NOT_FOUND,
                                  message="Job does not exist")

    def put(self, id):
        """
        update the given id job
        """
        payload = request.json
        schema = CoOpJobSchema()
        current_job = CoOpJobService.get_by_id(id)
        try:
            result = schema.load(payload, instance=current_job, partial=True)
        except ValidationError as err:
            return Response.error(err.messages,
                                  status_code=HttpStatusCode.BAD_REQUEST,
                                  message="Form validation error.")

        return Response.success(schema.dump(result),
                                status_code=HttpStatusCode.OK,
                                message="Job updated successful.")

    def delete(self, id):
        """
        soft deleting the Job.
        """
        deleted, error = CoOpJobService.delete_by_id(id)
        if deleted:
            return Response.success(
                {"id": id},
                status_code=HttpStatusCode.OK,
                message="Job Deleted Successful")
        else:
            return Response.error(
                error,
                status_code=HttpStatusCode.NOT_FOUND,
                message="Job does not exist.")

