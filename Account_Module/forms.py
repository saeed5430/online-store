import validators
from django import forms
from django.core.exceptions import ValidationError
from django.core import validators


class RegistrationForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.EmailValidator,
            validators.MaxLengthValidator(100)
        ]
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if ((password and confirm_password)
                and password != confirm_password):
            raise ValidationError('رمز عبور با تکرار رمز عبور مغایرت دارد!')

        return confirm_password

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.EmailValidator,
            validators.MaxLengthValidator(100)
        ]
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.EmailValidator,
            validators.MaxLengthValidator(100)
        ]
    )
class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
