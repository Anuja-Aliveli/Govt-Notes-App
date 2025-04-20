from rest_framework import serializers
from GovtNotesManager.Models.ContentMappingModel import ContentMapping

class ContentMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentMapping
        fields = '__all__'