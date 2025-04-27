from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profiles',max_length=40,verbose_name="تصویر کاربر",null=True,blank=True)
    email_active_code = models.CharField(max_length=100,verbose_name='کد فعال سازی ایمیل')
    about= models.TextField(max_length=1000,verbose_name="متن درباره کاربر",null=True,blank=True)

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def str(self):
        if self.first_name and self.last_name is not None:
            return self.get_full_name()
        return self.email