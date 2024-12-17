from rest_framework.views import APIView
from .api_response import ApiResponse
from django.db import connections


class HealthCheckView(APIView):
    """
    Health check view
    """

    def get(self, request):
        # health check business logic
        return ApiResponse.success()