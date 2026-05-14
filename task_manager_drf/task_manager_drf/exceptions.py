from rest_framework.views import exception_handler
from rest_framework import status


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data = {
            "error": exc.__class__.__name__,
            "message": response.data.get("detail") or str(exc),
            "status": response.status_code,
        }

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            response.data["errors"] = exc.detail if hasattr(exc, "detail") else str(exc)

    return response
