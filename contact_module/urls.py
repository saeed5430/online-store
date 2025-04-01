from django.urls import path
from .views import ContactUsView,CreateProfileView,ProfileView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',ContactUsView.as_view(),name='contact_us_page'),
    path('create-profile/',CreateProfileView.as_view(),name = 'creat_profile_page'),
    path('profiles/', ProfileView.as_view(), name='profiles_page')
]