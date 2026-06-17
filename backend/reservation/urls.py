from django.urls import path
from .views import GetRestaurantMap


urlpatterns=[
     path('getMap/<int:restaurant_id>/',GetRestaurantMap.as_view(), name='getRestaurantMap'),
]