import uuid
from django.db import models
from django.utils.text import slugify
from Common import constants as ct
from GovtNotesManager.Models.TopicsModel import Topics

class Subtopics(models.Model):
    subtopicId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    topicId = models.ForeignKey(Topics, on_delete=models.CASCADE, related_name=ct.TOPICS_SUBTOPICS, db_column="topicId")
    subtopicName = models.CharField(max_length=ct.CHAR_MEDIUM_LIMIT, unique=True)
    subtopicDescription = models.TextField()
    subtopicSlug = models.SlugField(max_length=ct.CHAR_MEDIUM_LIMIT, unique=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdBy = models.CharField(max_length=ct.CHAR_MEDIUM_LIMIT, null=True, blank=True)
    updatedBy = models.CharField(max_length=ct.CHAR_MEDIUM_LIMIT, null=True, blank=True)

    class Meta:
        db_table = "Subtopics"

    def save(self, *args, **kwargs):
        if not self.subtopicSlug:
            self.subtopicSlug = slugify(self.subtopicName)
        super().save(*args, **kwargs)
