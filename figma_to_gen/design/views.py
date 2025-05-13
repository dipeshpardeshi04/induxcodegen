from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .utils import get_figma_file_data, generate_angular_code, save_angular_code_to_file
from decouple import config


def home(request):
    return HttpResponse("Welcome to the homepage! ->  http://127.0.0.1:8000/generate-angular-code/") 

def get_design_code(request):
    # Static data for now (replace with real ones later)
    figma_file_id = "IIpRorWOueRQMMzAKoWfuY"
    figma_access_token = settings.FIGMA_ACCESS_TOKEN
    gemini_api_key = settings.GEMINI_API_KEY

    try:
        # Step 1: Get Figma data
        figma_data = get_figma_file_data(figma_file_id, figma_access_token)
        # print(figma_data)
        # Step 2: Generate Angular code
        angular_code = generate_angular_code(figma_data)

        # Step 3: Save the Angular code to a file
        file_name = "generated_angular_code.ts"
        save_angular_code_to_file(angular_code, file_name)

        # Check file exists before proceeding
        try:
            with open(file_name, 'r') as file:
                content = file.read()
                response = HttpResponse(content, content_type='application/typescript')
                # response['Content-Disposition'] = f'attachment; filename={file_name}'
                print(f"Response type: {type(response)}")  # Log the response type
                return response
        except FileNotFoundError:
            return HttpResponse("Error: Generated file not found.", status=404)

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
