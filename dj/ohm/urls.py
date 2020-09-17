from django.conf.urls import url
from ohm import views

urlpatterns = [
    url('^$', views.ohm, name='ohm'),
]
