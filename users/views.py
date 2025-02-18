from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]  # Requires JWT Token

    def get(self, request):
        return Response({"message": "Authenticated!", "user": request.user.username})
