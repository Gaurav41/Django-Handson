from django.http.response import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.core.paginator import Paginator
# Create your views here.

## Pagination by function based views
def post_list(request):
    posts = Post.objects.all().order_by('id')
    paginator = Paginator(object_list=posts,per_page=3,orphans=1)
    page_num = request.GET.get("page")
    page = paginator.get_page(page_num)
    return render(request,"myapp/posts.html",{"page_obj":page})


## Pagination by class based views
class PostListView(ListView):
    model=Post
    template_name="myapp/posts.html"
    ordering=['id']
    paginate_by= 3 # 3 items per page
    paginate_orphans = 1 

    # def get_context_data(self, **kwargs):
    #     try:
    #         return super(PostListView,self).get_context_data(**kwargs)
    #     except Http404:
    #         self.kwargs['page']=1
    #         return super(PostListView,self).get_context_data(**kwargs)
    
    
    def paginate_queryset(self, queryset, page_size):
        try:
            return super().paginate_queryset(queryset, page_size)
        except Http404:
            self.kwargs['page']=1
            return super().paginate_queryset(queryset, page_size)


class PostDetailView(DetailView):
    model = Post
    template_name="myapp/post.html"

