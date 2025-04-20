from rest_framework import serializers
from GovtNotesManager.Models.ContentTextModel import ContentText

class ContentTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentText
        fields = '__all__'