from django.views.generic import ListView
from .models import Article


# Create your views here.
class ArticleListView(ListView):
    queryset = Article.objects.filter(status=True)
    template_name = "blog/article_list.html"
