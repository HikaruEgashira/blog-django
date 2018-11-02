# templateのhtmlを利用して見た目をつくるファイル
from django.shortcuts import render, get_object_or_404 # オブジェクトの取得 http://djangoproject.jp/doc/ja/1.0/topics/http/shortcuts.html#get-list-or-404
from django.views.generic import TemplateView
from .models import Post

# Create your views here.

# class description(TemplateView):
#     template_name = "application/index.html"


#     def get(self, request):
#         return render(self.request, self.template_name)

def index(request):
    posts = Post.objects.order_by('-published') # ハイフンで逆順に
    return render(request, 'application/index.html', {'posts': posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'application/post.html',{'post':post})

def about(request):
    return render(request, 'application/about.html')

def contact(request):
    return render(request, 'application/contact.html')