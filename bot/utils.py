import logging
import os
import json

# Configure logging
logging.basicConfig(level=logging.INFO)

def load_user_profile():
    if os.path.exists('assets/user_profile.json'):
        with open('assets/user_profile.json', 'r') as file:
            return json.load(file)
    return {"name": "User", "preferences": {}}

def save_user_profile(data):
    with open('assets/user_profile.json', 'w') as file:
        json.dump(data, file)
    logging.info("User profile saved successfully.")

def log_error(error_message):
    logging.error(f"Error: {error_message}")
