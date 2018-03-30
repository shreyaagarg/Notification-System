from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

branches = [
        ("aero", "Aerospace"),
        ("civil", "Civil"),
        ("cse", "Computer Science"),
        ("ece", "Electronics & Communication"),
        ("elec", "Electrical"),
        ("mech", "Mechanical"),
        ("meta", "Materials & Metallurgical"),
        ("prod", "Production & Industrial"),
    ]

class Student(models.Model):


    years = [
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
    ]

    Name = models.CharField(max_length=50)
    Student_ID = models.CharField(max_length=8, blank=False, unique=True)
    DOB = models.DateField(verbose_name="Date Of Birth" )
    Branch = models.CharField(max_length=4, choices=branches, default="aero")
    Year_Of_Study = models.CharField(max_length=1, choices=years, default="1")
    Address = models.CharField(max_length=300)
    Contact_Number = PhoneNumberField(blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE , default=None)

class Faculty(models.Model):

    designations = [  ("prof","Professor"),
                      ("asso" , "Associate Professor"),
                      ("assi" , "Assistant Professor"),
                      ("inst" , "Instructor")
    ]

    Name = models.CharField(max_length=50)
    Faculty_ID = models.CharField(max_length=8, blank=False, unique=True)
    Department =  models.CharField(max_length=4, choices=branches, default="aero")
    Contact_Number = PhoneNumberField(blank=False)
    Designation = models.CharField(max_length=4 , choices=designations , default="prof")
    Qualification = models.CharField(max_length=300)
    user = models.OneToOneField(User, on_delete=models.CASCADE , default=None)