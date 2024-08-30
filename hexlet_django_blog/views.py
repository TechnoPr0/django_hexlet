from django.shortcuts import render

def index(request):
    return render(request, 'base.html', context={'who' : 'kIRILL'})


def about(request):
    return render(request, 'base_about.html')