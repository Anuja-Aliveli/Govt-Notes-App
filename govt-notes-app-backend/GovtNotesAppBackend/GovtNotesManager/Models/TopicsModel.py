import uuid
from django.db import models
from django.utils.text import slugify
from Common import constants as ct
from GovtNotesManager.Models.SubjectsModel import Subjects

class Topics(models.Model):
    topicId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subjectId = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name=ct.SUBJECTS_TOPICS,db_column="subjectId")
    topicName = models.CharField(max_length=ct.CHAR_MEDIUM_LIMIT, unique=True)
    topicDescription = models.TextField()
    topicSlug = models.SlugField(max_length=ct.CHAR_MEDIUM_LIMIT, unique=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdBy = models.CharField(max_length=ct.CHAR_MEDIUM_LIMIT, null=True, blank=True)
    updatedBy = models.CharField(max_length=ct.CHAR_MEDIUM_LIMIT, null=True, blank=True)

    class Meta:
        db_table = "Topics"

    def save(self, *args, **kwargs):
        if not self.topicSlug:
            self.topicSlug = slugify(self.topicName)
        super().save(*args, **kwargs)
