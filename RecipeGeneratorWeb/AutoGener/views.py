from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'AutoGener/index.html')
