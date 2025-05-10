import uuid
from django.db import models
from django.utils.text import slugify
from Common import constants as ct
from GovtNotesManager.Models.SubjectCategoryModel import SubjectCategory

class Subjects(models.Model):
    subjectId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categoryId = models.ForeignKey(SubjectCategory, on_delete=models.CASCADE, related_name=ct.SUBJECT_CATEGORY,db_column="categoryId")
    subjectName = models.CharField(max_length=ct.CHAR_MEDIUM_LIMIT, unique=True)
    subjectDescription = models.TextField()
    subjectSlug = models.SlugField(max_length=ct.CHAR_MEDIUM_LIMIT, unique=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdBy = models.CharField(max_length=ct.CHAR_MEDIUM_LIMIT, null=True, blank=True)
    updatedBy = models.CharField(max_length=ct.CHAR_MEDIUM_LIMIT, null=True, blank=True)

    class Meta:
        db_table = "Subjects"

    def save(self, *args, **kwargs):
        if not self.subjectSlug:
            self.subjectSlug = slugify(self.subjectName)
        super().save(*args, **kwargs)
