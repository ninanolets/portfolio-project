from django.shortcuts import render

from .models import Job
# Create your views here.

def home(request):
    jobs = Job.objects # this will get all the job models into the database and turn them into python objects
    return render(request, 'jobs/home.html', {'jobs': jobs})

# Make homepage: this, together with url path
