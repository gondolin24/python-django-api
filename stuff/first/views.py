from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("was it that easy to make an endpoint?!?!")
    # return render(request,'post/index.html')
