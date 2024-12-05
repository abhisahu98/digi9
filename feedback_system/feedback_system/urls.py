# feedback_system/urls.py

from django.contrib import admin
from django.urls import path, include  # include is used to include other URL patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feedback/', include('feedback.urls')),  # Include URLs from the feedback app
]
