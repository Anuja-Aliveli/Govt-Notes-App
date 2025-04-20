from rest_framework import serializers
from GovtNotesManager.Models.TopicsModel import Topics

class TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = '__all__'