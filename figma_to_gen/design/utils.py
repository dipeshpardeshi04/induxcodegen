import requests
from django.conf import settings
from decouple import config

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
    api_key = config('GEMINI_API_KEY')
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}'
    headers = {
        'Content-Type': 'application/json'
    }

    # Better prompt for separate Angular files
    prompt_text = (
    "From the following Figma JSON data, generate a complete Angular component in a single code block.\n"
    "Include the HTML, CSS (inside the component or as styles), and TypeScript code.\n"
    "Do NOT provide any explanation or markdown formatting.\n"
    "The component should be named appropriately (e.g., HomeComponent), but feel free to name it based on the design context.\n"
    "Replace any SVGs or icons with random image URLs (like Unsplash), keeping the layout intact.\n"
    "Make the UI professional, clean, modern, and fully responsive.\n"
    "Ensure all styling is present (in the component or inline styles) — no external CSS frameworks unless necessary.\n"
    "Include simple interactivity like click events or hover animations where appropriate.\n"
    "Make sure the code is well-structured, production-ready, and works directly inside an Angular project.and plz give always in same structure, do not change it \n\n"
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
# def save_angular_code_to_file(code, filename):
#     with open(filename, 'w') as file:
#         file.write(code)
