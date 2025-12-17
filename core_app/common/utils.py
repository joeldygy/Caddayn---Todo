import random
import urllib

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

class CommonUtils:
    def __init__(self) -> None:
        super().__init__()



    @staticmethod
    def success_response_data(message, data: list | dict = None, image=False):
        if image:
            return message
        if data is None and message is None:
            return {'status': True}
        if message is None:
            return {'status': True, 'data': data}
        if data is None:
            return {'status': True, 'message': message}
        return {'status': True, 'message': message, 'data': data}



    @staticmethod
    def error_response_data(message: str, error: list[str] | str):
        return {'status': False, 'message': message, 'error': error}