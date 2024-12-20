import json

# Load the JSON data
with open('PL_SDE_Code_Test.postman_collection.json', 'r') as file:
    data = json.load(file)

# Extract the body

def extract_body():
    with open('PL_SDE_Code_Test.postman_collection.json', 'r') as file:
        data = json.load(file)
    
    for item in data['item']:
        if 'request' in item:
            return item['request']['body']['raw']


def extract_dates(data):
    checkin = data['item'][0]['request']['body']['raw']
    checkin_date = json.loads(checkin)['variables']['input']['dates']['checkin']
    checkout_date = json.loads(checkin)['variables']['input']['dates']['checkout']
    
    return checkin_date, checkout_date

# body = extract_body(data)

def configure_body(body, checkin_date, checkout_date, address, lat, lon, page_size):
    body = json.loads(body)
    body['variables']['input']['dates']['checkin'] = checkin_date
    body['variables']['input']['dates']['checkout'] = checkout_date
    body['variables']['input']['location']['searchString'] = address
    body['variables']['input']['location']['latitude'] = lat
    body['variables']['input']['location']['longitude'] = lon
    body['variables']['input']['pagination']['rowsPerPage'] = page_size
    return json.dumps(body)

# body = configure_body(body, checkin_date='2025-01-01', checkout_date='2025-02-02', address='Mumbai', lat=19.0760, lon=72.8777, page_size=50)

