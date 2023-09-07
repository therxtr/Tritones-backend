from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse

from tritones.models import exampleModel
from tritones.serializers import exampleModelSerializer

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_data(request):
	data = exampleModel.objects.all()
	if request.method == 'GET':
		serializer = exampleModelSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)
     
# Create your views here.
def view_home(request):
    return render(request, "tritones/home.html")

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
