import uuid
from django.db import models
from Common import constants as ct
from GovtNotesManager.Models.SubjectsModel import Subjects
from GovtNotesManager.Models.TopicsModel import Topics
from GovtNotesManager.Models.SubtopicsModel import Subtopics

class ContentMapping(models.Model):
    contentId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subjectId = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name=ct.CONTENT_MAPPINGS,db_column="subjectId")
    topicId = models.ForeignKey(Topics, on_delete=models.CASCADE, related_name=ct.CONTENT_MAPPINGS,db_column="topicId")
    subtopicId = models.ForeignKey(Subtopics, on_delete=models.CASCADE, related_name=ct.CONTENT_MAPPINGS,db_column="subtopicId")

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "ContentMapping"
