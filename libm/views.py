from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from libm.models import *
import json
from django.core import serializers
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from django.views.decorators.cache import cache_control
import datetime
from datetime import date

from django.contrib import messages

# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
     try:
         return render_to_response('index.html', context_instance=RequestContext(request) )
     except KeyError:
         return render_to_response('index.html', context_instance=RequestContext(request))

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def tsignup(request):
     try:
         return render_to_response('tsignup.html' )
     except KeyError:
         return render_to_response('tsignup.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Tsignup(request):
    try:
       print "In tsignup ", request.method
       username = request.GET.get('tName')
       print "username", username
       eid = request.GET.get('eid')
       passwd = request.GET.get('pass')
       passwd_conf = request.GET.get('pass_confirm')

       print "password", passwd
       if username and passwd and passwd_conf and eid:
          print "passwordi inside", passwd
          sign_up_auth = TeacherInfo.objects.filter(t_name=username).filter(eid=eid)
          if sign_up_auth:
              print sign_up_auth
              signup_res = SignUpT.objects.filter(t_name=username).filter(password=passwd)
              print "login_res", signup_res
              if not signup_res:
                  signup = SignUpT()
                  signup.eid = eid
                  signup.t_name = username
                  signup.password_confirm = passwd_conf
                  signup.password = passwd
                  signup.save()
                  return redirect("/tlogin")
              else:
                  return redirect("/tsignup")
          else:
              return redirect("/tsignup")
       else:
           return redirect("/tsignup")
    except KeyError:
       pass



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def stSignUp(request):
     try:
         return render_to_response('stsignup.html' )
     except KeyError:
         return render_to_response('stsignup.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signup(request):
    try:
       print "In signup ", request.method
       username = request.GET.get('stName')
       print "username", username
       unroll = request.GET.get('unroll')
       passwd = request.GET.get('pass')
       passwd_conf = request.GET.get('pass_confirm')

       print "password", passwd
       if username and passwd and passwd_conf and unroll:
          print "passwordi inside", passwd
          sign_up_auth = StudentInfo.objects.filter(student_name=username).filter(university_roll_no=unroll)
          if sign_up_auth:
              print sign_up_auth
              signup_res = SignUpSt.objects.filter(student_name=username).filter(password=passwd)
              print "login_res", signup_res
              if not signup_res:
                  signup = SignUpSt()
                  signup.university_roll_no = unroll
                  signup.student_name = username
                  signup.password_confirm = passwd_conf
                  signup.password = passwd
                  signup.save()
                  return redirect("/stLogin")
              else:
                  return redirect("/stSignUp")
          else:
              return redirect("/stSignUp")
       else:
           return redirect("/stSignUp")
    except KeyError:
       pass

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def studentLogin(request):
    try:
       print "In st login ", request.GET
       unroll = request.GET.get('unroll')
       print "username", unroll
       paswd = request.GET.get('pass')
       print "password", paswd
       if unroll and paswd:
          print "passwordi inside", paswd
          login_res = SignUpSt.objects.filter(university_roll_no=unroll).filter(password=paswd)
          print "login_res", login_res
          if login_res:
              request.session['stuser'] = unroll
              return redirect("/stInfo")
          else:
              return redirect("/stLogin")
       else:
          return redirect("/stLogin")
    except KeyError:
          return redirect("/stLogin")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def TLogin(request):
    try:
       print "In t login ", request.GET
       eid = request.GET.get('eid')
       print "username", eid
       paswd = request.GET.get('pass')
       print "password", paswd
       if eid and paswd:
          print "passwordi inside", paswd
          login_res = SignUpT.objects.filter(eid=eid).filter(password=paswd)
          print "login_res", login_res
          if login_res:
              request.session['tuser'] = eid
              return redirect("/tInfo")
          else:
              return redirect("/tLogin")
       else:
          return redirect("/tLogin")
    except KeyError:
          return redirect("/tLogin")


#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def stInfo(request):
    try:
       stuser = request.session["stuser"]
       if stuser:
          print "user is", stuser
          addStudent = StudentInfo.objects.filter(university_roll_no=stuser) 
          print addStudent
          stuname = ""
          for i in addStudent:
             stuname = i.student_name
          updateFine = StudentInfo.objects.all()
          for fi in updateFine:
             fine_charged = calculate_fine(fi.university_roll_no)
             print "in stinfo", fine_charged
             fi.update(fine=fine_charged)
             #updateFine.save(force_update=True)
          return render_to_response('stinfo.html', {'addStudent':addStudent, 'stuser':stuser, 'stuname':stuname})
       else:
           return redirect("/stLogin")
           #return render_to_response('stinfo.html' )
    except KeyError:
           return redirect("/stLogin")


def TInfo(request):
    try:
       tuser = request.session["tuser"]
       if tuser:
          print "user is", tuser
          tinfo = TeacherInfo.objects.filter(eid=tuser) 
          print tinfo
          tname = ""
          for i in tinfo:
             t_name = i.t_name
          updateFine = TeacherInfo.objects.filter(eid=tuser)
          for fi in updateFine:
             fine_charged = calculate_fine(fi.eid)
             print "in tinfo", fine_charged
             fi.update(fine=fine_charged)
             #updateFine.save(force_update=True)
          return render_to_response('tinfo.html', {'tinfo':updateFine, 'tuser':tuser, 't_name':t_name})
       else:
           return redirect("/tlogin")
           #return render_to_response('stinfo.html' )
    except KeyError:
           return redirect("/tlogin")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def tLogin(request):
     try:
         return render_to_response('tlogin.html' )
     except KeyError:
         return render_to_response('tlogin.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def stLogin(request):
     try:
         return render_to_response('stlogin.html' )
     except KeyError:
         return render_to_response('stlogin.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
def avbooks(request):
     try:
        user = request.session["user"]
        if user:
           #print "user is", user
           avbooks = AvailableBook.objects.all() 
           #print avbooks
           return render_to_response('lib.html',{'avbooks':avbooks, 'user':user})
        else:
           return redirect("/")
     except KeyError:
        #print "except"
        return redirect("/")

@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
def issBooks(request):
     try:
        user = request.session["user"]
        if user:
           #print "user is", user
           issbooks = IssuedBook.objects.all() 
           #print issbooks
           return render_to_response('issbooks.html', {'issbooks': issbooks, 'user':user})
        else:
           return redirect("/")
     except KeyError:
        return redirect("/")


@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
def studentRecord(request):
     try:
        user = request.session["user"]
        if user:
          updateFine = StudentInfo.objects.all()
          for fi in updateFine:
             fine_charged = calculate_fine(fi.university_roll_no)
             fi.update(fine=fine_charged)
             #fi.fine = fine_charged
             #fi.save(force_update=True)
          return render_to_response('stRecord.html', {'addStudent':updateFine, 'user':user})
        else:
           return redirect("/")
     except KeyError:
        return redirect("/")


@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
def teacherRecord(request):
     try:
        user = request.session["user"]
        if user:
          updateFine = TeacherInfo.objects.all()
          for fi in updateFine:
             fine_charged = calculate_fine(fi.eid)
             fi.update(fine=fine_charged)
             #fi.fine = fine_charged
             #fi.save(force_update=True)
          return render_to_response('trecord.html', {'tInfo':updateFine, 'user':user})
        else:
           return redirect("/")
     except KeyError:
        return redirect("/")


def addBooks(request):
     try:
        #print "In add books",request.POST
        status = {}
        if request.method == 'POST':
          bookname = request.POST.get('book_name')
          authName = request.POST.get('authname')
          dpt = request.POST.get('dpt')
          #print "data in server", bookname, authName, dpt
          addBook = AvailableBook()
          addBook.book_name = bookname
          addBook.Author_name = authName
          addBook.Department = dpt 
          addBook.save()
          status['success'] = 0
        #print "sending response"
        return HttpResponse(json.dumps(status))
     except KeyError:
        pass

def check_student_record(roll_no):
    find_stu = StudentInfo.objects.filter(university_roll_no=roll_no)
    if not find_stu:
       print "student not present in records, first add student"
       return 1
    else:
       print "issue ok"
       return 0

def check_teacher_record(roll_no):
    find_teacher = TeacherInfo.objects.filter(eid=roll_no)
    if not find_teacher:
       print "Teacher is not present in records, first add Teacher"
       return 1
    else:
       print "issue ok"
       return 0
      
def check_book_availability(bookname):
     find_book = AvailableBook.objects.filter(book_name=bookname) 
     if not find_book:
        print "Book is not available"
        return 1
     else:
        check_avail = IssuedBook.objects.filter(book_name=bookname)
        if not check_avail:
           print "issue book"
           return 0
        else:
           print "Book is issued to someone else"
           return 1

def update_book_submission_count(uid):
    updateBookCount = StudentInfo.objects.filter(university_roll_no=uid)   
    if not updateBookCount:
       updateBookCount = TeacherInfo.objects.filter(eid=uid)
                                                                             
    for i in updateBookCount:
        print i.no_of_books_issued 
        if i.no_of_books_issued == 2:
            i.no_of_books_issued -= 1
            i.save()
        elif i.no_of_books_issued == 1:
            i.no_of_books_issued -= 1
            i.save()


def update_book_submission(request):
    try:
       status = {}
       print "request is", request.POST
       if request.method == 'POST':
          bookname = request.POST.get('book_name')
          uid = request.POST.get('uid')
          print "bookname", bookname, uid
          update_submission = IssuedBook.objects.filter(book_name=bookname) 
          print "update submission", update_submission
          if update_submission:
             update_book_submission_count(uid)
             update_submission.delete()
             status['success'] = 0
             return HttpResponse(json.dumps(status))
    except KeyError:
       return redirect("/issued_books")

def issuedBooks(request):
     try:
        #print "In issue books", request.POST
        status = {}
        if request.method == 'POST':
          bookname = request.POST.get('book_name')
          stname = request.POST.get('stname')
          roll_no = request.POST.get('roll_no')
          fromd = request.POST.get('from')
          to = request.POST.get('to')
          fromd = datetime.datetime.strptime(fromd, "%d/%m/%Y").date()
          to = datetime.datetime.strptime(to, "%d/%m/%Y").date()
          issbook = IssuedBook() 
          issbook.book_name = bookname
          issbook.assignedTo = stname
          issbook.roll_no = roll_no
          issbook.lendPeriod_from = fromd
          issbook.lendPeriod_to = to
          bstatus = check_book_availability(bookname)
          if bstatus == 1:
             print "book not available"
             status['success'] = 1
          elif bstatus == 0:
             stStatus = check_student_record(roll_no)
             if stStatus == 0: 
                st = update_issue_book_count(roll_no)
                if st == 0:
                   issbook.save()
                   status['success'] = 0
                if st == 1:
                   status['success'] = 1

             elif stStatus == 1:
                print "student not present in records"
                tStatus = check_teacher_record(roll_no)
                if tStatus == 0:
                   st = update_issue_book_count(roll_no)
                   if st == 0:
                      issbook.save()
                      status['success'] = 0
                   if st == 1:
                      status['success'] = 1
                elif tStatus == 1:
                   print "Teacher is not present in records"
                   status['success'] = 1

        return HttpResponse(json.dumps(status))
     except KeyError:
        pass

def update_issue_book_count(roll_no):
    updateBookCount = StudentInfo.objects.filter(university_roll_no=roll_no)
    if not updateBookCount:
       updateBookCount = TeacherInfo.objects.filter(eid=roll_no)

    for i in updateBookCount:
        print i.no_of_books_issued 
        if i.no_of_books_issued == 2:
            print "books can not be issued"
            return 1
        elif i.no_of_books_issued < 2 and i.no_of_books_issued >= 0:
            print "books can be issued"
            i.no_of_books_issued += 1
            i.save()
            return 0

def calculate_fine(uni_roll):
     issuedBooks = IssuedBook.objects.filter(roll_no=uni_roll)
     fromd = date.today()
     for i in issuedBooks:
         fromd = i.lendPeriod_from
     fine = date.today() - fromd
     #print "fine", fine.__str__()
     import re
     diff =  re.match('\d+', fine.__str__())
     diff = int(diff.group()) - 7
     if diff > 0:
        fine_charged = diff * 10;
     else:
        fine_charged = 0;
     #print "fine charged in cal fine", fine_charged
     return fine_charged

def addStudent(request):
     try:
        #print "In add Student ", request.POST
        status = {}
        if request.method == 'POST':
          stuname = request.POST.get('stName')
          uno = request.POST.get('uno')
          dpt = request.POST.get('dpt')
          #issbooks = request.POST.get('issbooks')
          #print "info is", stuname, uno, dpt
          addStu = StudentInfo.objects.filter(university_roll_no=uno) 
          if not addStu:
             addStudent = StudentInfo() 
             addStudent.student_name = stuname
             addStudent.university_roll_no = uno
             addStudent.student_department = dpt
             addStudent.no_of_books_issued = 0 
             fine_charged = calculate_fine(uno)
             print "fine charged", fine_charged
             addStudent.fine = fine_charged 
             addStudent.save()
             status['success'] = 0
          else:
             st = update_issue_book_count(uno)
             if st == 0:
                 addStudent.save()
                 status['success'] = 0
             if st == 1:
                 status['success'] = 1
        print "sending response",json.dumps(status)
        return HttpResponse(json.dumps(status))
     except KeyError:
        pass

def updateBook(request):
     try:
        print "In update Student ", request.POST
        return HttpResponse(json.dumps({'status':1}))
     except KeyError:
        pass

def addTeacher(request):
     try:
        #print "In add Student ", request.POST
        status = {}
        if request.method == 'POST':
          tname = request.POST.get('tName')
          eid = request.POST.get('eid')
          tdpt = request.POST.get('tdpt')
          #issbooks = request.POST.get('issbooks')
          print "info is", tname, eid, tdpt
          addteach = TeacherInfo.objects.filter(eid=eid) 
          if not addteach:
             addt = TeacherInfo() 
             addt.t_name = tname
             addt.eid = eid
             addt.teacher_department = tdpt
             addt.no_of_books_issued = 0 
             fine_charged = calculate_fine(eid)
             print "fine charged", fine_charged
             addt.fine = fine_charged 
             addt.save()
             status['success'] = 0
          else:
             st = update_issue_book_count(uno)
             if st == 0:
                 addt.save()
                 status['success'] = 0
             if st == 1:
                 status['success'] = 1
        print "sending response",json.dumps(status)
        return HttpResponse(json.dumps(status))
     except KeyError:
        pass



@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
def login(request):
     try:
        username = request.GET.get('username')
        paswd = request.GET.get('pwd')
        if username and paswd:
           login_res = AdminInfo.objects.filter(username=username).filter(password=paswd)
           if login_res:
               request.session['user'] = username
               return redirect("/available_books")
           else:
               messages.error(request, 'Invalid Username Password')
               return redirect("home")
        else:
            messages.error(request, 'Invalid Username Password.')
            return redirect("home")

     except KeyError:
        pass

@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
def logout(request):
    try:
    	if request.session["user"] :
            del request.session['user']
            return redirect('/') 
    except KeyError:
        pass
        return redirect('/')

