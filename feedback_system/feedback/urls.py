# feedback/urls.py

from django.urls import path
from . import views  # Import views from the feedback app

urlpatterns = [
    path('submit/', views.submit_feedback, name='submit_feedback'),  # Submit feedback view
    path('success/', views.success, name='success'),  # Success page after feedback submission
]
