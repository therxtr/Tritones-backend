from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.my_view, name='my_view')
]
