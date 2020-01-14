from django.shortcuts import render
from subprocess import run, check_output
from django.http import HttpResponse
from .models import SHell
from rest_framework import viewsets
from .serializer import SHell_Serializer


# Create your views here.


def home(request):
    return render(request, "home.html")


def command(request, c_id):
    c_data = check_output(['ls'], shell=True)
    # x=[x for x in c_data.split('')]
    return HttpResponse(check_output(['ls'], shell=True))


def command_out(request, command):
    sh = SHell.objects.all()
    return HttpResponse(sh)


'''
creating the viewset for rest api
view sets as the name implies create a class that contains functionality related with a set of views.
in single viewset class we can have multiple views.
so that the regular get and post methods doesn't work here so different methods are being used in the django 
rest framework view sets that are

    list – list all elements, serves GET to /api/subscriber
    create – create a new element, serves POST to /api/subscriber
    retrieve – retrieves one element, serves GET to /api/subscriber/1
    update and partial_update – updates single element, handles PUT/PATCH to /api/subscriber/1
    destroy – deletes single element, handles DELETE to /api/subscriber/1

'''


class shell_viewset(viewsets.ModelViewSet):
    serializer_class = SHell_Serializer
    queryset = SHell.objects.all()

