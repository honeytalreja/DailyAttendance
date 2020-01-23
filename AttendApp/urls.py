from django.conf.urls import url, include
from . import views

# Url defined here, can access the page related to the url by adding the path
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login$', views.user_login, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^attendance$', views.mark_attendance, name='mark_attendance'),
    url(r'^data$', views.admin_data, name='admin_data'),
]
