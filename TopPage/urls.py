from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='TopPage_Index'),
]
