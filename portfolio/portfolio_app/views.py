from django.shortcuts import render
from .models import Project

def index(request):
    projects = Project.objects.all()[0:9]

    context_dict = {'projects': projects}
    
    return render(request, 'portfolio/index.html', context_dict)