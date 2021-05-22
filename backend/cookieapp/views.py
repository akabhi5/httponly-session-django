from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.middleware.csrf import get_token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def get_csrf_token(request):
    response = Response({"message": "Set CSRF cookie"})
    response["X-CSRFToken"] = get_token(request)
    return response


@api_view(['POST'])
def login_view(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(username=username, password=password)
    if user:
        print(user)
        login(request, user)
        return Response({'message': 'User logged in'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)