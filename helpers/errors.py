from fastapi.responses import JSONResponse


async def not_found(request, err):
    """Page not found."""
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse({"message": f"{base_error_message}. Detail: {err}"}, status_code=404)

async def bad_request(request, err):
    """Bad request."""
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse({"message": f"{base_error_message}. Detail: {err}"}, status_code=400)

async def server_error(request, err):
    """Server error."""
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse({"message": f"{base_error_message}. Detail: {err}"}, status_code=500)