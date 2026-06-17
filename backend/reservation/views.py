from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializer import RestarauntGetSerializer
from .models import Table
from rest_framework.response import Response
from rest_framework import status


class GetRestaurantMap(APIView):
    permission_classes = [IsAuthenticated]
        
    def get(self, request, restaurant_id):
        tables = Table.objects.filter(restaurant=restaurant_id)
        
        serializer=RestarauntGetSerializer(tables, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)