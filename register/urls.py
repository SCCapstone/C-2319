from . import views
from .views import view_profile , edit_profile
from django.urls import path, re_path
from django.conf.urls import url


urlpatterns = [
    # url(r'^$', views.home),
    url(r'^profile/$', views.view_profile, name="view_profile"),
    url(r'^profile/edit/$' , views.edit_profile, name = 'edit_profile'),
]
