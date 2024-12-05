from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import JSONField

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.course_name} ({self.course_code})"

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    rating = models.IntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not (1 <= self.rating <= 5):
            raise ValidationError('Rating must be between 1 and 5.')

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"Feedback by {self.user.username} for {self.course}"

class FeedbackMetadata(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    metadata = JSONField()

    def __str__(self):
        return f"Metadata for Feedback ID {self.feedback.id}"
