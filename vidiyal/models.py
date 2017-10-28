from django.db import models
from django.urls import reverse
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
    # TODO: link an user to an idea -
    # created_by, last_update_by
    # relevant_image

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('idea-detail', args=[str(self.id)])

