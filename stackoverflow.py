import requests

# Set the parameters for the API call
params = {
    'site': 'stackoverflow',
    'sort': 'votes',
    'tagged': '<topic>',
}

# Make the API call
response = requests.get('https://api.stackexchange.com/2.2/questions', params=params)

# Extract the data from the response
data = response.json()

# Loop through the items in the data and print the question and answer
for item in data['items']:
    print(item['title'])
    for answer in item['answers']:
        print(answer['body'])
