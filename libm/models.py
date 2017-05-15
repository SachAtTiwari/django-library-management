from django.db import models

# Create your models here.

class AdminInfo(models.Model, dict):
    username = models.CharField(max_length=100,default='admin')
    password = models.CharField(max_length = 100, default='admin')

class StudentInfo(models.Model, dict):
    student_name = models.CharField(max_length=100,default=None)
    university_roll_no = models.IntegerField(default=None)
    student_department = models.CharField(max_length=100,default=None)
    #issued_book_name = models.CharField(max_length = 100, default=None)
    no_of_books_issued = models.IntegerField(default=None)
    fine = models.IntegerField(default=None)

class TeacherInfo(models.Model, dict):
    t_name = models.CharField(max_length=100,default=None)
    eid = models.IntegerField(default=None)
    teacher_department = models.CharField(max_length=100,default=None)
    #issued_book_name = models.CharField(max_length = 100, default=None)
    no_of_books_issued = models.IntegerField(default=None)
    fine = models.IntegerField(default=None)

class IssuedBook(models.Model, dict):
    book_name = models.CharField(max_length=100,default=None)
    assignedTo = models.CharField(max_length = 100, default=None)
    roll_no = models.IntegerField(default=None)
    lendPeriod_to = models.DateField(max_length = 100, default=None)
    lendPeriod_from = models.DateField(max_length = 100, default=None)

class AvailableBook(models.Model, dict):
    book_name = models.CharField(max_length=100,default=None)
    Author_name = models.CharField(max_length = 100, default=None)
    Department = models.CharField(max_length = 100, default=None)

class SignUpSt(models.Model,dict):
    university_roll_no = models.IntegerField(default=None)
    student_name = models.CharField(max_length=100,default=None)
    password = models.CharField(max_length=100,default=None)
    password_confirm = models.CharField(max_length=100,default=None)

class SignUpT(models.Model,dict):
    eid = models.IntegerField(default=None)
    t_name = models.CharField(max_length=100,default=None)
    password = models.CharField(max_length=100,default=None)
    password_confirm = models.CharField(max_length=100,default=None)
