from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


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
        return user
    
    
class CustomerRegistartionConfirmationSerializer(serializers.Serializer):
    token=serializers.CharField(write_only=True)
    