from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import CustomerRegistrationSerializer, CustomerRegistartionConfirmationSerializer, CustomerLoginSerializer
from .services.mail import send_email_registration
from rest_framework.response import Response
from rest_framework import status
from .models import VerificationToken
from rest_framework_simplejwt.tokens import RefreshToken

class CustomerRegistrationView(APIView):
    
    def post(self, request):
        print(request.data)
        serializer=CustomerRegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            user=serializer.save()
            send_email_registration(user=user)
            return Response({'message':'user created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

class CustomerRegistrationConfirmationView(APIView):    
    def post(self, request):
        serializer=CustomerRegistartionConfirmationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'ok'}, status=status.HTTP_200_OK)
        return Response({'message':'token not found'}, status=status.HTTP_404_NOT_FOUND)

class CustomerLogin(APIView):
    def post(self, request):
        print(request.data)
        serializer=CustomerLoginSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)
        return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token)
        })
