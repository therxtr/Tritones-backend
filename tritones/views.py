import json
from django.http import JsonResponse, HttpResponse

from tritones.models import Member, Photo
from tritones.serializers import memberSerializer, tritoneSpotifyTrackSerializer, photoSerializer

from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail

from .config import sp

from .models import TritoneSpotifyTrack


# send member data
@csrf_exempt
def get_member_data(request):
	data = Member.objects.all()
	if request.method == 'GET':
		serializer = memberSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)

# send photo data
@csrf_exempt
def get_member_data(request):
	data = Photo.objects.all()
	if request.method == 'GET':
		serializer = photoSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)




# contact form view
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

# track data for spotify
@csrf_exempt
def get_track_data(request):
    data = TritoneSpotifyTrack.objects.all()
    if request.method == 'GET':
        serializer = tritoneSpotifyTrackSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def fetch_and_store_tracks(request):
    # Fetch the top tracks of the artist
    the_tritones_artist_id = "1eohVzWa5vbk54pmWcFQar"
    top_tracks = sp.artist_top_tracks(the_tritones_artist_id)

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
    return HttpResponse("Data fetched and stored successfully.")