from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic.list import ListView

from article_module.models import Article


# class ArticlesView(View):
#     def get(self, request):
#         articles = Article.objects.filter(is_active=True)
#         context = {
#             'articles': articles
#         }
#         return render(request, 'article_module/articles_page.html', context)


class ArticlesListView(ListView):
    model = Article
    paginate_by = 5
    template_name = 'article_module/articles_page.html'
