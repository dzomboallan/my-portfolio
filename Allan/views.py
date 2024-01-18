from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Project

# Create your views here.
def index(request):
    home = Home.objects.latest('updated')
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)
    categories = Category.objects.all()
    projects = Project.objects.all()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': projects,
    }

    return render(request, 'index.html', context)
