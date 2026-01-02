from functools import wraps
from rest_framework.response import Response
from rest_framework import status

def standard_response(default_message="Request successful"):
    """
    Decorator to standardize API responses for DRF views.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Call the original view
                result = func(*args, **kwargs)

                # If the view already returns a DRF Response, extract its data
                if isinstance(result, Response):
                    data = result.data
                    status_code = result.status_code
                else:
                    data = result
                    status_code = status.HTTP_200_OK

                # Wrap the response if it's a dict without 'success' key
                if isinstance(data, dict) and "success" not in data:
                    response_data = {
                        "success": True,
                        "message": data.get("message", default_message),
                        "data": data.get("data", None),
                        "errors": data.get("errors", None)
                    }
                else:
                    response_data = data

                return Response(response_data, status=status_code)

            except Exception as e:
                # Handle unexpected exceptions
                return Response(
                    {
                        "success": False,
                        "message": str(e),
                        "data": None
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        return wrapper
    return decorator
