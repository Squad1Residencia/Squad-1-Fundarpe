from django.shortcuts import render

def login_view(request):
    return render(request, 'index.html')