from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from .models import Product
from django.views.generic import ListView,DetailView
from django.shortcuts import get_object_or_404
from django.db.models import Avg
from django.http import Http404
# Create your views here.


class ProductListView(ListView):
    template_name = 'eshop_project/Product_list.html'
    model = Product
    context_object_name = 'product'
    ordering = ['price']
    paginate_by = 6
    def get_queryset(self):
        base = super(ProductListView,self).get_queryset()
        result_base = base.filter(is_active=True)
        return result_base

class ProductDetailView(DetailView):
    template_name = 'eshop_project/Product_detail.html'
    model = Product
    context_object_name = 'product'


from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.http import HttpResponseBadRequest
from .models import Product  # مطمئن شو که مدل Product را ایمپورت کرده‌ای

# class AddProductFavorite(View):
#     def post(self, request):
#         product_id = request.POST.get("Product_id")  # مقدار را دریافت کن
#         if not product_id:
#             return HttpResponseBadRequest("Product ID is required")  # بررسی مقدار
#
#         product = get_object_or_404(Product, pk=product_id)  # دریافت محصول یا 404
#         request.session['product_favorite'] = product_id  # ذخیره در سشن
#
#         return redirect(product.get_absolute_url())  # هدایت به صفحه محصول



# def Product_list(request):
#     Products = Product.objects.all().order_by('-price')[:5]
#     return render(request,'eshop_project/Product_list.html',context={
#         'Products':Products ,
#     })

# def Product_detail(request,slug):
#     Product_i = get_object_or_404(Product, slug=slug)
#     return render(request,'eshop_project/Product_detail.html',context={
#         'Product':Product_i
#     })