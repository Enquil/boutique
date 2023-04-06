from django.shortcuts import render


def index(request):
    '''
    View that returns index.html
    '''
    return render(request, 'home/index.html')
