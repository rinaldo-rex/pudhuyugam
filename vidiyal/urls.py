"""pudhuyugam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from .views import (
    Index,
    IdeasList,
    IssueList,
    IdeaDetail,
    IssueDetail,
    ChartData,
    chart_data,
    DiscussionList,
    DiscussionDetail,
)
urlpatterns = [
    url(r'^$', Index.as_view(), name='home'),
    url(r'^ideas/', IdeasList.as_view(), name='ideas'),
    url(r'^issues/', IssueList.as_view(), name='issues'),
    url(r'^idea/(?P<pk>\d+)/$', IdeaDetail.as_view(), name='idea-detail'),
    url(r'^issue/(?P<pk>\d+)/$', IssueDetail.as_view(), name='issue-detail'),
    url(r'^api/chart/idea/data/(?P<pk>\d+)/$', chart_data, name='api-chart-data'),
    url(r'^discussions/$', DiscussionList.as_view(), name='discussions'),
    url(r'^discussion/(?P<pk>\d+)/$', DiscussionDetail.as_view(), name='discussion-detail'),
    # url(r'^$'),
]
