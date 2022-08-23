from django.shortcuts import render
from .models import Article

# Create your views here.
def blog_list(request):
    return render(request, 'blog.html')

def blog_detail(request, id_data):
    article = Article.objects.get(id=id_data)
    return render(request, 'article.html', context={
        'article': article
    })