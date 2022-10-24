from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class cspView(TemplateView):
    template_name='csp.html'