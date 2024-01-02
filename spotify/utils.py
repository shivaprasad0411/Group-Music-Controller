from .models import SpotifyToken
from datetime import timedelta
from django.utils import timezone
from requests import post
from .credentials import CLIENT_ID, CLIENT_SECRET

def update_or_create_user_tokens(session_id, access_token, token_type, expires_in, refresh_token):
    tokens = SpotifyToken.objects.filter(user=session_id)
    
    if tokens.exists():
        token = tokens[0]
        token.access_token = access_token
        token.token_type = token_type
        token.expires_in = timezone.now() + timedelta(seconds=expires_in)
        token.refresh_token = refresh_token
        token.save(update_fields=['access_token','token_type','expires_in','refresh_token'])
    else:
        token = SpotifyToken(user=session_id, access_token=access_token, token_type=token_type, expires_in=timezone.now() + timedelta(seconds=expires_in), refresh_token=refresh_token)
        token.save()

def is_spotify_authenticated(session_id):
    tokens = SpotifyToken.objects.filter(user=session_id)
    if tokens.exists():
        expiry = tokens[0].expires_in
        if expiry <= timezone.now():
            refresh_spotify_token(session_id)
        return True
    return False

def refresh_spotify_token(session_id):
    refresh_token = SpotifyToken.objects.get(user=session_id).refresh_token
    
    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type':'refresh_token',
        'refresh_token':refresh_token,
        'client_id':CLIENT_ID,
        'client_secret':CLIENT_SECRET
    }).json()
    
    access_token = response.get('access_token')
    token_type = response.get('token_type')
    expires_in = response.get('expires_in')
    
    update_or_create_user_tokens(session_id, access_token, token_type, expires_in, refresh_token)