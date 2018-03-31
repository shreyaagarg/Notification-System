from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


def FacHome(request , fac_id):

    faculty = get_object_or_404(User , pk=fac_id)

    return HttpResponse("Hello There. I am Id: " + str(fac_id))