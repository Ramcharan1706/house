from django.urls import path
from . import views

urlpatterns = [
    path('House/estimate/', views.estimate_house_price, name='estimate_house_price'),  # This matches /House/estimate/
    path('estimate/', views.estimate_house_price, name='estimate_house_price'),  # This matches /estimate/
    path('greek/<str:name>/', views.greek, name='greek'),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
]
