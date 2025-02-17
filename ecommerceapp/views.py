from django.shortcuts import render

# Create your views here.
def index(request):     # Define a function called index that takes a request as an argument.
    return render(request, 'app/index.html')