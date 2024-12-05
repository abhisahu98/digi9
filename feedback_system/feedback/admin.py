from django.contrib import admin
from .models import User, Course, Feedback, FeedbackMetadata

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Feedback)
admin.site.register(FeedbackMetadata)
