from django.shortcuts import render
from django.views import generic, View
from .models import Request

# Create your views here.
class RequestList(generic.ListView):
    model = Request
    queryset = Request.objects.filter(active=True).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
