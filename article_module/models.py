from jalali_date import date2jalali
from django.db import models
from django.utils import timezone

from Account_Module.models import User


# Create your models here.
class ArticleCategory(models.Model):
    parent = models.ForeignKey('self',null=True,blank=True, on_delete=models.CASCADE)
    title=models.CharField(max_length=200,verbose_name='عنوان دسته بندی')
    url_title=models.CharField(max_length=200,unique=True,verbose_name='عنوان در url')
    is_active=models.BooleanField(default=True,verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی های مقاله'
class Article(models.Model):
    title=models.CharField(max_length=300,verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=400,db_index=True,allow_unicode=True,verbose_name='عنوان در url')
    image = models.ImageField(upload_to='images/articles',verbose_name='تصویر مقاله')
    short_description = models.TextField(verbose_name='توضیحاتت کوتاه')
    text = models.TextField(verbose_name='متن مقاله')
    is_active=models.BooleanField(default=True,verbose_name='فعال/غیرفعال')
    selected_category=models.ManyToManyField(ArticleCategory,verbose_name='دسته بندی ها')
    author = models.ForeignKey(User,on_delete = models.CASCADE,verbose_name='نویسنده',null=True,editable=False)
    create_date = models.DateTimeField(auto_now_add=True,editable=False,null=True,verbose_name='تاریخ ثبت')


    def __str__(self):
        return self.title

    def get_jalali_create_date(self):
        return date2jalali(self.create_date)

    def get_jalali_create_time(self):
        return self.create_date.strftime('%H:%M')
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'
