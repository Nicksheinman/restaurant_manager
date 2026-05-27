from django.urls import path
from .views import CustomerRegistrationView, CustomerRegistrationConfirmationView, CustomerLogin


urlpatterns=[
     path('registration/',CustomerRegistrationView.as_view(), name='registration'),
     path('registration_Confirmation/',CustomerRegistrationConfirmationView.as_view(), name='confirmation'),
     path('login_user/', CustomerLogin.as_view(), name='login')
]