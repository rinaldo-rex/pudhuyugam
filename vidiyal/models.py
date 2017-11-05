from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField
# Create your models here.


class Idea(models.Model):
    title = models.CharField(max_length=50, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    desc = models.CharField(max_length=200) # short description
    description = models.TextField(max_length=20000) #long description
    feasibility_count = models.IntegerField(default=0)
    usability_count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    needed_fund = models.IntegerField(default=0)
    available_fund = models.IntegerField(default=0)
    issue = models.ForeignKey('Issue', on_delete=models.SET_NULL, null=True, blank=True)
    img_url = models.URLField(null=True, blank=True)
    # TODO: link an user to an idea -
    # created_by, last_update_by
    # relevant_image

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('idea-detail', args=[str(self.id)])


class Issue(models.Model):
    title = models.CharField(max_length=50, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    desc = models.CharField(max_length=200)  # short description
    description = models.TextField(max_length=20000)  # long description
    updated = models.DateTimeField(auto_now=True)
    img_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('issue-detail', args=[str(self.id)])


class Article(models.Model):
    """Each article that makes the discussion forum"""
    title = models.CharField(max_length=300, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    # content = models.TextField(blank=False, null=False)
    content = MarkdownxField(blank=False, null=False)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    # TODO: Author

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('discussion-detail', args=[str(self.id)])

