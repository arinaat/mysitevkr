from django.shortcuts import render

# Create your views here.
def tool1(request):
    return render(request, 'tool1.html')

def tools(request):
    return render(request, 'tools.html')