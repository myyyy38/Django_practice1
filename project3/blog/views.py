from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class IndexView(generic.ListView):
    #モデル名_list.htmlに勝手に渡される
    model = Post

    #get_querysetにオーバーライドして修正
    def get_queryset(self):
        #日付で降順ソート
        return Post.objects.order_by('-created_at')