
from django.contrib import admin
from django.urls import path, include
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('app.urls')),
    path('api/auth/', include('rest_framework.urls')),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf'))
]

# http://localhost:8000/auth/convert-token