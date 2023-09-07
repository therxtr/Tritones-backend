from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_home, name='view_home'),
    path('about-us', views.view_about_us, name='view_about_us'),
    path('auditions', views.view_auditions, name='view_auditions'),
    path('photos', views.view_photos, name='view_photos'),
    path('bookings', views.view_bookings, name='view_bookings'),
    path('contact-us', views.view_contact_us, name='view_contact_us'),
]
