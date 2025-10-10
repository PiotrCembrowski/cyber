from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'cyber/index.html')

def tasks(request):
    return render(request, 'cyber/tasks.html')
