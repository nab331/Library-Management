from django.conf.urls import url,include
from . import views

app_name = 'dash'

urlpatterns = [
    url(r'^admin_dash/$', views.admin_dash, name="admin_dash"),
    url(r'^student_dash/$',views.student_dash,name="student_dash"),
    url(r'^staff_dash/$', views.staff_dash, name="staff_dash"),
    url(r'^student_dash/books/$', views.book_list, name="Books"),
    url(r'^student_dash/users/$', views.users_list, name="Users"),
]
''