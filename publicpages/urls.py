from django.urls import path

from publicpages import views


urlpatterns = [
    path('', views.home_view, name='home'),
]