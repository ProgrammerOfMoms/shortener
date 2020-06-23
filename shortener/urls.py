from django.contrib import admin
from django.urls import path, re_path

from .views import UrlList, UrlShort, UrlView

urlpatterns = [
    path('', UrlList.as_view()),
    path('create/', UrlShort.as_view()),
    re_path(r'^(?P<hash>.+)$', UrlView.as_view())
]
