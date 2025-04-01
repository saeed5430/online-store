from django import forms
from .models import contactus

class ContactUsForm(forms.Form):
    full_name  = forms.CharField(label='نام و نام خانوادگی',max_length=50,
        error_messages={
            'required':'لطفا نام و نام خانوادگی را وارد کنید',
            'max_lenght':'نام و نام خانوادگی نمی تواند بیشتر از 50 کاراکتر باشد'
        },
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder':'نام و نام خانوادگی'
        })
    )
    email = forms.EmailField(label='ایمیل',widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'ایمیل'
    }))
    subject = forms.CharField(label='عنوان',widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder':'موضوع'
    }))
    text = forms.CharField(label='متن پیام',widget=forms.Textarea(attrs={
        'class': "form-control",
        'placeholder':'متن پیام',
        'rows':'5',
        'id':'message'
    }))

class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = contactus
        fields = ['full_name','email','title','message']
        widgets = {
            'full_name':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'نام و نام خانوادگی'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'متن خود را وارد کنید',
                'rows':5,
                'id':'message'
            })
        }
        labels = {
            'full_name':'نام و نام خانوادگی شما',
            'email':'ایمیل شما'
        }
        error_messages = {
            'full_name':{
                'required':'نام و نام خانوادگی شما خالی می باشد.'
            }
        }

class ProfileForm(forms.Form):
    user_image = forms.ImageField()
