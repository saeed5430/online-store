from django.urls import path
from . import views

urlpatterns = [
    path('',views.ArticleListView.as_view(),name='articles_list'),
    path('<str:category>',views.ArticleListView.as_view(),name='articles_list_component')
]