from django.http import JsonResponse
from .constants import RESULT_INFO
from rest_framework import status


class ApiResponse(JsonResponse):
    def __init__(self, result, info, status_code):
        self.result = result
        self.info = info
        self.status_code = status_code

        response_body = {"result": self.result, "info": self.info}
        super().__init__(data=response_body, status=self.status_code)

    @classmethod
    def bad_request(cls, data={}):
        return ApiResponse(data, RESULT_INFO["BAD_REQUEST"], status.HTTP_400_BAD_REQUEST)

    @classmethod
    def system_error(cls):
        return ApiResponse(None, RESULT_INFO["SYSTEM_ERROR"], status.HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def success(cls, data=None):
        return ApiResponse(data, RESULT_INFO["SUCCESS"], status.HTTP_200_OK)

    @classmethod
    def created(cls, data=None):
        return ApiResponse(data, RESULT_INFO["RECORD_CREATED"], status.HTTP_201_CREATED)

    @classmethod
    def updated(cls, data=None):
        return ApiResponse(data, RESULT_INFO["RECORD_UPDATED"], status.HTTP_200_OK)

    @classmethod
    def deleted(cls):
        return ApiResponse(None, RESULT_INFO["RECORD_DELETED"], status.HTTP_200_OK)

    @classmethod
    def idem_error(cls, data=None):
        return ApiResponse(data, RESULT_INFO["IDEM_ERROR"], status.HTTP_200_OK)

    @classmethod
    def request_timeout(cls):
        return ApiResponse(None, RESULT_INFO["REQUEST_TIMEOUT"], status.HTTP_504_GATEWAY_TIMEOUT)

    @classmethod
    def forbidden(cls):
        return ApiResponse(None, RESULT_INFO["FORBIDDEN"], status.HTTP_403_FORBIDDEN)

    @classmethod
    def service_unavailable(cls):
        return ApiResponse(None, RESULT_INFO["SERVICE_UNAVAILABLE"], status.HTTP_503_SERVICE_UNAVAILABLE)
