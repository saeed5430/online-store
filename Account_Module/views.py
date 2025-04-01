from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect,reverse
from django.contrib.auth import get_user_model,login,logout
from django .views import View
from .models import User
from django.utils.crypto import get_random_string
from Account_Module.forms import RegistrationForm, LoginForm, ForgotPasswordForm, ResetPasswordForm
from django.http import Http404,HttpRequest
from utils.email_service import send_custom_email


class RegisterView(View):
    def get(self,request):
        register_form = RegistrationForm()
        context = {
            'register_form':register_form
        }
        return render(request,'account_module/register.html',context)

    def post(self,request):
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email','این ایمیل قبلا ثبت نام شده است')
            else:
                new_user = User(email=user_email,email_active_code= get_random_string(72),is_active=False,username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                send_custom_email(subject='فعالسازی حساب کاربری',from_email='hesam54300@gmail.com',to=[new_user.email],html_page='emails/activate_account.html',
                email_active_code=new_user.email_active_code)
                return redirect('login_page')
        context = {
            'register_form':register_form
        }
        return render(request,'account_module/register.html',context)
class LoginView(View):
    def get(self,request):
        login_form = LoginForm()
        context = {
            'login_form':login_form
        }
        return render(request,'account_module/login.html',context)

    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email','نام کاربری یا رمز عبور نادرست است')
                else:
                    check_password = user.check_password(user_password)
                    if check_password:
                        login(request, user)
                        return redirect(reverse('index_page'))
                    else:
                        login_form.add_error('email','نام کاربری یا رمز عبور نادرست است')
                        #todo:show a error message
            else:
                login_form.add_error('email','کاربری با چنین ایمیلی وجود ندارد')

        context={
            'login_form':login_form
        }
        return render(request,'account_module/login.html',context)
class ActiveAccountView(View):
    def get(self,request,email_active_code):
        user:User = User.objects.filter(email_active_code__exact= email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                # todo:show success message to user
            else:
                pass
                # todo:show your account was activated message to user
            return redirect(reverse('login_page'))
        raise Http404()


        # user:User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        # if user is not None:
        #     if not user.is_active:
        #         user.is_active = True
        #         user.email_active_code = get_random_string(72)
        #         user.save()
        #         # todo:show success message to user
        #     else:
        #         #todo:show your account was activated message to user
        #         pass
        #     return redirect('login_page')
        # raise Http404
class ForgetPassword(View):
     def get(self,request:HttpRequest):
         context = {
            'forget_password_form':ForgotPasswordForm
         }
         return render(request,'Account_Module/forgot_password.html',context)
     def post(self,request:HttpRequest):
         forget_password_form = ForgotPasswordForm(request.POST)
         if forget_password_form.is_valid():
             user_email = forget_password_form.cleaned_data.get('email')
             user: User = User.objects.filter(email__iexact=user_email).first()
             if user is not None:
                 send_custom_email(subject='تغییر رمز عبور', from_email='hesam54300@gmail.com',
                                   to=[user.email], html_page='emails/forgot_password.html',
                                    email_active_code=user.email_active_code)
                 return redirect(reverse('index_page'))

             #todo: sent a email message for change password
         context = {
            'forget_password_form':forget_password_form
         }
         return render(request,'Account_Module/forgot_password.html',context)
class ResetPassword(View):
    def get(self, request: HttpRequest,active_code):
        reset_password_form = ResetPasswordForm()
        user:User = User.objects.filter(email_active_code__exact=active_code).first()
        if user is not None:
            pass
        context={
            'reset_password_form':reset_password_form,
            'user':user
        }
        return render(request, 'Account_Module/reset_password.html', context)
    def post(self,request:HttpRequest,active_code):
        reset_password_form = ResetPasswordForm(request.POST)
        if reset_password_form.is_valid():
            password = reset_password_form.cleaned_data.get('password')
            confirm_password = reset_password_form.cleaned_data.get('confirm_password')
            if password == confirm_password:
             user:User = User.objects.filter(email_active_code__exact=active_code).first()
             if user is not None:
                 user.is_active = True
                 user.set_password(password)
                 user.email_active_code=get_random_string(72)
                 user.save()
                 return redirect(reverse('login_page'))
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect(reverse('login_page'))


