from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns =[
    # url(r'^books/$', views.BookListView.as_view()),
    # url(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view()),
]


router = DefaultRouter()
router.register(r'books', views.BookInfoView)
urlpatterns += router.urls
