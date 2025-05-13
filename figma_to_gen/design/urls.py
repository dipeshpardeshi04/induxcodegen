from django.urls import path
from .views import get_design_code, home  # ✅ import your actual Django view function

urlpatterns = [
    path('', home, name='home'),
    path('generate-angular-code/', get_design_code, name='generate_angular_code'),  # ✅ fix here
]
