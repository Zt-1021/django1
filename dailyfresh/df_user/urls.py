from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^register_handle/$', views.register_handle, name='register_handle'),
    url(r'^register_exist/$', views.register_exist, name='register_exist'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_handle/$', views.login_handle, name='login_handle'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^info/$', views.info, name='info'),
    url(r'^order/$', views.order, name='order'),
    url(r'^site/$', views.site, name='site'),

]