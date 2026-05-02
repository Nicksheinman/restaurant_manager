from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import CustomerRegistrationSerializer, CustomerRegistartionConfirmationSerializer
from .services.mail import send_email_registration
from rest_framework.response import Response
from rest_framework import status
from .models import VerificationToken

class CustomerRegistrationView(APIView):
    
    def post(self, request):
        serializer=CustomerRegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            user=serializer.save()
            send_email_registration(user=user)
            return Response({'message':'user created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

class CustomerRegistrationConfirmationView(APIView):
    
    def get(self, request):
        # serializer=CustomerRegistartionConfirmationSerializer
        token = request.query_params.get('token')
        verification=VerificationToken.objects.get(token=token)
        verification.is_verificated=True
        verification.save()
        user=verification.user
        user.is_active=True
        user.save()
        return Response({'message':'ok'}, status=status.HTTP_200_OK)

    