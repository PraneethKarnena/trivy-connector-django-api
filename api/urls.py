from django.urls import path

from api import views


urlpatterns = [
    path('scan/', views.ScanView.as_view(), name='scan'),
    path('result/<uuid:pk>/', views.ScanResultView.as_view(), name='result'),
]