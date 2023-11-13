from c_app import views
from django.urls import path

urlpatterns=[
    path('', views.home, name='home'),
    path('compress/', views.compress_file, name='compress_file'),
]