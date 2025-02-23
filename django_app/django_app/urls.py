from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),    # e.g. /api/services/
    path('api/users/', include('users.urls')),  # e.g. /api/users/login
]
