from django.shortcuts import render
import requests
# Create your views here.

def show(request):
    response = requests.get('http://127.0.0.1:8000/web/students/')
    todos = response.json()
    return render(request, 'index.html', {'user': todos})