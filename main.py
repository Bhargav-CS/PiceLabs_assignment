import requests
import csv
import json

def fetch_data(body):
    """Fetch data from the Booking.com API"""
    
    url = "https://www.booking.com/dml/graphql"
    headers = {
        "accept": "*/*",
        "accept-language": "en-GB,en;q=0.7",
        "content-type": "application/json",
        "cookie": "px_init=0; pcm_consent=analytical%3Dtrue%26countryCode%3DIN%26consentId%3Def552b9e-a259-4741-ad3a-e66db563ec9c%26consentedAt%3D2024-02-29T14%3A48%3A18.689Z%26expiresAt%3D2024-08-27T14%3A48%3A18.689Z%26implicit%3Dtrue%26marketing%3Dtrue%26regionCode%3DKA%26regulation%3Dnone%26legacyRegulation%3Dnone; bkng_sso_session=e30; bkng_sso_ses=e30; _pxhd=l1VHnFED432P4U6wG-B5VP9%2F46XzrG7Qv8lfOB8g2HN265AlW8BB6AP98WWPzjdhLQAwiMtiKf4LV5y2pbS6QQ%3D%3D%3AM4mRLb4ORiG5aLq5Mil%2FFBL%2FucckryNyUxrxSgFtrF2L4x310dL3r9Rv%2FuUltSC3pk4Y%2FfIlRNQYFKAUNBPs04UgQNbn1ani1YpbAZT%2FCfc%3D; pxcts=aa860a0d-d711-11ee-9e8d-f6ec8a89a25b; bs=%7B%22gc%22%3A1%7D; qr_is_sr=fast-click; 11_srd=%7B%22features%22%3A%5B%7B%22id%22%3A5%7D%5D%2C%22score%22%3A3%2C%22detected%22%3Afalse%7D; pcm_personalization_disabled=0; bkng_sso_auth=CAIQsOnuTRpmCvN2T1sxcM7wXLWbcQd6z0Cm6xaWBO9rQxOB9/ONnhf71l2kwxfJx3auoJfKUWOVHJrK5KkdNUhEkYNeJoe9o5Hmu7Iu65+ZJcWj+P6CJfn52bjP2LuDh1KKqYp9F5++eAAWsxbP; cors_js=1; BJS=-; aws-waf-token=eb71beb8-98b5-4eb6-bd21-9e817d992a68:HgoAikFJbishAAAA:kePYlBJb55HsoBGxx/Z8QHWZLfDjB298StazgQnecolRTcEM6kKLCfCbCrpHiiBkezeXlm2gIInb6zD96VJvKg6kWj4LUPTB3JIHc1Ueo4zmWJtW4kiUv1AMXkQf7itB3jWZzrxrfqQsjlEOJIE9izvW948rpf1aM47INlA/elWfva4dwgh7wMu+LXf88F0W7HIKOslLXyvaBKgZ; bkng=11UmFuZG9tSVYkc2RlIyh9YSvtNSM2ADX0BnR0tqAEmju3Hqww3f4xH1FWtu0PhSoE1GWriV3TDLv6gfUX9GITdglHqvXFXqI0DxpljqO8ImGlmzozNwIe1y9El%2Fk0KPyzFeJWurckAlX9ymWsW87Y3ZXs8HUZ1fkIFCFwjEGGJWczz4jdBC7DL0nNNu8G9sT6axa5eWgMRgwPTYXp7lgk5A%3D%3D; lastSeen=0",
        "origin": "https://www.booking.com",
        "referer": "https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4AofIxbMGwAIB0gIkNDFkMDkyZDktMDFlZC00NzMxLTkyMjMtNGFhYWIxNjEwMjg12AIF4AIB&sid=aa4f62f572ac5f487c282f0f11ec409c&aid=304142&ss=Bangalore&ssne=Bangalore&ssne_untouched=Bangalore&lang=en-gb&src=index&dest_id=-2090174&dest_type=city&checkin=2024-06-18&checkout=2024-06-19&group_adults=1&no_rooms=1&group_children=0&nflt=distance%3D3000",
        "sec-ch-ua": "\"Brave\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "x-booking-context-action-name": "searchresults_irene",
        "x-booking-context-aid": "304142",
        "x-booking-csrf-token": "eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJjb250ZXh0LWVucmljaG1lbnQtYXBpIiwic3ViIjoiY3NyZi10b2tlbiIsImlhdCI6MTcxODcwNzI1NywiZXhwIjoxNzE4NzkzNjU3fQ.gA_WWPhKkgTxDbcyKB-uFUsf_obvRlbvoXZdZFmcJ6EkASNrqdWTR52ltzPSWG_WgOBQBZYGklU3KfhgMTWldg",
        "x-booking-et-serialized-state": "E2VhNDBFc4_90QQbS9aUekVBL5O2uMzHdM99N6US3R1fVugRNyessdEVjxWsuup9I",
        "x-booking-pageview-id": "cd2e4b1c6a810062",
        "x-booking-site-type-id": "1",
        "x-booking-topic": "capla_browser_b-search-web-searchresults"
    }

    try:
        response = requests.post(url, headers=headers, data=body)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None

