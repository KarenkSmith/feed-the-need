from django.shortcuts import render
from django.http import HttpResponse

# Views

# Home
def home(request):
  return render(request, 'index.html')

# About
def about(request):
  return render(request, 'about.html')