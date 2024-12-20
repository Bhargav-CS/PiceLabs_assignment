import json

# Read the JSON response from the response.json file
with open('response.json', 'r') as file:
    response_json = file.read()

# Parse the JSON response
response = json.loads(response_json)

# Extract the results
results = response['data']['searchQueries']['search']['results']

# Base URL for constructing the listing URLs
base_url = "https://www.booking.com/hotel/in/"

# Construct the listing URLs
listing_urls = [f"{base_url}{result['basicPropertyData']['pageName']}.html" for result in results]

# Print the listing URLs
for url in listing_urls:
    print(url)