from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='budget-home'),
    path('add-project/', views.add_project, name='add-project')
]
