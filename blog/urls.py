from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from blog.models import Post

urlpatterns = patterns(''
    url(r'^(?:page\/(?P<page\d+))?$',
      ListView.as_view(
        queryset = Post.objects.order_by('-pub_date')[:5],
        context_object_name='posts'
        template_name='posts/index.html')),

    url(r'^posts\/(?P<post_id\d+)[^\/]*?$',
      ListView.as_view(
        model=Post,
        template_name='posts/show.html'))
)
