import requests

# Replace with your Stack Exchange API key
API_KEY = "<your-api-key>"

# The URL of the Stack Exchange API
API_URL = "https://api.stackexchange.com/2.2"

# The topic you want to search for
TOPIC = "machine learning"

# The maximum number of results to return
MAX_RESULTS = 10

# Build the API query URL
query_url = f"{API_URL}/search?order=desc&sort=activity&tagged={TOPIC}&site=stackoverflow&filter=withbody&key={API_KEY}"

# Fetch the results from the API
response = requests.get(query_url)

# Parse the response as JSON
results = response.json()

# Print the questions and answers
for item in results["items"][:MAX_RESULTS]:
    print(item["title"])
    print(item["body"])
    print()
