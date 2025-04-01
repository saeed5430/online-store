from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index_page'),
    path('about-us', views.AboutUs.as_view(), name='about_us'),
]