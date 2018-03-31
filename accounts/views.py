from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Signup_student_form, Signup_faculty_form
from DepUpdate.models import AuthStudent,AuthFaculty

def StuSignUpView(request):

    if request.method == "POST":
        form = Signup_student_form(request.POST)
        try:
            values = request.POST
            object = AuthStudent.objects.get(SID = values['Student_ID'])

            if ( values['Student_ID'] , values['Name'] , values['DOB'] , values['Branch'] , values['Year_Of_Study']) == ( object.SID , object.Name , object.DOB.isoformat() , object.branch , object.year ):

                if form.is_valid():

                    instance = form.save(commit=False)
                    username = values['Student_ID']
                    password = values.get('password',None)
                    email = values['email']

                    user = User.objects.create_user(username=username, email=email)
                    user.set_password(password)
                    user.save()
                    my_group = Group.objects.get(name="Students")
                    user.groups.add(my_group)
                    instance.user = user
                    instance.save()


                    user = authenticate(username=username,password=password)
                    login(request,user)

                    return HttpResponse("Hello User is created")



            else:
                error_messages = """Your are not an authenticated member of this institution.
                Kindly contact your respective department"""
                return render(request, 'accounts/StuSignUp.html', {'form': form , 'error_messages' : error_messages})

        except Exception as e:
            print(e)
            error_messages = """Your are not an authenticated member of this institution.
                Kindly contact your respective department"""
            return render(request, 'accounts/StuSignUp.html', {'form': form,  'error_messages' : error_messages})

    else:
        form = Signup_student_form()

    return render(request , 'accounts/StuSignUp.html' , {'form' : form})


def StuLogInView(request):
    if request.method == "POST":

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            user = form.get_user()
            login(request,user)
            return HttpResponse("Login done")
    else:
        form = AuthenticationForm()

    return render(request , 'accounts/StuLogIn.html' , {'form':form})


def FacSignUpView(request):
    if request.method == "POST":
        form = Signup_faculty_form(request.POST)
        try:
            values = request.POST
            object = AuthFaculty.objects.get(SID = values['Faculty_ID'])

            if ( values['Faculty_ID'] , values['Name'] , values['Department'] , values['Designation'] ) == ( object.FID , object.Name , object.Department , object.Designation ):

                if form.is_valid():

                    instance = form.save(commit=False)
                    username = values['Student_ID']
                    password = values.get('password',None)
                    email = values['email']

                    user = User.objects.create_user(username=username, email=email)
                    user.set_password(password)
                    user.save()
                    my_group = Group.objects.get(name="Faculty")
                    user.groups.add(my_group)
                    instance.user = user
                    instance.save()

                    user = authenticate(username=username,password=password)
                    login(request,user)
                    print("Hello")

                    return HttpResponse("Hello There")



            else:
                error_messages = """Your are not an authenticated member of this institution.
                Kindly contact your respective department"""
                return render(request, 'accounts/FacSignUp.html', {'form': form , 'error_messages' : error_messages})

        except Exception as e:
            print(e)
            error_messages = """Your are not an authenticated member of this institution.
                Kindly contact your respective department"""
            return render(request, 'accounts/FacSignUp.html', {'form': form,  'error_messages' : error_messages})

    else:
        form = Signup_faculty_form()

    return render(request , 'accounts/FacSignUp.html' , {'form' : form})


def FacLogInView(request):
    if request.method == "POST":

        form = AuthenticationForm(data=request.POST)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():

            user = form.get_user()
            login(request,user)
            print("1")
            return redirect('Notification:FacHome' , fac_id= request.user.id)
    else:
        print("2")
        form = AuthenticationForm()
    print("3")
    return render(request , 'accounts/FacLogIn.html' , {'form':form})


@login_required(login_url='/accounts/StuSignUp')
def Proflogout(request):

    logout(request)

    return redirect('accounts:StuSignUp')