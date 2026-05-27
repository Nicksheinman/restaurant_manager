from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import VerificationToken
User = get_user_model()
from django.contrib.auth import authenticate


class CustomerRegistrationSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=150)
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)
    second_password=serializers.CharField(write_only=True)
    first_name=serializers.CharField(required=True, allow_blank=False)
    last_name=serializers.CharField(required=False, allow_blank=True)
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("username exist")
        return value
    def validate(self, attrs):
        if attrs['password']!=attrs['second_password']:
            raise serializers.ValidationError('password do not match')
        return attrs
    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("User with this email already exists.")
        return value
    def create(self, validated_data):
        validated_data.pop('second_password')
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data.get('last_name', ''),
            role=User.Role.CUSTOMER,
            is_active=False
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    
class CustomerRegistartionConfirmationSerializer(serializers.Serializer):
    token=serializers.CharField(write_only=True)
    def create(self, validated_data):
        token = validated_data["token"]
        verification=VerificationToken.objects.get(token=token)
        verification.is_verificated=True
        verification.save()
        user=verification.user
        user.is_active=True
        user.save()
        return user
    
class CustomerLoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=150)
    password=serializers.CharField(write_only=True)
    def validate(self, attrs):
        user=authenticate(
            request=self.context.get('request'),
            username=attrs["username"],
            password=attrs['password']
        )
        
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled")
        
        attrs["user"] = user
        return attrs
    