from django.db import models
from Common import constants as ct
from GovtNotesManager.Models.ContentMappingModel import ContentMapping

class ContentText(models.Model):
    contentId = models.ForeignKey(ContentMapping, on_delete=models.CASCADE, related_name=ct.CONTEXT_TEXT,db_column="contentId")
    content_html = models.TextField()
    content_json = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ContentText"
