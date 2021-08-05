from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from bbsapp.models import *
from django.db.models import Q

def bbs(request):
    
    return render(request,'bbspage.html',locals())

