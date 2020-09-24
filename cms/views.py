from django.shortcuts import render
from django.http import HttpResponse

from cms.models import Comic

# Create your views here.
def comic_list(request):
    """書籍の一覧"""
    comics = Comic.objects.all()
    return render(request,
                  'cms/comic_list.html',     # 使用するテンプレート
                  {'comics': comics})
