from django.shortcuts import render, redirect
from .models import Course, Feedback
from .forms import FeedbackForm

def submit_feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Adjust as needed
    else:
        form = FeedbackForm()

    courses = Course.objects.all()  # Query all courses to populate dropdown
    return render(request, 'submit_feedback.html', {'form': form, 'courses': courses})
