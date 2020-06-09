from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='budget-home'),
    path('profile/', views.profile, name='user-profile')
]
