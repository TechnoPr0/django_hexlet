from django.shortcuts import render
from django.views.generic.base import TemplateView
# def index(request):
# return render(request, 'base.html', context={'who' : 'kIRILL'})


class HomePage(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'Kirill'
        return context


def about(request):
    return render(request, 'base_about.html')
