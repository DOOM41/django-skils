from django.shortcuts import render
from django.http import HttpResponse
from core.models import Article, Comment, OtherImage

# Create your views here.


def article(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, "core/articles.html", context)


def article_view(request, id):
    context = {
        'article': Article.objects.get(id=id),
        'images': OtherImage.objects.filter(article=id),
        'comments': Comment.objects.filter(article=id)
    }
    return render(request, "core/article_view.html", context)
