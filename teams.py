import requests
import json

# Replace this with your Incoming Webhook URL
webhook_url = "YOUR_WEBHOOK_URL_HERE"

# Define the message payload
message_payload = {
    "text": "Hello, this is a test message from Python with improved error handling!"
}

try:
    # Attempt to send the message
    response = requests.post(
        url=webhook_url,
        headers={"Content-Type": "application/json"},
        data=json.dumps(message_payload),
        timeout=10  # Adding a timeout to avoid hanging
    )
    
    # Check the response status code
    response.raise_for_status()  # This will raise an HTTPError for bad responses (4xx or 5xx)

    print("Message sent successfully!")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    print(f"Response content: {response.text}")

except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}")

except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error occurred: {timeout_err}")

except requests.exceptions.RequestException as req_err:
    print(f"An error occurred: {req_err}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
