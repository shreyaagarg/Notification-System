from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from accounts.models import Faculty


def is_member(user):
    return user.groups.filter(name='Faculty').exists()

@user_passes_test(is_member,login_url='/accounts/FacLogIn')
@login_required(login_url='/accounts/FacLogIn')
def FacHome(request , fac_id):
    user = get_object_or_404(User , pk=fac_id)
    object = Faculty.objects.get(user=user)
    print(user.groups.all())
    return render(request, 'Notification/FacHome.html' , { 'object': object , 'faculty':user})