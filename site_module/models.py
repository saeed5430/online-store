from django.db import models

class SiteSettings(models.Model):
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی',default=True)
    site_name = models.CharField(max_length=200,verbose_name= 'نام سایت',)
    address = models.CharField(max_length=200,verbose_name= 'آدرس سایت')
    phone = models.CharField(max_length=200,null=True,verbose_name= 'تلفن سایت')
    fax = models.CharField(max_length=200,null=True,verbose_name= 'فکس سایت')
    email = models.CharField(max_length=200,null=True,verbose_name= 'ایمیل سایت')
    copy_right = models.TextField(verbose_name= 'متن کپی رایت سایت')
    site_logo = models.ImageField(upload_to='images/site-setting',verbose_name= 'لوگو سایت')
    site_url = models.CharField(max_length=200,verbose_name= 'دامنه سایت')
    about_us = models.TextField(verbose_name= 'درباره سایت')
    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'
    def __str__(self):
        return self.site_name
class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200,verbose_name= 'عنوان')

    class Meta:
        verbose_name = 'دسته بندی لینک های فوتر'
        verbose_name_plural = 'دسته بندی های لینک های فوتر'

    def __str__(self):
        return self.title

class FooterLink(models.Model):
    title = models.CharField(max_length=200,verbose_name= 'عنوان')
    url = models.URLField(max_length=500,verbose_name= 'لینک')
    footerlink = models.ForeignKey(to=FooterLinkBox,verbose_name= 'دسته بندی',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
        return self.title
class Slider(models.Model):
    title = models.CharField(max_length=200,verbose_name= 'عنوان')
    url = models.URLField(max_length=500,verbose_name= 'لینک')
    url_title = models.CharField(max_length=200,verbose_name= 'عنوان لینک')
    description = models.TextField(verbose_name= 'توضیحات')
    image = models.ImageField(upload_to='',verbose_name='تصویر اسلاید')
    is_active = models.BooleanField(default=True,verbose_name= 'فعال/غیرفعال')

    class Meta:
        verbose_name = 'اسلاید'
        verbose_name_plural = 'اسلایدها'

    def __str__(self):
        return self.title