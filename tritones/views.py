from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view_home(request):
    return HttpResponse("Hello, Tritones!")

def view_about_us(request):
    return HttpResponse("Hello, About Us!")

def view_auditions(request):
    return HttpResponse("Hello, Auditions!")

def view_photos(request):
    return HttpResponse("Hello, Photos!")

def view_bookings(request):
    return HttpResponse("Hello, Bookings!")

def view_contact_us(request):
    return HttpResponse("Hello, Contact Us!")
