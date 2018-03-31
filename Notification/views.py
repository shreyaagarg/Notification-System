from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

@login_required(login_url='/accounts/FacLogIn')
def FacHome(request , fac_id):

    faculty = get_object_or_404(User , pk=fac_id)
    print(faculty)
    return HttpResponse("Hello There. I am Id: " + str(fac_id))