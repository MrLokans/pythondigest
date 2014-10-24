from .feeds import AllEntriesFeed, RussianEntriesFeed, IssuesFeed
from django.conf.urls import patterns, url

from frontend.views import (
    Index,
    IssuesList,
    IssueView,
    HabrView,
    NewsList,
    AddNews,
    ViewEditorMaterial
)

urlpatterns = patterns('',
    url(r'^add/', AddNews.as_view(), name='addnews'),
    url(r'^feed/$', NewsList.as_view(), name='feed'),
    url(r'^rss/$', AllEntriesFeed(), name='rss'),
    url(r'^rss/ru/$', RussianEntriesFeed(), name='russian_rss'),
    url(r'^rss/issues/$', IssuesFeed(), name='issues_rss'),
    url(r'^issues/$', IssuesList.as_view(), name='issues'),
    url(r'^issue/(?P<pk>[0-9]+)/$', IssueView.as_view(), name='issue_view'),
    url(r'^habr/(?P<pk>[0-9]+)/$', HabrView.as_view(), name='habr_issue_view'),
    url(r'^(?P<section>[a-z\-]+)/(?P<slug>[a-z\-]+)/$', ViewEditorMaterial.as_view(), name='editor_material'),
    url(r'^(?P<slug>[a-z\-]+)/$', ViewEditorMaterial.as_view(), name='landing'),
    url(r'^$', Index.as_view(), name='home'),
)

