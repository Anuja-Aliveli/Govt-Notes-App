from rest_framework import serializers
from GovtNotesManager.Models.SubjectsModel import Subjects

class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'