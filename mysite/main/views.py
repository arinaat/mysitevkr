from django.shortcuts import render


def Home(request):
    return render(request, 'main/index.html')

def Help(request):
    return render(request, 'main/help.html')




