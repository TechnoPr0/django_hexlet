from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse
# def index(request):
# return render(request, 'base.html', context={'who' : 'kIRILL'})


"""class HomePage(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'Kirill'
        return context"""


def index(request):
    uri = reverse("article", args=["python", 42])
    return redirect(uri)


def about(request):
    return render(request, 'base_about.html')
