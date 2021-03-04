def register_routes(api, app, root="api"):
    from app.co_op_jobs import register_routes as attach_co_op

    attach_co_op(api, app)

