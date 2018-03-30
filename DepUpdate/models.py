from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class AuthStudent(models.Model):

    branches = [
        ("aero" , "Aerospace"),
        ("civil", "Civil"),
        ("cse", "Computer Science"),
        ("ece", "Electronics & Communication"),
        ("elec", "Electrical"),
        ("mech", "Mechanical"),
        ("meta", "Materials & Metallurgical"),
        ("prod" , "Production & Industrial"),
    ]

    years = [
        ("1" , 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
    ]

    SID = models.CharField(max_length=8, blank=False , unique=True)
    Name = models.CharField(max_length=50)
    DOB = models.DateField()
    branch = models.CharField(max_length=4, choices=branches , default="aero")
    year = models.CharField(max_length=1,choices=years, default="1")

    def __str__(self):

        return self.SID


    class Meta:
        ordering = ['SID']

class course(models.Model):

    courselist = [
        ('CSN101', 'INTRODUCTION TO COMPUTER SCIENCE AND ENGINEERING'),
        ('CSN103', 'DIGITAL ELECTRONIC AND LOGIC DESIGN'),
        ('CSN201', 'DISCRETE STRUCTURES FOR COMPUTER SCIENCE'),
        ('CSN202', 'COMPUTER ARCHITECTURE AND ORGANIZATION'),
        ('CSN203', 'OBJECT ORIENTED PROGRAMMING'),
        ('CSN204', 'ANALYSIS AND DESIGN OF ALGORITHMS'),
        ('CSN206', 'ENGINEERING ANALYSIS '),
        ('CSN207', 'MICROPROCESSOR AND ITS APPLICATIONS'),
        ('CSN208', 'DATA BASE MANAGEMENT SYSTEM'),
        ('CSN210', 'COMPUTER '),
        ('CSN301', 'THEORY OF COMPUTATION'),
        ('CSN302', 'SOFTWARE ENGINEERING'),
        ('CSN303', 'WEB TECHNOLOGIES'),
        ('CSN304', 'COMPUTER GRAPHICS'),
        ('CSN305', 'ARTIFICIAL INTELLIGENCE'),
        ('CSN401', 'COMPILER DESIGN'),
        ('CSN402', 'SOFTWARE TESTING '),
        ('CSN403', 'SOFT COMPUTING'),
        ('CSN404', 'DIGITAL IMAGE PROCESSING'),
        ('CSN405', 'CLOUD COMPUTING'),
        ('CSN406', 'AGILE SOFTWARE DEVELOPMENT '),
        ('CSN407', 'Natural Language Processing'),
        ('CSN408', 'SOFTWARE PROJECT MAN'),
        ('CSN409', 'BIG DATA ANALYTICS'),
        ('CSN410', 'BIOINFORMATICS'),
        ('CSN411', 'NETWORK SECURITY'),
        ('CSN412', 'APPLIED CRYPTOGRAPHY'),
        ('CSN413', 'COMPUTER CRIME INVESTIGATION AND FORENSICS'),
        ('CSN414', 'BIOMETRIC SECURITY'),
        ('CSN415', 'Advanced'),
        ('CSN416', 'ADVANCED WIRELESS AND MOBILE NETWORKS'),
        ('CSN417', 'WIRELESS SENSOR NETWORKS'),
        ('CSN418', 'MOBILE COMPUTING'),
        ('CSN461', 'OBJECT ORIENTED PROGRAMMING'),
        ('CSN462', 'OPERATING SYSTEMS'),
        ('CSN463', 'WEB '),
        ('CSN421', 'MACHINE LEARNING'),
        ('CSN422', 'ADVANCED DATABASE SYSTEMS'),
        ('CSN423', 'ADVANCED SOFTWARE EN'),
        ('CSN424', 'ADVANCED ALGORITHM DESIGN AND ANALYSIS'),
        ('CSN425', 'ADVANCED COMPUTER ARCHITECTURE'),
        ('CSN431', 'DATA STRUCTURES '),
        ('CSN432', 'COMPUTER NETWORKS'),
        ('CSN433', 'COMPUTER CRIME INVESTIGATION AND FORENSICS'),
        ('CSN434', 'DATA BASE SYSTEMS'),
        ('CSN435', 'SOFTWARE ENGINEERING'),
        ('GSC101', 'ENVIRONMENTAL SCIENCES'),
        ('MAN101', 'MATHEMATICS I'),
        ('MAN103', 'PROBABILITY AND STATISTICS'),
        ('MAN105', 'VECTOR CALCULUS, FOURIER SERIES AND LAPLACE '),
        ('MAN106', 'PARTIAL DIFFERENTIAL EQUATIONS AND SPECIAL '),
        ('PYN101', 'OSCILLATIONS AND OPTICS'),
        ('PYN102', 'CONDENSED MATTER PHYSICS'),
        ('PYN ', 'MECHANICS'),
        ('PYN', 'ELECTROMAGNETIC THEORY'),
        ('CHN101', 'APPLIED CHEMISTRY'),
        ('CHN', 'PHYSICAL CHEMISTRY'),
        ('CHN', 'INORGANIC '),
        ('CHN', 'PHYSICAL CHEMISTRY'),
        ('HSS101', 'ETHICS AND SELF AWARENESS     '),
        ('HSS103', 'COMMUNICATION SKILLS (ADVANCED)'),
        ('HSS201', 'ECONOMICS'),
        ('HSS202', 'PSYCHOLOGY'),
        ('HSS203', 'SOCIOLOGY'),
        ('HSS204', 'FRENCH   '),
        ('HSM401', 'PRINCIPLES OF MANAGEMENT'),
        ('HSM102', 'BUSINESS ENVIRONMENT AND BUSINESS LAWS     '),
        ('HSM403', 'ENTREPRENEURSHIP AND PROJECT MANAGEMENT'),
        ('HSM405', 'MARKETING MANAGEMENT     '),
        ('HSM406', 'HUMAN RESOURCE MANAGEMENT     '),
        ('CSN104', 'COMPUTER PROGRAMMING (BASIC)'),
        ('CSN105', 'COMPUTER PROGRAMMING (ADVANCED)'),
        ('ESC101', 'ENGINEERING DRAWING '),
        ('ESC102', 'FLUID MECHANICS'),
        ('ESC103', 'INTRODUCTION TO MANUFACTURING'),
        ('ESC201', 'THERMODYNAMICS'),
        ('ESC202', 'ESSENTIALS OF INFORMATION TECHNOLOGY'),
        ('ESC203', 'MATERIALS SCIENCE'),
        ('ESC204', 'SOLID MECHANICS'),
        ('ESC205', 'INTRODUCTION TO ELECTRONICS'),
        ('ESC206', 'BASIC ELECTRICAL SCIENCES'),
        ('ESC207', 'MECHATRONICS'),
        ('ESC', 'MECHANICAL ENGINEERING DRAWING'),
        ('XXX', 'TECHNICAL COMMUNICATION'),
        ('MAN 401', 'OPERATIONS  RESEARCH'),
        ('PYN', 'ADVANCED PHYSICS '),
        ('PYN', 'CRYSTAL PHYSICS'),
        ('CHN401', 'MODERN INSTRUMENTAL METHODS OF CHEMICAL ANALYSIS'),
        ('HSM401', 'PRINCIPLES OF MANAGEMENT'),
        ('HSM402', 'BUSINESS ENVIRONMENT AND BUSINESS LAWS     '),
        ('HSM404', 'FINANCIAL MANAGEMENT     '),
        ('HSM405', 'MARKETING MANAGEMENT     '),
        ('HSM406', 'HUMAN RESOURCE MANAGEMENT     '),
        ('HSM431', 'MANAGING INNOVATION AND CHANGE     '),
        ('HSM432', 'BUSINESS RESEARCH '),
        ('MAN431', 'ALGEBRA '),
        ('MAN432', 'NUMBER THEORY '),
        ('MAN433', 'FOURIER SERIES AND INTEGRAL TRANSFORMS'),
        ('MAN434', 'CALCULUS OF VARIATIONS'),
        ('PYN', 'QUANTUM MECHANICS'),
        ('PYN', 'STATISTICAL PHYSICS'),
        ('PYN', 'NUCLEAR PHYSICS'),
        ('PYN', 'EXPERIMENTAL NUCLEAR PHYSICS'),
        ('PYN', 'X'),
        ('CHN', 'ANALYTICAL CHEMISTRY'),
        ('CHN', 'ENVIRONMENTAL CHEMISTRY'),
        ('CHN', 'RECENT ADVANCES IN CHEMICAL SCIENCES'),

    ]

    CourseID = models.CharField(max_length=7 )
    CourseName = models.CharField(max_length=50 , choices=courselist , default=None)
    Credits = models.IntegerField( validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ])



    def __str__(self):

        return self.CourseID

    def get_coursename(self, cno):

            lis = list(zip(*self.courselist))
            if cno in lis[0]:
                return lis[1][lis[0].index(cno)]
            else:
                return None


class AuthFaculty(models.Model):

    branches = [
        ("aero" , "Aerospace"),
        ("civil", "Civil"),
        ("cse", "Computer Science"),
        ("ece", "Electronics & Communication"),
        ("elec", "Electrical"),
        ("mech", "Mechanical"),
        ("meta", "Materials & Metallurgical"),
        ("prod" , "Production & Industrial"),
    ]

    designations = [("prof", "Professor"),
                   ("asso", "Associate Professor"),
                   ("assi", "Assistant Professor"),
                   ("inst", "Instructor")
                   ]

    FID = models.CharField(max_length=8, blank=False , unique=True)
    Name = models.CharField(max_length=50)
    Department = models.CharField(max_length=4, choices=branches , default="aero")
    Designation = models.CharField(max_length=4, choices=designations, default="prof")

    def __str__(self):

        return self.FID