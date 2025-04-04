"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from myapp import views, ca, abc
from myapp import calculate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('message/', views.message),
    # path('message2/', views.message2),
    # path('greet/<name>', views.greet),
    # # path('add/<int:n1>/<int:n2>', views.add),
    # path('add/<n1>/<n2>', views.add),
    # path('add1/', views.add1),
    # path('calculate/', calculate.calculator),
    # re_path(r'^user/(?P<username>[a-z]+)/$', views.user),
    # re_path(r'^user1/(?P<username>[A-Z]+)/$', views.user1),
    # re_path(r'^user2/(?P<username>[a-zA-Z\s@_-]+)/$', views.user2),
    # re_path(r'^user3/(?P<username>[0-9]+)/$', views.user3),
    # re_path(r'^user4/(?P<username>[a-zA-z0-9]+)/$', views.user4),
    # re_path(r'^user5/(?P<username>[\w -]+)/$', views.user5),
    # re_path(r'^user6/(?P<username>[\d]{1,4}+)/$', views.user6),
    # re_path(r'^user7/(?P<month>\d{2}+)/(?P<year>\d{4}+)/$', views.user7),
    # re_path(r'^user8/(?P<username>\d+|[a-zA-Z]+)/$', views.user8),
    # re_path(r'^student/(?P<studentId>[0-9]+)/(?P<studentName>[a-zA-Z\s]*)/?$', views.student),
    # re_path(r'^employee/(?P<empname>[a-zA-Z]+)(?:/(?P<empsalary>[0-9]*))/?$', views.employee),
    # re_path(r'^blog(?:/(?P<post_slug>[\w-]+))*/$', views.blog_details),
    # path('check/', views.check),
    # re_path(r'^food_details/(?P<foodname>[a-zA-Z]*)/?(?P<foodprice>[0-9]*)/$', views.food_details),
    # path('test/', views.test),
    # path('test1/', views.test1),
    # path('yummy_list/', views.yummy_list),
    # path('yummy_list/<str:single_yummy_item>/', views.yummy_details, name="abhishek"),
    # path('testcss/', views.test_css),
    # path('tastyfood/', views.tasty_list),
    # path('htmlform/', views.form),
    # path('htmlformtask/', views.taskForm),
    # path("form1/", views.form1),
    # path('success/', views.success, name="success"),
    # path('htmltemplateform/', views.htmlform),
    # path('formvalidate/', views.validate),
    # path('ca/', ca.items_list),
    # path('cadetails/<str:persondetail>/', ca.item_details, name="profile"),
    # path('abc/', abc.details, name="query"),
    # path('routes/', views.routes_details),
    # path('home/', views.home, name="home"),
    # path('about/', views.about, name="about"),
    # path('contact/', views.contact, name="contact"),
    # path('singup/', views.usersingup)
    # path('signup/', views.Signup, name = 'signupform'),
    # path('delete/<int:id>', views.delete_user, name = 'delete_user'),
    # path('edit/<int:id>', views.edit_user, name = 'edit_user'),
    # path('blogpost/', views.blogpostform, name = "blogpostform"),
    # path('fetchblogposts/', views.fetchblogposts, name="fetchblogposts")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler404 = "myproject.views.handler404"
