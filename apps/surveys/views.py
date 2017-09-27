# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, 'surveys/index.html')

def result(request):
    return render(request, 'surveys/result.html')

def process(request):
    if 'count' not in request.session:
        request.session['count'] = 0

    request.session['name'] = request.GET['name']
    request.session['location'] = request.GET['location']
    request.session['language'] = request.GET['language']
    request.session['comment']= request.GET['comment']

    request.session['count'] += 1
    
    return redirect('/result')
