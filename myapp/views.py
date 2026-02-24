from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
# Create your views here.
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
