from django.conf.urls import url
from posts import views

urlpatterns = [
    url(r'^home/$', views.post_home, name="home"),
    url(r'^list/$', views.post_list, name="list"),
    url(r'^detail/(?P<post_id>\d+)/$', views.post_detail, name="detail"),

  
]