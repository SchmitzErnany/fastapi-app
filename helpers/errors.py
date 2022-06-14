from flask import make_response


def not_found(err):
    """Page not found."""
    return make_response({'message': str(err)}, 404)

def bad_request(err):
    """Bad request."""
    return make_response({'message': str(err)}, 400)

def server_error(err):
    """Server error."""
    return make_response({'message': str(err)}, 500)