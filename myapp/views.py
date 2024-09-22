from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from .authentication import KeycloakAuthentication

@api_view(['POST'])
def create_user(request):
    return JsonResponse({"Success": "user is created"})


@api_view(['GET'])
@authentication_classes([KeycloakAuthentication])
@permission_classes([IsAuthenticated])
def index(request):
    return JsonResponse({"Success":"Helloworld"})


