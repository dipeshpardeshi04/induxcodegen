import requests
from django.conf import settings


# Function to get the Figma file data
def get_figma_file_data(figma_file_id, access_token):
    url = f'https://api.figma.com/v1/files/{figma_file_id}'
    headers = {
        'X-Figma-Token': access_token
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Returning the full JSON response
    else:
        raise Exception(f"Error fetching Figma data: {response.text}")


# Function to send the Figma data to Gemini API to generate Angular code
def generate_angular_code(figma_data):
    api_key = settings.GEMINI_API_KEY
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}'
    headers = {
        'Content-Type': 'application/json'
    }

    # Better prompt for separate Angular files
    prompt_text = (
        "From the following Figma JSON data, generate Angular component code split into separate files:\n\n"
        "1. component.ts\n"
        "2. component.html\n"
        "3. component.css\n\n"
        "Each file content should be clearly separated in your response like:\n"
        "--- component.ts ---\n<code here>\n\n"
        "--- component.html ---\n<code here>\n\n"
        "--- component.css ---\n<code here>\n\n"
        "Here is the Figma JSON:\n"
        f"{figma_data}"
    )

    data = {
        "contents": [
            {
                "parts": [{"text": prompt_text}]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        try:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            raise Exception("Unexpected Gemini API response structure.")
    else:
        raise Exception(f"Error from Gemini API: {response.text}")

# Function to save the Angular code to a file
def save_angular_code_to_file(code, filename):
    with open(filename, 'w') as file:
        file.write(code)
