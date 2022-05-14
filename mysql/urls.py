from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns =[
    url(r'^books/$', views.BookListAPIView.as_view()),
    url(r'^books/(?P<pk>\d+)$', views.BookDetailAPIView.as_view()),
]


# router = DefaultRouter()
# router.register(r'books', views.BookInfoView, basename='books')
# urlpatterns += router.urls
