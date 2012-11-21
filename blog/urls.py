from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views'
    url(r'^(?:page\/(?P<page\d+))?$', 'index'),
    url(r'^posts\/(?P<post_id\d+)[^\/]*?$',  'show')
)
