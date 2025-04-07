from jalali_date import datetime2jalali
from django.views.generic import ListView

from django.shortcuts import render
from django.views import View

from article_module.models import Article


class ArticleView(View):
    def get(self, request):
        articles = Article.objects.filter(is_active=True)
        context = {'articles': articles }
        return render(request,'article_module/article_page.html',context)

class ArticleListView(ListView):
    model=Article
    paginate_by = 5
    template_name = 'article_module/article_page.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ArticleListView,self).get_context_data(*args,**kwargs)
        context['date'] = datetime2jalali(self.request.user.date_joined)
        return context