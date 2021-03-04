BASE_ROUTE = "job"


def register_routes(api, app, root="api"):
    from .controller import api as co_op_job_api

    api.add_namespace(co_op_job_api, path=f"/{root}/{BASE_ROUTE}")

