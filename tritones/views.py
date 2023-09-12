from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse

from tritones.models import Member, boardMember
from tritones.serializers import memberSerializer, boardMemberSerializer

from django.views.decorators.csrf import csrf_exempt

from .forms import ContactForm
from .models import contactModel 
from rest_framework import generics 
from .serializers import ContactSubmissionSerializer

from django.core.mail import send_mail


# send member data
@csrf_exempt
def get_member_data(request):
	data = Member.objects.all()
	if request.method == 'GET':
		serializer = memberSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)
    
# send board member data
@csrf_exempt
def get_board_data(request):
	data = boardMember.objects.all()
	if request.method == 'GET':
		serializer = boardMemberSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)
     
# contact form view
@csrf_exempt  # Disable CSRF protection for simplicity (not recommended for production)
def submit_contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            send_mail(
                'Contact Us Form Submission',
                form.cleaned_data['message'],
                'ExoticTestEmail@555.com',
                [email],  # recipient's email
                fail_silently=False,
            )
            return JsonResponse({'message': 'Form submitted successfully'})
        else:
            return JsonResponse({'message': 'Form data is not valid'})
    else:
        return JsonResponse({'message': 'Only POST requests are allowed'})