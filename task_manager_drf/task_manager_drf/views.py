from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class APIRootView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            "message": "Task Manager API",
            "endpoints": {
                "auth": {
                    "register": "/auth/register/",
                    "login": "/auth/login/",
                    "refresh": "/auth/refresh/",
                    "logout": "/auth/logout/",
                },
                "tasks": "/tasks/",
                "admin": "/admin/",
            },
        })
