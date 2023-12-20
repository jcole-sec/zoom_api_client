import requests
import json

ZOOM_API_KEY = 'YOUR_ZOOM_API_KEY'
ZOOM_API_SECRET = 'YOUR_ZOOM_API_SECRET'
ZOOM_BASE_URL = 'https://api.zoom.us/v2'

def get_token():
    """Get Zoom OAuth token."""
    url = f"{ZOOM_BASE_URL}/oauth/token"
    headers = {
        'Authorization': f"Basic {requests.utils.quote(ZOOM_API_KEY + ':' + ZOOM_API_SECRET)}"
    }
    response = requests.post(url, headers=headers, params={'grant_type': 'client_credentials'})
    return response.json()['access_token']

def get_signon_events(token, from_time, to_time):
    """Get sign-on events."""
    url = f"{ZOOM_BASE_URL}/report/users"
    headers = {
        'Authorization': f"Bearer {token}",
        'Content-Type': 'application/json'
    }
    params = {
        'from': from_time,
        'to': to_time
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

if __name__ == "__main__":
    token = get_token()
    from_time = '2023-01-01T00:00:00Z'  # Adjust as needed
    to_time = '2023-12-31T23:59:59Z'    # Adjust as needed
    events = get_signon_events(token, from_time, to_time)
    print(json.dumps(events, indent=4))
