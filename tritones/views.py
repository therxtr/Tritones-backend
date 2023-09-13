import json
from django.http import JsonResponse

from tritones.models import Member, boardMember
from tritones.serializers import memberSerializer, boardMemberSerializer

from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail

from .forms import ContactForm


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
"""
@csrf_exempt  # Disable CSRF protection for simplicity (not recommended for production)
def submit_contact_form(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			form.save()
            
			message_text = f"Name: {name}\nEmail: {email}\nMessage: {message}"
			send_mail(
                subject,
                message_text,
                email,
                ['exotictestemail555@gmail.com'],  # recipient's email
                fail_silently=False,
            )
			return JsonResponse({'message': 'Form submitted successfully'})
		else:
			print(request.POST)
			return JsonResponse(form.errors)
	return JsonResponse({'message': 'Only POST requests are allowed'})
"""

@csrf_exempt
def submit_contact_form(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)

            # Extract data from the JSON payload
            name = data.get('name')
            subject = data.get('subject')
            email = data.get('email')
            message = data.get('message')

            # Process the data by sending an email
            send_mail(
                f'Contact Us Form Submission: {subject}',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                email,  # Replace with your Gmail email
                ['exotictestemail555@gmail.com'],  # Replace with the recipient's email address
                fail_silently=False,
            )

            # Respond with a success message
            return JsonResponse({'message': 'Form submitted successfully'})

        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'message': 'Only POST requests are allowed'}, status=405)

			