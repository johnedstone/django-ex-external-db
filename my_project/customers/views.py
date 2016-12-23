import os

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView

from .models import Customer

class CustomerListView(ListView):
    model = Customer

def health(request):
    return HttpResponse('health check')

def index(request):
    # return HttpResponseRedirect(reverse('customers:list'))
    hostname = os.getenv('HOSTNAME', 'unknown')
    
    return render(request, 'customers/index.html', {
        'hostname': hostname,
        })
