from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Product
# Create your views here.

@api_view(['POST'])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        # Create token if not exists
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key,
            "user_id": user.id,
            "username": user.username
        })

    return Response(
        {"error": "Invalid credentials"},
        status=status.HTTP_401_UNAUTHORIZED
    )
    
@api_view(['GET'])
def dashboard(request):
    return Response({
        "message": "Welcome",
        "user": request.user.username
    })

class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all().values('id', 'name', 'price')
        return Response(list(products), status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        try:
            product = Product.objects.create(
                name=data['name'],
                price=data['price'],
            )
            return Response({'id': product.id, 'message': 'Created successfully'}, status=status.HTTP_201_CREATED)
        except KeyError as e:
            return Response({'error': f'Missing field: {e}'}, status=status.HTTP_400_BAD_REQUEST)
