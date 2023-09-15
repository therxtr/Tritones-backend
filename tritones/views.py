import json
from django.http import JsonResponse, HttpResponse

from tritones.models import Member, boardMember
from tritones.serializers import memberSerializer, boardMemberSerializer, tritoneSpotifyTrackSerializer

from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail

from .forms import ContactForm

from .config import sp

from .models import TritoneSpotifyTrack


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


def get_track_data(request):
    data = TritoneSpotifyTrack.objects.all()
    if request.method == 'GET':
        serializer = tritoneSpotifyTrackSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

def view_home(request):
    the_tritones_artist_id = "1eohVzWa5vbk54pmWcFQar"
    fetch_and_store_tracks(the_tritones_artist_id)

def fetch_and_store_tracks(artist_spotify_id):
    # Fetch the top tracks of the artist
    top_tracks = sp.artist_top_tracks(artist_spotify_id)

    # Process and store the fetched tracks in the database
    for track_data in top_tracks['tracks']:
        # Extract relevant information from the track data
        name = track_data['name']
        album = track_data['album']['name']
        spotify_id = track_data['id']

        # Fetch additional details for the track
        track_details = sp.track(spotify_id)

        # Extract the track image URL, track name, and year of release
        image_url = track_details['album']['images'][0]['url']  # URL of the first image
        release_year = track_details['album']['release_date'].split('-')[0]  # Extract year from release_date
        spotify_url = track_details['external_urls']['spotify']  # Spotify URL

        # Create or update the SpotifyTrack model instance with the additional details
        track, created = TritoneSpotifyTrack.objects.get_or_create(
            spotify_id=spotify_id,
            defaults={'name': name, 'album': album, 'image_url': image_url, 'release_year': release_year, 'spotify_url': spotify_url}
        )

    # Optionally, you can return the fetched tracks or a success message
    return "Data fetched and stored successfully."