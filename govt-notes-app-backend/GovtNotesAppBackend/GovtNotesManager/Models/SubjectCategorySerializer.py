from rest_framework import serializers
from GovtNotesManager.Models.SubjectCategoryModel import SubjectCategory

class SubjectsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectCategory
        fields = '__all__'