# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.

def index(request):
    return render(request, 'session_words/index.html')

def add(request):
    if 'activity' not in request.session:
        request.session['activity'] = ''
    #add entire string to activity -- each line will be a word
    request.session['the_time'] = strftime('%H:%M:%S%p, %m %d, %Y', gmtime())
    request.session['add_me'] = "<span style='color:" + request.GET['color'] + "'</span>" + request.GET['new_word']
    request.session['add_me'] += ' - added on '
    request.session['add_me'] += request.session['the_time']

    if 'big_font' in request.GET:
        request.session['add_me'] = "<h1>" + request.session['add_me'] + "</h1>"
    else:
        request.session['add_me'] = "<p>" + request.session['add_me'] + "</p>"

    request.session['activity'] += request.session['add_me']
    
    return redirect('/session_words')

def clear(request):
    del request.session['activity']
    return redirect('/session_words')
