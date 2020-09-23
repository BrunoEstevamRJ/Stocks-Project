from django.shortcuts import render

# Create your views here. QUOTES

def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})

