from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'dlib.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'libm.views.home', name="home"),
    url(r'^$', 'libm.views.home', name="home"),
    url(r'^available_books', 'libm.views.avbooks', name="avBooks"),
    url(r'^addBooks', 'libm.views.addBooks', name="addbooks"),
    url(r'^update', 'libm.views.updateBook', name="addbooks"),

    url(r'^issued_books', 'libm.views.issBooks', name="isbooks"),
    url(r'^issbooks', 'libm.views.issuedBooks', name="issubooks"),
    url(r'^updateSubmission', 'libm.views.update_book_submission', name="submitbooks"),

    url(r'^student_record', 'libm.views.studentRecord', name="studentRecord"),
    url(r'^addStudent', 'libm.views.addStudent', name="addStudent"),

    url(r'^teacher_record', 'libm.views.teacherRecord', name="tRecord"),
    url(r'^addTeacher', 'libm.views.addTeacher', name="addT"),

    url(r'^login', 'libm.views.login', name="login"),
    url(r'^logout', 'libm.views.logout', name="logout"),

    url(r'^stLogin', 'libm.views.stLogin', name="stlogin"),
    url(r'^stSignUp', 'libm.views.stSignUp', name="stlogout"),

    url(r'^signup', 'libm.views.signup', name="stsignup"),
    url(r'^stlogin', 'libm.views.studentLogin', name="studentLogin"),
    url(r'^stInfo', 'libm.views.stInfo', name="stinfo"),

    url(r'^tsignup', 'libm.views.tsignup', name="tsignup"),
    url(r'^tlogin', 'libm.views.tLogin', name="tLogin"),

    url(r'^Tsignup', 'libm.views.Tsignup', name="Tsignup"),
    url(r'^Tlogin', 'libm.views.TLogin', name="TLogin"),
    url(r'^tInfo', 'libm.views.TInfo', name="Tinfo"),
]
