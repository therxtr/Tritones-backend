from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_contact_form, name='submit_contact_form'),
    path('getTracks/', views.fetch_and_store_tracks)
]
