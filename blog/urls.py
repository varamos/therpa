from django.conf.urls import url
from . import views
from blog.views import *



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/', views.home, name='home'),
    url(r'^main_table/$', views.post_list, name='post_list'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^pie_chart/', views.pie_chart, name='pie_chart'),
    url(r'^random2/', views.random2, name='random2'),
    url(r'^treemaps/', views.treemaps, name='treemaps'),
    url(r'^treemaps_m/', views.treemaps_m, name='treemaps_m'),
    url(r'^real_main/', views.real_main, name='real_main'),
    url(r'^downloads/', views.downloads, name='downloads'),
    url(r'^about/', views.about, name='about'),
    url(r'^write/', write, name='write'),
    url(r'^list/', list, name='list'),
    url(r'^view/(?P<num>[0-9]+)/$', view),
    url(r'^main_10/', main_10_small_molecules, name='list'),


]
