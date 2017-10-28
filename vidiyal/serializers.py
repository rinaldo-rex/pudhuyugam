# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Idea

class IdeaChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ('needed_fund', 'available_fund')
    #
    def get_val(self):
        data = []
        data.append(self.data['needed_fund'])
        data.append(self.data['available_fund'])
        return data