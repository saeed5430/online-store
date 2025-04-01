from django.urls import path
from . import views
urlpatterns = [
    path('register',views.RegisterView.as_view(),name='register_page'),
    path('login',views.LoginView.as_view(),name='login_page'),
    path('logout',views.LogoutView.as_view(),name='logout_page'),
    path('forget-password',views.ForgetPassword.as_view(),name='forget_password_form'),
    path('reset-password/<active_code>',views.ResetPassword.as_view(),name='reset_password_form'),
    path('activate-account/<str:email_active_code>',views.ActiveAccountView.as_view(),name='activate_account')
]