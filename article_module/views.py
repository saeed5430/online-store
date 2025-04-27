from jalali_date import datetime2jalali
from django.views.generic import ListView, DetailView

from django.shortcuts import render
from django.views import View

from article_module.models import Article, ArticleCategory, ArticleComments
from django.db.models import Q


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
        if self.request.user.is_authenticated:
                context['date'] = datetime2jalali(self.request.user.date_joined)
        else:
                context['date'] = None

        return context
    def get_queryset(self):
        query = super(ArticleListView, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name:
            query = query.filter(selected_category__url_title__iexact=category_name)
        return query

class ArticleDetailView(DetailView):
    model=Article
    template_name = 'article_module/article_detail.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        current_page = self.object
        previous_page = Article.objects.filter(Q(is_active=True)&Q(id__lt=current_page.id)).order_by('-id').first()
        next_page = Article.objects.filter(Q(is_active=True)&Q(id__gt=current_page.id)).order_by('id').first()
        last_id = Article.objects.filter(is_active=True).order_by('-id').values_list('id', flat=True).first()
        first_id = Article.objects.filter(is_active=True).order_by('id').values_list('id', flat=True).first()

        comments = ArticleComments.objects.filter(article_id=current_page.id,parent=None).prefetch_related('articlecomments_set')

        context['comments'] = comments
        context['previous_page'] = previous_page
        context['next_page'] = next_page
        context['last_id'] = last_id
        context['first_id'] = first_id
        return context


    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query

def article_categories_component(request):
    main_categories=ArticleCategory.objects.filter(is_active=True)
    return render(request,"article_module/components/article_categories_component.html",context={"main_categories":main_categories})

