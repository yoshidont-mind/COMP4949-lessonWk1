from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView

def homePageView(request):
    return render(request, 'home.html')

def aboutPageView(request):
    # return request object and specify page.
    return render(request, 'about.html')

def tatsuyaPageView(request):
    return render(request, 'tatsuya.html')

def homePageView(request):
    # return request object and specify page.
    return render(request, 'home.html', {
        'mynumbers':[1,2,3,4,5,6,],
        'firstName': 'Tatsuya',
        'lastName': 'Yoshida',
    })
