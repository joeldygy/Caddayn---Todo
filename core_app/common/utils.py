from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


class CommonUtils:

    @staticmethod
    def get_token_payload(request: Request) -> dict:
        return getattr(request, "payload", {})

    @staticmethod
    def success_response(
        message: str,
        data=None,
        status_code=status.HTTP_200_OK
    ) -> Response:
        response = {
            "status": True,
            "message": message
        }

        if data is not None:
            response["data"] = data

        return Response(response, status=status_code)

    @staticmethod
    def error_response(
        message: str,
        errors=None,
        status_code=status.HTTP_400_BAD_REQUEST
    ) -> Response:
        response = {
            "status": False,
            "message": message
        }

        if errors is not None:
            response["errors"] = errors

        return Response(response, status=status_code)
