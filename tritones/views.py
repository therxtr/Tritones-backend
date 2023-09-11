from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse

from tritones.models import Member, boardMember
from tritones.serializers import memberSerializer, boardMemberSerializer

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_member_data(request):
	data = Member.objects.all()
	if request.method == 'GET':
		serializer = memberSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)
    
@csrf_exempt
def get_board_data(request):
	data = boardMember.objects.all()
	if request.method == 'GET':
		serializer = boardMemberSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)
     
# Create your views here.
def view_home(request):
    return HttpResponse("Hello, Home!")

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
