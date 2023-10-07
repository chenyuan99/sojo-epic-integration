import requests

# Set up the necessary variables
base_url = "<https://api.epic.com>"
client_id = "<your_client_id>"
client_secret = "<your_client_secret>"
access_token_url = f"{base_url}/oauth2/token"
api_endpoint = "<api_endpoint>"
patient_id = "<patient_id>"

# Step 1: Obtain an access token
data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret
}
response = requests.post(access_token_url, data=data)
access_token = response.json()["access_token"]

# Step 2: Call the Epic API endpoint
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}
response = requests.get(f"{base_url}/{api_endpoint}/{patient_id}", headers=headers)

# Step 3: Process the response
if response.status_code == 200:
    data = response.json()
    # Process the data as needed
    print(data)
else:
    print("Error:", response.status_code)
