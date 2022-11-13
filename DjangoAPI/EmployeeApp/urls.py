from django.urls import include, re_path
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^department/$',views.departmentApi),
    re_path(r'^department/([0-9]+)$',views.departmentApi),
] 