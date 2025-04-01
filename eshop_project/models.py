from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class productcategory(models.Model):
    title = models.CharField(max_length=300 ,db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=300,verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')
    def __str__(self):
        return f'{self.title}-{self.url_title}'
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural='دسته بندی ها'


class productBrand(models.Model):
    title = models.CharField(max_length=300,db_index=True,verbose_name= 'نام برند')
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')
    class Meta:
        verbose_name = 'برند'
        verbose_name_plural='برندها'
    def __str__(self):
        return f'{self.title}'
class Product(models.Model):
    title = models.CharField(max_length=300,verbose_name='عنوان محصول')
    category = models.ManyToManyField(productcategory, related_name='product_categories',verbose_name='دسته بندی ها')
    brand = models.ForeignKey(productBrand, on_delete=models.CASCADE,verbose_name='برند',null=True, blank=True)
    price = models.IntegerField(verbose_name='قیمت')
    short_description = models.CharField(max_length= 300,db_index=True,verbose_name='توضیحات کوتاه')
    description = models.TextField(db_index=True,verbose_name='توضیحات اصلی')
    is_active = models.BooleanField(default=False,verbose_name='فعال/غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده/نشده')
    slug = models.SlugField(default="",null=True,blank = True,max_length=200,unique=True,verbose_name='عنوان در url')
    image = models.ImageField(upload_to='images/products',null = True,verbose_name="تصویر محصول",blank=True)

    def get_absolute_url(self):
        return reverse('product_detail',args=[self.slug])
    def save(self, *args, **kwargs):
        #self.slug = slugify(self.title)#samsung galaxy s20 ==> samsung-galaxy-s20
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.price}"
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural='محصولات'
class productTag(models.Model):
    caption = models.CharField(max_length=300,db_index=True,verbose_name='عنوان')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_tags')
    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural='تگ های محصولات'
    def __str__(self):
        return self.caption
