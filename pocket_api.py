import pocket
import subprocess

# Consumer key and redirect URI
consumer_key = "112121-e1ca9fd80f33ca66b7bf308"
redirect_uri = "https://fviccia.github.io/odin-recipes/"

# Step 1: Get the request token
try:
    request_token = pocket.Pocket.get_request_token(
        consumer_key=consumer_key, redirect_uri=redirect_uri
    )
except Exception as e:
    print(f"Error getting request token: {e}")
    raise

# Step 2: Redirect user to Pocket's authorization page
auth_url = pocket.Pocket.get_auth_url(code=request_token, redirect_uri=redirect_uri)
print(f"Please visit the following URL to authorize the application: {auth_url}")

# You can open the URL in the browser (if using a script) using subprocess or another method
# subprocess.run(['xdg-open', auth_url])  # For Linux
# subprocess.run(['open', auth_url])  # For MacOS
# subprocess.run(['start', auth_url], shell=True)  # For Windows

# Pause the script here until the user authorizes the app in the browser
input("Press Enter after you have authorized the application...")

# Step 3: Exchange request token for access token
try:
    user_credentials = pocket.Pocket.get_credentials(
        consumer_key=consumer_key, code=request_token
    )
    access_token = user_credentials["access_token"]
    print(f"Access token: {access_token}")
except Exception as e:
    print(f"Error getting access token: {e}")
    raise

# Step 4: Create a Pocket instance and perform actions
try:
    pocket_instance = pocket.Pocket(consumer_key, access_token)
    # Get items from Pocket account
    response = pocket_instance.get()
    print(response)
except Exception as e:
    print(f"Error interacting with Pocket API: {e}")
    raise
