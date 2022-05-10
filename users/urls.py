from django.conf.urls import url
from . import views
# Create your views here.
urlpatterns = [
    # url (路径正则, 视图函数名字)
    url(r'^index/$', views.index),
    url(r'^say/$', views.say),
    url(r'^sayhello/$', views.sayhello),
]
