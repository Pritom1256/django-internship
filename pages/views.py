from django.shortcuts import render

def home(request):
    context = {
        'name': 'Pritom',
        'course': 'django internship training',
        'skills': ['Python', 'Django', 'HTML', 'CSS']
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {
        'description': 'This page demonstrates Django templating.',
        'age': 20
    })