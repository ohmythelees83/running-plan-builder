import requests

ACCESS_TOKEN = '90a69e9203744991651d9d3f185db6b2e39ef37b'

# Define the API endpoint
url = "https://www.strava.com/api/v3/athlete/activities"

# Make the request to Strava API
response = requests.get(
    url=url,
    headers={
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
)

# Parse the JSON response
activities = response.json()

# Print out the activities
for activity in activities:
    print(f"Name: {activity['name']}, Distance: {activity['distance']} meters, Time: {activity['moving_time']} seconds")
