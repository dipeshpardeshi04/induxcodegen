from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .utils import get_figma_file_data, generate_angular_code
import json
import re
import io
import zipfile
import time
import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return HttpResponse("Welcome to the homepage! ->  http://127.0.0.1:8000/generate-angular-code/?file_id=YOUR_FILE_ID")


def get_design_code(request):
    figma_file_id = request.GET.get('file_id')
    figma_access_token = settings.FIGMA_ACCESS_TOKEN
    page_name = request.GET.get('page')  # Optional

    if not figma_file_id:
        return HttpResponse("Missing 'file_id' parameter.", status=400)

    try:
        figma_data = get_figma_file_data(figma_file_id, figma_access_token)
        figma_data = clean_figma_data(figma_data)

        pages = figma_data.get('document', {}).get('children', [])

        # Auto-select first page if not provided
        if not page_name:
            if not pages:
                return HttpResponse("No pages found in the Figma file.", status=404)
            page_name = pages[0].get('name')
            print(f"[INFO] Automatically selected first page: {page_name}")

        selected_page = next((page for page in pages if page.get('name') == page_name), None)
        if not selected_page:
            return HttpResponse(f"Page '{page_name}' not found in Figma file.", status=404)

        frames = selected_page.get('children', [])
        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            for frame in frames:
                frame_name = frame.get('name', 'unnamed_frame').replace(' ', '_')
                success = False
                retry_attempts = 3

                for attempt in range(retry_attempts):
                    try:
                        angular_code = generate_angular_code(frame)
                        file_name = f"{frame_name}.ts"
                        zip_file.writestr(file_name, angular_code)
                        print(f"[✓] Successfully generated: {file_name}")

                        # Delay after success
                        time.sleep(10)
                        success = True
                        break

                    except Exception as e:
                        error_msg = str(e)
                        print(f"[✗] Error in frame '{frame_name}' (Attempt {attempt+1}): {error_msg}")

                        # Extract dynamic retry delay
                        retry_match = re.search(r'"retryDelay":\s*"(\d+)s"', error_msg)
                        delay = int(retry_match.group(1)) if retry_match else 10

                        print(f"[!] Waiting for {delay} seconds before retrying...")
                        time.sleep(delay)

                if not success:
                    print(f"[!] Skipping frame '{frame_name}' after {retry_attempts} failed attempts.")

        zip_buffer.seek(0)
        response = HttpResponse(zip_buffer.read(), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename="{page_name.replace(' ', '_')}_angular_code.zip"'
        return response

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)


def clean_figma_data(figma_data):
    json_str = json.dumps(figma_data, ensure_ascii=False)
    clean_str = re.sub(r'[^\x00-\x7F]+', '', json_str)
    return json.loads(clean_str)


def clean_code(code):
    return code.replace("```typescript", "").replace("```", "").strip()



def figma_json_to_code(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('Only POST allowed')

    try:
        data = json.loads(request.body)
        nodes = data.get('components', [])

        html_output = ""
        for node in nodes:
            html_output += render_component(node)

        return JsonResponse({
            'status': 'success',
            'generated_code': html_output
        })

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


# Helper function to render a component into HTML
def render_component(node):
    component = node.get("component", "div")
    styles = node.get("styles", {})
    style_string = "; ".join([f"{k}: {v}" for k, v in styles.items()])
    label = node.get("label", "")

    if component.lower() == "button":
        return f'<button style="{style_string}">{label}</button>\n'
    elif component.lower() == "input":
        return f'<input placeholder="{label}" style="{style_string}"/>\n'
    elif component.lower() == "text":
        return f'<p style="{style_string}">{label}</p>\n'
    else:
        return f'<div style="{style_string}">{label}</div>\n'