def extract_body():
    """Extract the body from the Postman collection"""
    
    try:
        with open('PL_SDE_Code_Test.postman_collection.json', 'r') as file:
            data = json.load(file)
        
        for item in data['item']:
            if 'request' in item:
                return item['request']['body']['raw']
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"An error occurred while extracting the body: {e}")
        return None

def configure_body(body, checkin_date, checkout_date, address, lat, lon, page_size):
    """Configure the body with the required parameters"""
    
    try:
        body = json.loads(body)
        body['variables']['input']['dates']['checkin'] = checkin_date
        body['variables']['input']['dates']['checkout'] = checkout_date
        body['variables']['input']['location']['searchString'] = address
        body['variables']['input']['location']['latitude'] = lat
        body['variables']['input']['location']['longitude'] = lon
        body['variables']['input']['pagination']['rowsPerPage'] = page_size
        return json.dumps(body)
    except (json.JSONDecodeError, KeyError) as e:
        print(f"An error occurred while configuring the body: {e}")
        return None

def parse_listings(data):
    """Parse the listings data and return a list of parsed data"""
    
    try:
        listings = data['data']['searchQueries']['search']['results']
        parsed_data = []
        base_url = "https://www.booking.com/hotel/in/" # Replace with appropriate country code
        for listing in listings:
            listing_id = listing['basicPropertyData']['id']
            listing_title = listing['displayName']['text']
            page_name = listing['basicPropertyData']['pageName']
            amount_per_stay = listing['priceDisplayInfoIrene']['displayPrice']['amountPerStay']['amount'].lstrip("US")
            listing_url = f"{base_url}{page_name}.html"
            parsed_data.append([listing_id, listing_title, page_name, amount_per_stay, listing_url])
        return parsed_data
    except (KeyError, TypeError) as e:
        print(f"An error occurred while parsing the listings: {e}")
        return []

def write_to_csv(data, filename="listings.csv"):
    """Write the parsed data to a CSV file"""
    
    headers = ["Listing ID", "Listing Title", "Page Name", "Amount Per Stay", "Listing URL"]
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)
    except IOError as e:
        print(f"An error occurred while writing to CSV: {e}")

def main():
    # Hardcoded values for testing
    address = "Pune"
    lat = 18.516726
    lon = 73.856255
    page_size = 50
    checkin_date = "2025-01-01"
    checkout_date = "2025-01-02"
    body = extract_body()
    if body:
        body = configure_body(body, checkin_date, checkout_date, address, lat, lon, page_size)
        if body:
            data = fetch_data(body)
            if data:
                parsed_data = parse_listings(data)
                write_to_csv(parsed_data)
                
                
def app_flask(params):
    address = str(params['address'])
    lat = float(params['lat'])
    lon = float(params['lon'])
    page_size = int(params['page_size'])
    checkin_date = str(params['checkin_date'])
    checkout_date = str(params['checkout_date'])
    body = extract_body()
    if body:
        body = configure_body(body, checkin_date, checkout_date, address, lat, lon, page_size)
        if body:
            data = fetch_data(body)
            if data:
                parsed_data = parse_listings(data)
                write_to_csv(parsed_data)
                return parsed_data
            else:
                return None
        else:
            return None
    else:
        return None

# if __name__ == "__main__":
#     main()