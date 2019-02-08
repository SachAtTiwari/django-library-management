from django.conf.urls import include, url
from django.contrib import admin
from libm.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'dlib.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name="home"),
    url(r'^$', home, name="home"),
    url(r'^available_books', avbooks, name="avBooks"),
    url(r'^addBooks', addBooks, name="addbooks"),
    url(r'^update', updateBook, name="addbooks"),

    url(r'^issued_books', issBooks, name="isbooks"),
    url(r'^issbooks', issuedBooks, name="issubooks"),
    url(r'^updateSubmission', update_book_submission, name="submitbooks"),

    url(r'^student_record', studentRecord, name="studentRecord"),
    url(r'^addStudent', addStudent, name="addStudent"),

    url(r'^teacher_record', teacherRecord, name="tRecord"),
    url(r'^addTeacher', addTeacher, name="addT"),

    url(r'^login', login, name="login"),
    url(r'^logout', logout, name="logout"),

    url(r'^stLogin', stLogin, name="stlogin"),
    url(r'^stSignUp', stSignUp, name="stlogout"),

    url(r'^signup', signup, name="stsignup"),
    url(r'^stlogin', studentLogin, name="studentLogin"),
    url(r'^stInfo', stInfo, name="stinfo"),

    url(r'^tsignup', tsignup, name="tsignup"),
    url(r'^tlogin', tLogin, name="tLogin"),

    url(r'^Tsignup', Tsignup, name="Tsignup"),
    url(r'^Tlogin', TLogin, name="TLogin"),
    url(r'^tInfo', TInfo, name="Tinfo"),
]
