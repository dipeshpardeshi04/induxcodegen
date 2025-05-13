# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from design.views import generate_angular_code  # Import the view for this URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('design.urls')),
    path('design/generate-angular-code/', generate_angular_code, name='generate-angular-code'),
    path('figma/', include('design.urls')),  # Example if using an app 'figma'
    path('upload/', include('design.urls')),
    path('', include('design.urls')),  # Your home app, if defined
]
