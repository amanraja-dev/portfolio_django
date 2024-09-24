from django.shortcuts import render, redirect , reverse
from django.contrib.auth import logout
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
import os

from apps.models import Profile

# Create your views here.
def home(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'project.html')

def education(request):
    return render(request, 'education.html')

def contact(request):
    return render(request, 'contact.html')

def skills(request):
    return render(request, 'skill.html')

def resume(request):
    return render(request, 'resume.html')

def feedback(request):
    return render(request, 'feedback.html')

def activity(request):
    return render(request, 'activity.html')



def signin(request):
    if request.method == 'GET':
        return redirect(reverse('social:begin', args=['google-oauth2']))

def signout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

# Download resume function
def download_resume(request):
    # Get the path to the PDF file
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'resumes', 'AMANRAJA_FULL_STACK_RESUME.pdf')
    
    # Check if the file exists
    if os.path.exists(pdf_path):
        # Open the PDF file in binary mode
        with open(pdf_path, 'rb') as pdf_file:
            # Create an HttpResponse object with the appropriate PDF content type
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            # Set the Content-Disposition header to force download
            response['Content-Disposition'] = 'attachment; filename="AMANRAJA_FULL_STACK_RESUME.pdf"'
            return response
    else:
        return HttpResponse("File not found")