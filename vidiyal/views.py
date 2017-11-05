from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Idea, Issue, Article
# Create your views here.
from rest_framework.views import APIView
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from .serializers import IdeaChartSerializer
from rest_framework.response import Response

def format_score(value):
    """Returns the score in thousands. Eg: 10.5k"""
    str_score = str(value)

    if int(value) < 1000:
        return str_score
    else:
        return str(str(int(value)/1000).join('k'))


class Index(TemplateView):
    """Returns the homepage"""
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        pass  # TODO: pass "new" contents


class IdeasList(ListView):
    template_name = 'ideas.html'
    model = Idea


class IssueList(ListView):
    template_name = 'issues.html'
    model = Issue


class IdeaDetail(DetailView):
    template_name = 'idea_view.html'
    model = Idea

    # def get_queryset(self):
    #     print(Idea.objects.filter(pk))

    # def get_object(self, queryset=None):
    #     idea_id = self.kwargs.get('idea_id')
    #     self.obj = get_object_or_404(Idea, id=idea_id)
    #     return self.obj


class IssueDetail(DetailView):
    template_name = 'issue_view.html'
    model = Issue


# class ChartData(viewsets.ModelViewSet):
def chart_data(request, pk):
    # id = kwargs.get('idea_id')
    print(pk)
    data = get_object_or_404(Idea, id=pk)

    if request.method == 'GET':
        serializer = IdeaChartSerializer(data)
        labels= ["Needed Fund", "Available Fund"]
        data = {
            "labels": labels,
            "data" : serializer.get_val(),
        }
        return JsonResponse(data)
    # authentication_classes = []
    # permission_classes = []
    # def get(self, response, format=None):
    #     labels = ["Needed fund", "Available fund"]
    #     dataset = [1000, 287]
    #     data = {
    #         "labels": labels,
    #         "data": dataset,
    #     }
    #     return Response(data)

class ChartData(APIView):
    def get_object(self, pk):
        return get_object_or_404(Idea, pk)

    def get(self, request, pk, format=None):
        idea = self.get_object(pk)
        serializer = IdeaChartSerializer(idea)
        return Response(serializer.data)


class DiscussionList(ListView):

    model = Article
    template_name = 'discussions.html'


class DiscussionDetail(DetailView):

    model = Article
    template_name = 'discussion_view.html'


def about(request):
    context = {}
    return render(
        request,
        'about.html',
        context=context,
    )

