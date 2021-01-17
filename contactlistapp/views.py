from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def addContact(request):
    return render(request, 'new.html')
