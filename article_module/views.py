from jalali_date import datetime2jalali
from django.views.generic import ListView

from django.shortcuts import render
from django.views import View

from article_module.models import Article, ArticleCategory


class ArticleView(View):
    def get(self, request):
        articles = Article.objects.filter(is_active=True)
        context = {'articles': articles }
        return render(request,'article_module/article_page.html',context)

class ArticleListView(ListView):
    model=Article
    paginate_by = 1
    template_name = 'article_module/article_page.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ArticleListView,self).get_context_data(*args,**kwargs)
        context['date'] = datetime2jalali(self.request.user.date_joined)
        return context

    def get_queryset(self):
        query = super(ArticleListView, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name:
            query = query.filter(selected_category__url_title__iexact=category_name)
        return query


def article_categories_component(request):
    main_categories=ArticleCategory.objects.filter(is_active=True)
    return render(request,"article_module/components/article_categories_component.html",context={"main_categories":main_categories})
