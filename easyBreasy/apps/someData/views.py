from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Client
from django.contrib.auth import authenticate, logout, login as log


class ClientView(ListView):
    model = Client
    context_object_name = 'clients'
    template_name = 'someData/list_client.html'

class ClientDetailView(DetailView):
    model = Client
    context_object_name = 'client'
    template_name = 'someData/detail_client.html'

def login(request):
    post = request.POST
    username = post.get('username')
    password = post.get('password')
    user = authenticate(username=username, password=password)
    if user:
        log(request, user)
        return redirect('/')
    # print 'ok'


def exit(request):
    logout(request)
    return redirect('/')
