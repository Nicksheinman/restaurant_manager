from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import CustomerRegistrationSerializer
from .services.mail import send_email_registration
from rest_framework.response import Response
from rest_framework import status

class CustomerRegistrationView(APIView):
    
    def post(self, request):
        serializer=CustomerRegistrationSerializer
        
        if serializer.is_valid():
            user=serializer.save()
            send_email_registration(user=user)
            return Response({'message':'user created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

