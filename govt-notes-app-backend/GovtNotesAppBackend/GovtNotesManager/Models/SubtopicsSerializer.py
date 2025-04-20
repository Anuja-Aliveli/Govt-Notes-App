from rest_framework import serializers
from GovtNotesManager.Models.SubtopicsModel import Subtopics

class SubtopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtopics
        fields = '__all__'