# Django Internship Project

---

## Project Overview
This project is a simple Django web application created for internship learning. It demonstrates Django setup, app creation, URL routing, template inheritance, filters, tags, and dynamic data rendering using views and templates.

---

#  Code Snippets

---

##  views.py

```python
from django.shortcuts import render

def home(request):
    context = {
        'name': 'Pritom',
        'course': 'Django Internship Training',
        'skills': ['Python', 'Django', 'HTML', 'CSS']
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {
        'description': 'This page demonstrates Django template system.',
        'age': 20
    })

project urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]

app urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]

Template Inheritance Explanation:
In this project, template inheritance is used to avoid repeating HTML code.

base.html is the parent template
home.html and about.html extend base.html..
This allows a common layout (header and footer) to be reused.
Filters and Tags Explanation:
Filters Used:
upper → converts text to uppercase
title → formats text properly

Example:{{ name|upper }}
Tags Used:
##{% for %} → loop through list
##{% if %} → conditional logic

Data Flow Explanation:
views.py → context → templates → browser

Step by step:
1)views.py sends data using context dictionary
2)template receives data
3)Django renders HTML dynamically
4)browser displays final output

Conclusion:
This project helped to understand:

##Django project structure
##App creation
##URL routing
##Template inheritance
##Filters and tags usage
##Data passing from backend to frontend
