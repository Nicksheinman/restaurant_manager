from django.urls import path
from .views import CustomerRegistrationView, CustomerRegistrationConfirmationView


urlpatterns=[
     path('registration/',CustomerRegistrationView.as_view(), name='registration'),
     path('registration_Confirmation/',CustomerRegistrationConfirmationView.as_view(), name='confirmation'),
     
]