from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        CUSTOMER = "customer", "Customer"
        OWNER = "owner", "Owner"
        ADMIN = "admin", "Admin"
    
    email=models.EmailField(unique=True)
    
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER
    )
    
class VertificationToken(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    token=models.CharField(max_length=300)
    is_verificated=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)