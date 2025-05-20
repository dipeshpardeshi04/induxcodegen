from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .utils import get_figma_file_data, generate_angular_code
from decouple import config
import json
import re
import io
import zipfile

def home(request):
    return HttpResponse("Welcome to the homepage! ->  http://127.0.0.1:8000/generate-angular-code/") 

def get_design_code(request):
    # figma_file_id = "IIpRorWOueRQMMzAKoWfuY"
    # figma_file_id = "TemBQUyFUDC8jmHM2S2UCk"
    figma_file_id = request.GET.get('file_id')
    figma_access_token = settings.FIGMA_ACCESS_TOKEN
    # page_name = request.GET.get('page', 'Page 1')  # Page name to target
    page_name = request.GET.get('page')
    if not figma_file_id or not page_name:
        return HttpResponse("Missing 'file_id' or 'page' parameter.", status=400)

    try:
        # Step 1: Get and clean Figma file JSON
        figma_data = get_figma_file_data(figma_file_id, figma_access_token)
        figma_data = clean_figma_data(figma_data)

        # Step 2: Get the specific page data
        pages = figma_data.get('document', {}).get('children', [])
        selected_page = None
        for page in pages:
            if page.get('name') == page_name:
                selected_page = page
                break

        if not selected_page:
            return HttpResponse(f"Page '{page_name}' not found in Figma file.", status=404)

        # Step 3: Iterate through each frame in the page
        frames = selected_page.get('children', [])
        output_summary = ""

        

        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            for frame in frames:
                frame_name = frame.get('name', 'unnamed_frame').replace(' ', '_')
                try:
                    angular_code = generate_angular_code(frame)
                    file_name = f"{frame_name}.ts"
                    
                    # Write each generated code as a file inside the ZIP archive
                    zip_file.writestr(file_name, angular_code)

                except Exception as e:
                    # You can log error or ignore frames that failed
                    print(f"Error generating code for frame '{frame_name}': {e}")

        zip_buffer.seek(0)

        # Send ZIP file as a response
        response = HttpResponse(zip_buffer.read(), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename="{page_name.replace(" ", "_")}_angular_code.zip"'

        return response


    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)


def get_page_data_from_figma(figma_data, page_name, frame_name):
    """
    Extract specific frame/component from a given page in Figma JSON.
    
    figma_data: Full Figma file JSON (dict)
    page_name: Name of the page in Figma
    frame_name: Name of the frame/component inside that page
    
    Returns the JSON of the frame/component if found, else None
    """
    pages = figma_data.get('document', {}).get('children', [])
    print("Inter")
    for page in pages:
        print("for lop")
        if page.get('name') == page_name:
            # Found the page
            print("pages found")
            frames = page.get('children', [])
            for frame in frames:
                print(frame.get('name'))
                if frame.get('name') == frame_name:
                    
                    # print(frame)
                    return frame
    return None



def print_page_names(figma_data):
    pages = figma_data.get('document', {}).get('children', [])
    for page in pages:
        print(page.get('name'))



def clean_figma_data(figma_data):
    # Dump to string, clean it, then load back to dict
    json_str = json.dumps(figma_data, ensure_ascii=False)
    clean_str = re.sub(r'[^\x00-\x7F]+', '', json_str)
    return json.loads(clean_str)  # Convert back to dict

def clean_code(code):
    return code.replace("```typescript", "").replace("```", "").strip()
